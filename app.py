import streamlit as st
import PyPDF2

# App Title
st.title("AI Resume Analyzer")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Your Resume (PDF)",
    type=["pdf"]
)

# Skills List
skills = [
    "python",
    "sql",
    "java",
    "power bi",
    "tableau",
    "machine learning",
    "data analytics",
    "excel",
    "artificial intelligence"
]

# If file uploaded
if uploaded_file is not None:

    # Read PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    text = text.lower()

    st.subheader("Resume Analysis")

    found_skills = []

    # Check skills
    for skill in skills:

        if skill in text:
            found_skills.append(skill)

    # Display skills
    st.write("Detected Skills:")

    st.write(found_skills)

    # Resume Score
    score = len(found_skills) * 10

    st.write("Resume Score:", score, "/ 100")

    # Suggestions
    st.subheader("Suggestions")

    if score < 50:
        st.write(
            "Add more technical skills and projects."
        )

    else:
        st.write(
            "Good resume with strong skills."
        )