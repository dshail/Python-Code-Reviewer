# Python Code Reviewer

A Streamlit-based web application that uses Google Gemini AI to review Python code, identify errors, suggest improvements, and rate the code.

## Features
✅ AI-powered Python Code Review  
✅ Error Identification & Categorization (Syntax, Logic, Performance)  
✅ Automated Refactoring Suggestions  
✅ Code Quality Rating (Out of 5)  
✅ Code Difference Highlighting  
✅ Downloadable AI Review Report  
✅ Simple and Interactive UI using Streamlit  

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/dshail/Python-Code-Reviewer.git
cd Python-Code-Reviewer
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key
Create a `.env` file and add your Gemini API key:
```bash
echo "GENAI_API_KEY=your_google_gemini_api_key" > .env
```
Or set it manually in your environment:
```bash
export GENAI_API_KEY=your_google_gemini_api_key
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

## Deployment
Deploy on Streamlit Cloud or any cloud provider supporting Streamlit. Enable auto-update for GitHub changes.

## Topics
python  streamlit  ai  code-review  generative-ai  google-gemini  machine-learning  automation  refactoring  error-detection

---

Contributions are welcome! Feel free to open an issue or submit a pull request. 😊
