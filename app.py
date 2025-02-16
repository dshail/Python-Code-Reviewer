import os
import ast
import streamlit as st
import google.generativeai as genai
import difflib

# Securely fetch API Key from environment variable
api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    st.error("🚨 API key is missing! Set 'GENAI_API_KEY' as an environment variable.")
    st.stop()

genai.configure(api_key=api_key)

# System instruction for AI
system_prompt = """
You are an advanced Python code reviewer. Your task is to:
- Identify errors in the given Python code.
- Categorize issues as Syntax, Logic, or Performance-related.
- Suggest improvements or optimizations.
- Provide an overall rating (out of 5) based on code quality.
- Output the response in a structured format, including:
  - Errors categorized by type
  - Suggested fixes
  - Optimized code snippets
  - A final rating
"""

# Initialize Gemini AI
gemini = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)

# Streamlit UI
st.title("🚀 Python Code Reviewer with Gemini AI")
st.markdown("### 📝 Paste your Python code below:")
user_prompt = st.text_area("📌 Enter your Python code:", height=250)

# Syntax validation function
def is_valid_python_code(code):
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False

# Function to generate AI review
def generate_review(code):
    response = gemini.generate_content(code)
    return response.text

# Function to extract code improvements
def extract_suggestions(response_text):
    if "Suggested Improvements:" in response_text:
        return response_text.split("Suggested Improvements:")[-1].strip()
    return "No specific improvements suggested."

# Function to extract optimized code snippet
def extract_optimized_code(response_text):
    if "Optimized Code:" in response_text:
        return response_text.split("Optimized Code:")[-1].strip()
    return "No optimized code provided."

# Function to highlight code differences
def highlight_code_diff(original, optimized):
    diff = difflib.unified_diff(original.splitlines(), optimized.splitlines(), lineterm="")
    return "\n".join(diff)

# Process user input
if st.button("🔍 Review Code"):
    if not user_prompt.strip():
        st.warning("⚠️ Please enter a Python code snippet first.")
    elif not is_valid_python_code(user_prompt):
        st.error("🚨 Invalid Python code! Please check for syntax errors.")
    else:
        with st.spinner("🔎 Analyzing your code..."):
            ai_review = generate_review(user_prompt)

        # Display AI Review
        st.subheader("✅ AI Review:")
        st.write(ai_review)

        # Extract and display improvements
        suggestions = extract_suggestions(ai_review)
        st.subheader("💡 Suggested Improvements:")
        st.write(suggestions)

        # Extract and display optimized code
        optimized_code = extract_optimized_code(ai_review)
        if optimized_code != "No optimized code provided.":
            st.subheader("🔄 Optimized Code:")
            st.code(optimized_code, language="python")
            
            # Highlight differences
            diff_output = highlight_code_diff(user_prompt, optimized_code)
            st.subheader("📌 Code Differences:")
            st.code(diff_output, language="diff")

        # Extract rating if available
        if "Rating:" in ai_review:
            rating = ai_review.split("Rating:")[-1].strip().split("\n")[0]
            st.subheader(f"⭐ Code Quality Rating: {rating}/5")

        # Download AI Review Report
        if st.button("📥 Download Review Report"):
            with open("review_report.txt", "w") as f:
                f.write(ai_review)
            st.download_button(label="Download Report", data=ai_review, file_name="review_report.txt", mime="text/plain")

# End of script
