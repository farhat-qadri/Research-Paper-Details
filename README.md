# Research Paper Extractor

This is a simple **Flask web application** that allows users to upload research papers in **PDF format**. The application extracts metadata (title, authors, abstract, keywords, DOI, references) and sends it to the **Google Gemini API** for processing. The structured details are then displayed on the webpage and stored in an **Excel file** for download.

## Features
- Upload a **PDF research paper**
- Extract metadata using **Google Gemini API**
- Save extracted details into an **Excel sheet**
- Download the structured data


## Folder Structure
```
research-extractor/
│── app.py                     # Flask backend
│── templates/
│   │── index.html              # Upload page (Frontend)
│   │── results.html            # Display extracted details
│── static/
│   │── styles.css              # CSS for styling
│── uploads/                    # Folder to store uploaded PDFs and Excel files
│── processing/
│   │── extractor.py            # Handles text extraction & API calls
│── requirements.txt            # Dependencies
│── README.md                   # Documentation
```

## Setup & Installation
### **1. Clone the Repository**
```sh
git clone repo link
cd folder name
```

### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3. Configure Google Gemini API**
1. Get an API key from [Google AI Studio](https://aistudio.google.com/).
2. Set it in your environment variables or update `app.py`:
   ```python
   genai.configure(api_key="YOUR_GEMINI_API_KEY")
   ```

### **4. Run the Application**
```sh
python app.py
```
Go to `http://127.0.0.1:5000/` in your browser.

## Usage
1. Upload a **PDF file**.
2. Wait for the **extraction and processing**.
3. View extracted **metadata and entities**.
4. Download the structured **Excel file**.

## Technologies Used
- **Flask** → Web Framework
- **Google Gemini API** → AI-based extraction
- **pdfminer.six** → PDF text extraction
- **pandas & openpyxl** → Excel handling
- **HTML, CSS** → Frontend

