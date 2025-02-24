from flask import Flask, render_template, request, redirect, url_for
import os
import google.generativeai as genai
from werkzeug.utils import secure_filename
from pdfminer.high_level import extract_text
import json

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    return extract_text(pdf_path)

def send_to_gemini(pdf_text):
    genai.configure(api_key="AIzaSyAcvN5DD5d23fRVaHN6F6k8kPI-kJ4nN4A")
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    prompt = f"""
    Extract the following details from the research paper and return the output as a JSON object:
    {{
        "Title": "<Title of the paper>",
        "Authors": ["<List of authors>"],
        "Keywords": ["<List of keywords>"],
        "DOI": "<DOI if available>",
        "Journal/ Conference name": "<Journal or Conference name>",
        "Journal/ Conference website": "<URL of the Journal/Conference if available>",
        "Affiliations": ["<List of affiliations>"]
    }}
    
    Text:
    {pdf_text}
    """

    response = model.generate_content(prompt)
    cleaned_text = response.text.replace("```json", "").replace("```", "").strip()
    cleaned_text = json.loads(cleaned_text)
    print("HAHHAHAHAAHAH")
    print(cleaned_text)
    return cleaned_text
    
@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    files = request.files.getlist('file')
    if not files:
        return redirect(request.url)
    
    results = []  # List to store response details for each file
    
    for file in files:
        if file.filename == '':
            continue  # Skip files with no filename
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Extract text and send to Gemini for this file
            pdf_text = extract_text_from_pdf(file_path)
            gemini_response = send_to_gemini(pdf_text)
            
            results.append({
                'filename': filename,
                'response': gemini_response
            })
    
    return render_template('results.html', response=results)



@app.route('/success/<filename>')
def upload_success(filename):
    return f"File '{filename}' uploaded successfully! (Next: Process with Gemini API)"

if __name__ == '__main__':
    app.run(debug=True)
