import re
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
SKILL_BANK = [
    "python", "java", "sql", "javascript", "aws", "docker", "kubernetes",
    "machine learning", "excel", "react", "c++", "tableau", "power bi",
    "communication", "leadership", "project management", "git", "github",
    "agile", "scrum", "data analysis", "api", "rest", "nosql", "cloud",
    "linux", "html", "css", "django", "flask", "tensorflow", "pytorch"
]

def has_skill(skill, text):
    # whole-word match, so "java" is not found inside "javascript"
    pattern = r"(?<![a-z0-9+])" + re.escape(skill) + r"(?![a-z0-9+])"
    return re.search(pattern, text) is not None

def get_missing_skills(resume_text, job_desc):
    missing = []
    job_desc_lower = job_desc.lower()
    resume_text_lower = resume_text.lower()
    for skill in SKILL_BANK:
        # If the skill is in the JOB but NOT in the RESUME
        if has_skill(skill, job_desc_lower) and not has_skill(skill, resume_text_lower):
            missing.append(skill)
    return missing

# 3. NEW: LEARNING PLAN
# For each skill: (free resource to learn from, small project to practice)
LEARNING_GUIDE = {
    "python": ("Kaggle Learn: Python", "Write a script that reads a CSV file and prints a summary"),
    "java": ("MOOC.fi Java Programming (free)", "Build a console to-do list app"),
    "sql": ("SQLBolt interactive lessons", "Create a small student database and write 10 queries"),
    "javascript": ("javascript.info", "Build a simple calculator web page"),
    "aws": ("AWS Skill Builder: Cloud Practitioner Essentials (free)", "Host a static web page on AWS S3"),
    "docker": ("Docker official Get Started guide", "Put your Streamlit app in a Docker container"),
    "kubernetes": ("Kubernetes Basics tutorial on kubernetes.io", "Run a sample app on a local cluster (minikube)"),
    "machine learning": ("Kaggle Learn: Intro to Machine Learning", "Train a simple model on a Kaggle dataset"),
    "excel": ("Microsoft Learn: Excel training", "Build a small sheet with formulas and a chart"),
    "react": ("react.dev Learn", "Build a small to-do app in React"),
    "c++": ("learncpp.com", "Write a small program with classes, like a bank account"),
    "tableau": ("Tableau free training videos", "Make a dashboard from a public dataset"),
    "power bi": ("Microsoft Learn: Power BI training", "Make a sales dashboard from a sample file"),
    "communication": ("Practice task (no course needed)", "Record a 2-minute video explaining one of your projects"),
    "leadership": ("Practice task (no course needed)", "Lead a small team task or study group and write down what you learned"),
    "project management": ("Atlassian Agile Coach (free)", "Plan one of your projects with a task board (Trello or Jira)"),
    "git": ("Pro Git book (free)", "Create a repo, make 5 commits and one branch"),
    "github": ("GitHub Skills (free)", "Publish one project with a clear README"),
    "agile": ("Atlassian Agile Coach (free)", "Plan your next project in 1-week sprints"),
    "scrum": ("The Scrum Guide (free, scrumguides.org)", "Run a mock sprint planning for one of your projects"),
    "data analysis": ("Kaggle Learn: Pandas and Data Visualization", "Analyse one dataset and write 5 findings"),
    "api": ("Postman Learning Center (free)", "Call a public API from Python and show the result"),
    "rest": ("Postman Learning Center (free)", "Build a tiny REST API with Flask"),
    "nosql": ("MongoDB University free courses", "Store and query student records in MongoDB"),
    "cloud": ("AWS Skill Builder: Cloud Practitioner Essentials (free)", "Deploy one small app to a free cloud tier"),
    "linux": ("Linux Journey (linuxjourney.com)", "Do a day of your work using only the terminal"),
    "html": ("MDN Web Docs: Learn HTML", "Build a one-page personal portfolio"),
    "css": ("MDN Web Docs: Learn CSS", "Style your portfolio page to work on mobile"),
    "django": ("Official Django tutorial", "Build the polls app from the tutorial"),
    "flask": ("Official Flask quickstart", "Build a small notes app with Flask"),
    "tensorflow": ("TensorFlow official tutorials", "Train an image classifier on a small dataset"),
    "pytorch": ("PyTorch official tutorials", "Train a small neural network on a simple dataset"),
}

def build_learning_plan(missing_skills, job_desc, max_skills=4):
    job_desc_lower = job_desc.lower()
    # Most important first: skills the job description mentions the most
    ranked = sorted(missing_skills, key=lambda s: job_desc_lower.count(s), reverse=True)
    top = ranked[:max_skills]
    week1 = []  # learn
    week2 = []  # build
    for skill in top:
        resource, project = LEARNING_GUIDE.get(
            skill, ("Search for a beginner course on " + skill, "Make a small project using " + skill))
        week1.append((skill, resource))
        week2.append((skill, project))
    return week1, week2, ranked[max_skills:]

# 4. LOOK AND FEEL (custom CSS)
st.set_page_config(page_title="Skill-Job Match", page_icon="🎯", layout="centered")

