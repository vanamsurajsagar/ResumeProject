import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- 1. CORE FUNCTIONS ---

def extract_text_from_pdf(file):
    """Extracts text from an uploaded PDF file."""
    try:
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text.lower()
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""

def get_missing_skills(resume_text, job_desc):
    """Compares job description against a skill bank and the resume."""
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
        # Check if the skill is mentioned in the job but not in the resume
        if skill in job_desc_lower and skill not in resume_text_lower:
            missing.append(skill)
    return missing

# --- 2. USER INTERFACE (STREAMLIT) ---

st.set_page_config(page_title="AI Resume Matcher", page_icon="📄")

st.title("📄 AI Resume Matcher & Skill Suggester")
st.write("Analyze how well your resume matches a job description and find missing keywords.")

# Input Area
st.subheader("Configuration")
job_description = st.text_area("Paste the Job Description here:", height=200, placeholder="Example: We are looking for a Python developer with SQL and AWS experience...")
uploaded_file = st.file_uploader("Upload your Resume (PDF format only)", type="pdf")

# Execution
if st.button("Analyze Match"):
    if uploaded_file is not None and job_description.strip() != "":
        with st.spinner('Analyzing your resume...'):
            # Process text
            resume_text = extract_text_from_pdf(uploaded_file)
            
            if resume_text:
                # 1. Calculate Similarity Score
                text_content = [resume_text, job_description]
                cv = CountVectorizer()
                count_matrix = cv.fit_transform(text_content)
                similarity_score = cosine_similarity(count_matrix)[0][1] * 100
                
                # 2. Find Missing Skills
                missing_skills = get_missing_skills(resume_text, job_description)
                
                # --- 3. DISPLAY RESULTS ---
                st.markdown("---")
                st.subheader("Analysis Results")
                
                # Metric and Progress Bar
                st.metric(label="ATS Match Score", value=f"{similarity_score:.2f}%")
                st.progress(int(similarity_score))
                
                # Dashboard Layout
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("### Match Status")
                    if similarity_score >= 70:
                        st.success("✅ Strong Match! Your resume looks great for this role.")
                    elif similarity_score >= 40:
                        st.warning("🏃 Mid-Range Match. Consider adding more keywords.")
                    else:
                        st.error("❌ Low Match. You may need to tailor your resume significantly.")
                
                with col2:
                    st.write("### Skill Suggestions")
                    if missing_skills:
                        st.write("Found in Job Description but missing from your Resume:")
                        for skill in missing_skills:
                            st.info(f"• {skill.title()}")
                    else:
                        st.success("🎯 No major skill gaps detected!")
            else:
                st.error("Could not extract text from the PDF. Please try a different file.")
    else:
        st.error("Please upload a PDF file and paste a Job Description first.")

# Footer
st.markdown("---")
st.caption("Built with Python, Streamlit, and Scikit-Learn")