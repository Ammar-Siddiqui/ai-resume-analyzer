import streamlit as st
from resume_utils import extract_text_from_pdf , compute_similarity

st.title("📄 AI Resume Analyzer")


resume_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
job_description = st.text_area("Paste the job description here")

if resume_file and job_description:

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



    


