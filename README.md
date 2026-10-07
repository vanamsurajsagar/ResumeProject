# 🎯 AI Resume Matcher & Skill Gap Finder

> Find out what is missing in your resume and what to learn next.

A web application built with **Python and Streamlit** that compares a student's resume with an internship or job description, shows the **match score**, lists the **missing skills**, and creates a simple **2-week learning plan** to close the gap.

**🔗 Live demo:** https://resumeproject.streamlit.app/

---

## 🌍 Why this project

This project supports **UN Sustainable Development Goal 8: Decent Work and Economic Growth**.

Many students apply for internships and are not shortlisted, but they never find out why. They often do not know which skills a role really asks for, and free learning resources are scattered, so they do not know what to learn first.

This tool gives students a clear answer to two questions:

1. **What is missing in my resume for this role?**
2. **What should I learn in the next two weeks to fix it?**

## 🚀 Features

* 📄 **PDF resume upload**
  Upload a resume in PDF format. The text is extracted automatically with PyPDF2.

* 🎯 **ATS-style match score**
  Compares the resume with the job description using CountVectorizer and cosine similarity, and shows a percentage score.

* 🚦 **Match status**
  * 🟢 **70% and above:** Strong match
  * 🟡 **40% to 69%:** Mid-range match
  * 🔴 **Below 40%:** Low match

* 🔍 **Skill gap analysis**
  Checks the job description against a predefined skill bank and lists the skills the job mentions that the resume does not.

* 🗓️ **2-week learning plan** *(new)*
  Turns the most important missing skills into a simple plan:
  * **Week 1, Learn the basics:** a free resource for each skill.
  * **Week 2, Build and update:** a small practice project for each skill.

* 🎨 **Clean, colourful interface**
  Score card with a colour-coded bar, skill chips, and a week-by-week plan.

---

## 🧠 How it works

```text
   Upload resume (PDF)         Paste job description
            │                            │
            ▼                            │
   Extract text (PyPDF2)                 │
            │                            │
            └────────────┬───────────────┘
                         ▼
        CountVectorizer: text to numbers
                         │
                         ▼
        Cosine similarity: match percentage
                         │
                         ▼
        Skill gap analysis: skill bank check
                         │
                         ▼
        2-week learning plan: top missing skills
                         │
                         ▼
        Results: score, missing skills, plan
```

### Skill gap detection

For every skill in the skill bank, the app checks:

* Is the skill in the **job description**? If no, ignore it.
* Is the skill in the **resume**? If yes, ignore it.
* If it is in the job description but **not** in the resume, it is added to the missing skills.

Skills are matched as whole words, so for example "java" is not wrongly found inside "javascript".

### Building the learning plan

1. The missing skills are ranked by how many times the job description mentions them.
2. The top 4 are used. The rest are shown as "other missing skills for later".
3. Each skill gets one free learning resource (Week 1) and one small project (Week 2).
4. The plan reminds the student to add a skill to their resume **only if they really did the work**, then run the analysis again.

---

## 📊 Example output

Tested with a real web developer internship description:

```text
Overall Match: 27.4%  (Low match)

Missing skills: JavaScript, React, Django

Week 1: Learn the basics
  JavaScript: javascript.info
  React:      react.dev Learn
  Django:     Official Django tutorial

Week 2: Build and update
  JavaScript: Build a simple calculator web page
  React:      Build a small to-do app in React
  Django:     Build the polls app from the tutorial
```

---

## ⚙️ Technologies used

| Technology            | Purpose                                                |
| --------------------- | ------------------------------------------------------ |
| **Python**            | Core programming language                              |
| **Streamlit**         | Web application and interface                          |
| **PyPDF2**            | PDF text extraction                                    |
| **Scikit-learn**      | Text vectorization and similarity calculation          |
| **CountVectorizer**   | Converts text into numerical vectors                   |
| **Cosine similarity** | Measures similarity between resume and job description |

---

## 🧩 Skill bank

The app currently checks these skills:

| Category               | Skills                                                      |
| ---------------------- | ----------------------------------------------------------- |
| Programming            | Python, Java, C++, JavaScript                               |
| Data and AI/ML         | Machine Learning, Data Analysis, TensorFlow, PyTorch, Excel, Tableau, Power BI |
| Web development        | HTML, CSS, React, Django, Flask, API, REST                  |
| Cloud and DevOps       | AWS, Cloud, Docker, Kubernetes                              |
| Databases              | SQL, NoSQL                                                  |
| Tools                  | Git, GitHub, Linux                                          |
| Professional skills    | Communication, Leadership, Project Management, Agile, Scrum |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/vanamsurajsagar/ResumeProject.git
```

### 2. Go to the project folder

```bash
cd ResumeProject
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

---

## 🖥️ How to use

1. **Paste** the job or internship description.
2. **Upload** your resume as a PDF.
3. Click **Run Full Analysis**.
4. Read your **match score**, **missing skills** and **2-week learning plan**.

---

## 📁 Project structure

```text
ResumeProject/
├── app.py              # Streamlit app: logic and interface
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── screenshots/        # Images used in this README
```

---

## ⚠️ Limitations

This is an **ATS-style matching tool**, not a real commercial ATS. The score is an approximate indicator, not a measure of resume quality or hiring chances.

* The score uses word counts, so it does not understand meaning.
* The skill bank is limited. Skills that are not in it, such as PHP, Angular or Node.js, are not detected yet.
* Some short words, such as "rest", can match ordinary text and may be flagged by mistake.
* The learning resources are a fixed list that was chosen by hand.

---

## 🔮 Future improvements

* Use a smarter skill extractor (NLP or an LLM) instead of a fixed skill bank
* Use semantic similarity (for example BERT) instead of word counts only
* Support DOCX resumes
* Add more skills and learning resources, including regional-language resources
* Personalise the plan to the student's current level and career goal
* Send learning reminders by email or WhatsApp
* Compare one resume against several job descriptions

---

## 📚 What this project demonstrates

* Python and Streamlit application development
* PDF text extraction
* Text vectorization and cosine similarity
* Keyword-based skill extraction
* Turning analysis results into a practical, actionable plan

---

## 👨‍💻 Author

**Vanam Surajsagar**
B.Tech, Computer Science & Engineering (AI & ML)

GitHub: [github.com/vanamsurajsagar](https://github.com/vanamsurajsagar)

---

**Built with Python 🐍, Streamlit 🎈 and Scikit-learn 🤖**
