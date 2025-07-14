
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



### 🧪 How to Run Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/Ammar-Siddiqui/ai-resume-analyzer.git
   cd ai-resume-analyzer
   
2. **Create a virtual environment and activate it:**

   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. **Install requirements:**

   pip install -r requirements.txt

4. **Add your OpenAI key to a .env file:**

   OPENAI_API_KEY=your_key_here

5. Run the app:

   streamlit run app.py


