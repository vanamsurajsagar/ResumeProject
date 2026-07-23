import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Improved Text Extraction
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text.lower()

# 2. SMARTER SKILL BANK
def get_missing_skills(resume_text, job_desc):
    # Expanded list - you can add even more words inside these brackets!
    skill_bank = [
        "python", "java", "sql", "javascript", "aws", "docker", "kubernetes",
        "machine learning", "excel", "react", "c++", "tableau", "power bi",
        "communication", "leadership", "project management", "git", "github",
        "agile", "scrum", "data analysis", "api", "rest", "nosql", "cloud",
        "linux", "html", "css", "django", "flask", "tensorflow", "pytorch"
    ]
    
    missing = []
    job_desc_lower = job_desc.lower()
    resume_text_lower = resume_text.lower()
    
    for skill in skill_bank:
        # If the skill is in the JOB but NOT in the RESUME
        if skill in job_desc_lower and skill not in resume_text_lower:
            missing.append(skill)
    return missing

# 3. UI Setup
st.set_page_config(page_title="Pro Resume Analyzer", layout="centered")
st.title("📄 AI Resume Matcher & Skill Gap Finder")

job_description = st.text_area("Paste the Job Description here:", height=200)
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

if st.button("Run Full Analysis"):
    if uploaded_file and job_description:
        with st.spinner('Calculating scores...'):
            resume_text = extract_text_from_pdf(uploaded_file)
            
            # Logic for Score
            content = [resume_text, job_description]
            cv = CountVectorizer()
            matrix = cv.fit_transform(content)
            score = cosine_similarity(matrix)[0][1] * 100
            
            # --- DISPLAY RESULTS ---
            st.divider()
            st.subheader(f"Overall Match: {score:.2f}%")
            st.progress(int(score)) # Visual progress bar
            
            # Skill Gap Analysis
            missing_skills = get_missing_skills(resume_text, job_description)
            
            col1, col2 = st.columns(2)
            
            with col1:
                if score > 70:
                    st.success("High Match! Your resume is strong for this role.")
                else:
                    st.warning("Low Match. Try tailoring your resume.")
            
            with col2:
                if missing_skills:
                    st.subheader("💡 Missing Keywords")
                    for skill in missing_skills:
                        st.write(f"❌ {skill.title()}")
                else:
                    st.success("🎯 No major skill gaps found!")
    else:
        st.error("Please provide both a resume and a job description.")