st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #eef2ff 0%, #fdf2f8 100%); }
.hero { background: linear-gradient(120deg, #4f46e5 0%, #7c3aed 50%, #06b6d4 100%);
        padding: 28px 30px; border-radius: 18px; color: #ffffff; margin-bottom: 22px;
        box-shadow: 0 10px 25px rgba(79,70,229,0.25); }
.hero h1 { color: #ffffff; margin: 0; font-size: 2rem; }
.hero p { color: #e0e7ff; margin: 8px 0 0 0; font-size: 1.02rem; }
.card { background: #ffffff; color: #1f2937; padding: 20px 22px; border-radius: 16px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.08); margin-bottom: 16px; }
.card h3 { margin: 0 0 10px 0; color: #1f2937; font-size: 1.1rem; }
.score { font-size: 3rem; font-weight: 800; line-height: 1; }
.bar { background: #e5e7eb; border-radius: 999px; height: 14px; margin-top: 12px; overflow: hidden; }
.bar > div { height: 14px; border-radius: 999px; }
.chip { display: inline-block; background: #fee2e2; color: #b91c1c; padding: 6px 14px;
        border-radius: 999px; margin: 4px 6px 4px 0; font-weight: 600; font-size: 0.92rem; }
.chip-ok { background: #dcfce7; color: #15803d; }
.step { padding: 10px 12px; border-radius: 10px; margin: 8px 0; color: #1f2937; font-size: 0.95rem; }
.w1 { background: #e0f2fe; border-left: 5px solid #0284c7; }
.w2 { background: #fef3c7; border-left: 5px solid #d97706; }
.small { color: #4b5563; font-size: 0.92rem; }
</style>
""", unsafe_allow_html=True)

def level(score):
    if score >= 70:
        return "#16a34a", "Strong match", "Your resume fits this role well."
    if score >= 40:
        return "#d97706", "Mid-range match", "Add more relevant keywords where they are true for you."
    return "#dc2626", "Low match", "Try tailoring your resume to this role."

def score_card(score):
    color, title, tip = level(score)
    width = max(2, min(100, int(score)))
    return (
        '<div class="card"><h3>Overall Match</h3>'
        f'<div class="score" style="color:{color}">{score:.1f}%</div>'
        f'<div class="bar"><div style="width:{width}%; background:{color}"></div></div>'
        f'<p style="margin:12px 0 0 0; color:#1f2937"><b style="color:{color}">{title}.</b> {tip}</p></div>'
    )

def chips_card(skills):
    if skills:
        body = "".join(f'<span class="chip">{s.title()}</span>' for s in skills)
        note = '<p class="small" style="margin:8px 0 0 0">Skills the job mentions that your resume does not.</p>'
    else:
        body = '<span class="chip chip-ok">No major skill gaps found</span>'
        note = ""
    return f'<div class="card"><h3>Missing skills</h3>{body}{note}</div>'

def plan_card(title, css, rows, icon):
    body = "".join(f'<div class="step {css}">{icon} <b>{s.title()}:</b> {t}</div>' for s, t in rows)
    return f'<div class="card"><h3>{title}</h3>{body}</div>'

# 5. PAGE
st.markdown(
    '<div class="hero"><h1>🎯 AI Resume Matcher &amp; Skill Gap Finder</h1>'
    '<p>Find out what is missing in your resume and what to learn next.</p></div>',
    unsafe_allow_html=True)

left, right = st.columns(2)
with left:
    job_description = st.text_area("Paste the Job Description here:", height=220)
with right:
    uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

if st.button("🚀 Run Full Analysis", use_container_width=True):
    if uploaded_file and job_description:
        with st.spinner("Calculating scores..."):
            resume_text = extract_text_from_pdf(uploaded_file)

            # Logic for Score
            content = [resume_text, job_description]
            cv = CountVectorizer()
            matrix = cv.fit_transform(content)
            score = cosine_similarity(matrix)[0][1] * 100

            missing_skills = get_missing_skills(resume_text, job_description)

        c1, c2 = st.columns(2)
        with c1:
            st.markdown(score_card(score), unsafe_allow_html=True)
        with c2:
            st.markdown(chips_card(missing_skills), unsafe_allow_html=True)

        if missing_skills:
            week1, week2, extra = build_learning_plan(missing_skills, job_description)
            st.markdown("### 🗓️ Your 2-Week Learning Plan")
            p1, p2 = st.columns(2)
            with p1:
                st.markdown(plan_card("Week 1: Learn the basics", "w1", week1, "📘"), unsafe_allow_html=True)
            with p2:
                st.markdown(plan_card("Week 2: Build and update", "w2", week2, "🛠️"), unsafe_allow_html=True)
            st.markdown(
                '<div class="card"><p class="small" style="margin:0">📝 At the end, add these skills to your resume '
                'only if you really did the work, then run the analysis again to see your new score.</p></div>',
                unsafe_allow_html=True)
            if extra:
                st.info("Other missing skills for later: " + ", ".join(s.title() for s in extra))
    else:
        st.error("Please provide both a resume and a job description.")