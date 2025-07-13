
# 📄 AI Resume Analyzer


Hi! Welcome to my first AI side project. 



An intelligent, interactive web app that helps job seekers optimize their resumes by comparing them to job descriptions and generating personalized feedback using OpenAI's GPT models.

---

## 🚀 Features

- ✅ **PDF Resume Upload**
- 🧠 **Job Description Matching**
- 📊 **Keyword Extraction & Match Score**
- 🤖 **AI-Powered Resume Feedback**
- ⚠️ **Missing Keyword Alerts**

---

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/) – Web app framework
- [spaCy](https://spacy.io/) – NLP for keyword extraction
- [OpenAI GPT-3.5 Turbo](https://platform.openai.com/) – AI resume suggestions
- [Python](https://www.python.org/) – Core language
- [dotenv](https://pypi.org/project/python-dotenv/) – Environment variable management

---

## 📂 Project Structure

```bash
ai-resume-analyzer/
├── app.py                 # Main Streamlit application
├── resume_utils.py        # PDF extraction + similarity scoring
├── requirements.txt       # Dependencies
├── .env                   # Your OpenAI API key (not uploaded to GitHub)
└── README.md              # This file

How to Run Locally

1. Clone the repo:

bash
Copy
Edit
git clone https://github.com/Ammar-Siddiqui/ai-resume-analyzer.git
cd ai-resume-analyzer
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add your OpenAI key to a .env file:

bash
Copy
Edit
OPENAI_API_KEY=your_key_here
Run the app:

bash
Copy
Edit
streamlit run app.py

