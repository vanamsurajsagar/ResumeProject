# 📄 AI Resume Matcher & Skill Gap Finder

An intelligent resume analysis web application built with **Python and Streamlit** that compares a candidate's resume with a given job description.

The application extracts text from a PDF resume, calculates an **ATS-style similarity score** using **CountVectorizer and Cosine Similarity**, and identifies important skills mentioned in the job description that are missing from the resume.

---

## 🚀 Features

* 📄 **PDF Resume Upload**

  * Upload a resume in PDF format.
  * Extract resume content automatically using PyPDF2.

* 🎯 **ATS Match Score**

  * Compares the resume with the job description.
  * Uses text vectorization and cosine similarity to calculate a percentage-based match score.

* 🔍 **Skill Gap Analysis**

  * Checks the job description against a predefined skill bank.
  * Identifies skills that appear in the job description but are not found in the resume.

* 📊 **Match Status**

  * Displays the result using different match levels:

    * 🟢 **70%+** → Strong Match
    * 🟡 **40–69%** → Mid-Range Match
    * 🔴 **Below 40%** → Low Match

* 💡 **Skill Suggestions**

  * Highlights missing technical and professional keywords that could be relevant to the job description.

* 🖥️ **Interactive Streamlit Interface**

  * Simple and user-friendly web interface.
  * Real-time analysis without requiring a separate backend.

---

## 🧠 How It Works

The application follows a simple NLP-based workflow:

```text
        ┌──────────────────────┐
        │   Upload Resume PDF  │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Extract PDF Text     │
        │     using PyPDF2     │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Enter Job Description│
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ CountVectorizer      │
        │ Text Vectorization   │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Cosine Similarity    │
        │ Calculate Match %    │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Skill Gap Analysis   │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │ Results & Suggestions│
        └──────────────────────┘
```

---

## ⚙️ Technologies Used

| Technology            | Purpose                                                |
| --------------------- | ------------------------------------------------------ |
| **Python**            | Core programming language                              |
| **Streamlit**         | Web application and UI                                 |
| **PyPDF2**            | PDF text extraction                                    |
| **Scikit-learn**      | Text vectorization and similarity calculation          |
| **CountVectorizer**   | Converts text into numerical vectors                   |
| **Cosine Similarity** | Measures similarity between resume and job description |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/vanamsurajsagar/ResumeProject.git
```

### 2. Navigate to the project directory

```bash
cd ResumeProject
```

### 3. Install dependencies

```bash
pip install streamlit PyPDF2 scikit-learn
```

Or, if a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

Then open the local URL provided by Streamlit in your browser.

---

## 🖥️ Application Workflow

### Step 1 — Upload Resume

Upload your resume in **PDF format**.

### Step 2 — Add Job Description

Paste the complete job description into the text area.

### Step 3 — Analyze

Click:

```text
Analyze Match
```

The application processes both inputs and performs the analysis.

### Step 4 — View Results

The application displays:

* ATS Match Score
* Match Status
* Missing Skills
* Skill Suggestions

---

## 📊 Example Output

```text
ATS Match Score
       68.42%

Match Status
⚠️ Mid-Range Match.
Consider adding more relevant keywords.

Skill Suggestions

• AWS
• Docker
• Kubernetes
• REST
```

---

## 🧩 Skill Bank

The current application checks a predefined set of skills, including:

### Programming

* Python
* Java
* C++
* JavaScript

### Data & AI/ML

* Machine Learning
* Data Analysis
* TensorFlow
* PyTorch

### Web Development

* HTML
* CSS
* React
* Django
* Flask

### Cloud & DevOps

* AWS
* Docker
* Kubernetes
* Cloud

### Databases

* SQL
* NoSQL

### Tools

* Git
* GitHub
* Linux

### Professional Skills

* Communication
* Leadership
* Project Management
* Agile
* Scrum

---

## 🧮 Similarity Calculation

The project uses **CountVectorizer** to convert the resume and job description into numerical representations.

Then **Cosine Similarity** is used to measure how similar the two text documents are.

Conceptually:

```text
Resume Text
     +
Job Description
     ↓
CountVectorizer
     ↓
Numerical Vectors
     ↓
Cosine Similarity
     ↓
Similarity Score
     ↓
ATS Match Percentage
```

The resulting similarity value is converted into a percentage for easier interpretation.

---

## 🔍 Skill Gap Detection

The application maintains a predefined skill bank.

For every skill:

```text
Is skill present in Job Description?
              │
          ┌───┴───┐
         YES      NO
          │
          ▼
Is skill present in Resume?
          │
      ┌───┴───┐
     YES      NO
      │        │
      │        ▼
      │   Add to Missing Skills
      │
      ▼
    Ignore
```

This allows candidates to quickly identify keywords that may be worth addressing in their resume **when they accurately reflect their experience**.

---

## 📁 Project Structure

```text
ResumeProject/
│
├── app.py
├── README.md
├── requirements.txt
│
└── Resume/
    └── Resume.pdf
```

> Update the structure above if your actual filenames or folders are different.

---

## 🎯 Project Objective

The goal of this project is to demonstrate how **Natural Language Processing (NLP)** and **Machine Learning techniques** can be applied to a practical recruitment-related problem.

It provides a simple way for candidates to compare their resumes against job descriptions and identify potential keyword or skill gaps.

---

## 🔮 Future Improvements

Possible improvements for future versions include:

* 🤖 Use transformer-based NLP models such as BERT
* 🧠 Add semantic similarity instead of only word-frequency similarity
* 📑 Support DOCX resumes
* 📝 Generate resume improvement suggestions
* 🎯 Categorize skills into technical and soft skills
* 📊 Add detailed skill-match percentages
* 🔎 Detect job responsibilities and required qualifications
* 💼 Add multiple job-description comparison
* 📈 Provide a detailed ATS analysis dashboard
* ☁️ Deploy the application online
* 🔐 Improve handling of uploaded resume data

---

## ⚠️ Limitations

This project is an **ATS-style resume matching tool**, not a real commercial ATS system.

The current implementation primarily relies on:

* Word-frequency-based text representation
* Cosine similarity
* A predefined skill bank

Therefore, the score should be treated as an **approximate similarity indicator**, rather than a definitive measure of resume quality or hiring probability.

---

## 📚 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Python programming
* Streamlit application development
* PDF text extraction
* Natural Language Processing fundamentals
* Text vectorization
* Cosine similarity
* Keyword extraction
* Basic resume-job matching
* Building an interactive ML-based web application

---

## 👨‍💻 Author

**Vanam Surajsagar**

B.Tech – Computer Science & Engineering
Specialization: Artificial Intelligence & Machine Learning

### GitHub

https://github.com/vanamsurajsagar

---

## ⭐ Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

---

**Built with Python 🐍, Streamlit 🎈 and Scikit-learn 🤖**
