import streamlit as st
from openai_helper import call_openai
from resume_to_text import extract_text_from_file, extract_university_name, extract_company_name
from linkedin_prompts import FULL_LINKEDIN_OPTIMIZATION_PROMPT
from suggestion_helper import fetch_real_connections, fetch_recruiters

st.set_page_config(page_title="LinkedIn Optimizer - General Mode", layout="centered")
st.title("🔗 AI LinkedIn Optimizer (General Mode)")
st.markdown("Boost your visibility, credibility, and hiring chances — powered by AI 💼")

uploaded_resume = st.file_uploader("📎 Upload Your Resume", type=["pdf", "docx", "txt"])
target_role = st.text_input("🎯 Target Role", placeholder="e.g., AI Product Manager")
location = st.text_input("🌍 Preferred Country/Location (optional)", placeholder="e.g., USA, Germany")
status = st.radio("🧑‍💼 Are you currently job seeking or employed?", ["Looking for a Job", "Currently Employed"])

if st.button("🚀 Optimize My LinkedIn") and uploaded_resume and target_role:
    resume_text = extract_text_from_file(uploaded_resume)
    university = extract_university_name(resume_text)
    company = extract_company_name(resume_text)

    with st.spinner("🔍 Analyzing your resume and generating your optimized profile..."):
        prompt = FULL_LINKEDIN_OPTIMIZATION_PROMPT.format(
            resume=resume_text,
            role=target_role,
            location=location or "Not specified",
            status=status
        )
        profile_response = call_openai(prompt)

    st.success("✅ Optimization complete!")

    st.subheader("🔹 Optimized LinkedIn Profile Content")
    st.markdown(profile_response)

    try:
        st.subheader("🔗 Top Suggested Connections")
        suggested_connections = fetch_real_connections(
            role=target_role,
            location=location or "",
            university=university,
            company=company
        )
        if suggested_connections:
            for name, link in suggested_connections:
                st.markdown(f"- [{name}]({link})", unsafe_allow_html=True)
        else:
            st.warning(f"No direct profiles found. Try [Google Search for {target_role} in {location}](https://www.google.com/search?q=site:linkedin.com/in+{target_role}+{location})")
    except Exception as e:
        st.error(f"❌ Could not fetch suggested connections: {e}")

    if status == "Looking for a Job":
        try:
            st.subheader("💼 Potential Recruiters")
            recruiters = fetch_recruiters(role=target_role, location=location or "")
            if recruiters:
                for name, link in recruiters:
                    st.markdown(f"- [{name}]({link})", unsafe_allow_html=True)
            else:
                st.warning(f"No recruiters found. Try [Google Search for {target_role} recruiter in {location}](https://www.google.com/search?q=site:linkedin.com/in+recruiter+{target_role}+{location})")
        except Exception as e:
            st.error(f"❌ Could not fetch recruiters: {e}")
else:
    st.info("📌 Please upload a resume and enter a target role to begin.")
