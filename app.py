import streamlit as st
from resume_utils import extract_text_from_pdf, compute_similarity
from dotenv import load_dotenv
import os
import openai

load_dotenv()

def get_gpt_resume_feedback(resume_text, job_desc=""):
    if job_desc.strip():
        prompt = f"""You are a professional career coach.
Review the following resume for the given job description.
Suggest specific improvements for clarity, impact, and alignment with the job.
List missing skills or keywords. Make your suggestions as a bullet list.

Resume:
{resume_text}

Job Description:
{job_desc}
"""
    else:
        prompt = f"""You are a professional career coach.
Review the following resume and suggest specific improvements for clarity, impact, and keyword alignment.
Make your suggestions as a bullet list.

Resume:
{resume_text}
"""

    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except openai.RateLimitError:
        return "⚠️ You have exceeded your OpenAI API quota. Please check your account billing or usage."
    except Exception as e:
        return f"⚠️ An error occurred: {str(e)}"

st.title("📄 AI Resume Analyzer")

resume_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
job_description = st.text_area("Paste the job description here (optional, but recommended for tailored feedback)")

# Only proceed if the resume is uploaded
if resume_file:
    resume_text = extract_text_from_pdf(resume_file)

    score, resume_keywords, job_keywords = compute_similarity(resume_text, job_description)

    st.markdown(f"### ✅ Match Score: **{score*100:.2f}%**")
    st.markdown("**Resume Keywords:** " + ", ".join(resume_keywords))
    st.markdown("**Job Keywords:** " + ", ".join(job_keywords))

    missing = list(set(job_keywords) - set(resume_keywords))
    if missing:
        st.warning("⚠️ Missing Keywords: " + ", ".join(missing))
    else:
        st.success("Your resume covers all the job keywords!")

    if st.button("Get AI Feedback 🤖"):
        with st.spinner("Generating AI-powered feedback..."):
            if len(job_description.strip()) >= 10:
                feedback = get_gpt_resume_feedback(resume_text, job_description)
            else:
                st.info("No job description entered. You'll get general feedback.")
                feedback = get_gpt_resume_feedback(resume_text, "")

            st.subheader("AI Suggestions 🤖 ")
            st.markdown(feedback)
