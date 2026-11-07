import streamlit as st

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from job_matcher import calculate_match
from career_recommender import recommend_careers

st.set_page_config(
    page_title="CareerAI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerAI")
st.subheader("AI-Powered Resume Analyzer")

st.divider()

uploaded_file = st.file_uploader(
    "📄 Upload Your Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "💼 Paste Job Description",
    height=180
)

if st.button("Analyze Resume"):

    if uploaded_file and job_description.strip():
      
        resume_text = extract_resume_text(uploaded_file)

        if resume_text.strip():

            skills = extract_skills(resume_text)

            st.header("📄 Resume Analysis")

            st.write("### Skills Found")

            if skills:
                st.write(", ".join(skills))
            else:
                st.warning("No known skills detected.")

            result = calculate_match(
                resume_text,
                job_description
            )

            st.divider()
            st.header("📊 Job Matching Results")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Skill Match",
                    f"{result['match_score']}%"
                )

            with col2:
                st.metric(
                    "Text Similarity",
                    f"{result['similarity']}%"
                )

            st.progress(result["match_score"] / 100)

            st.subheader("✅ Matched Skills")

            for skill in result["matched_skills"]:
                st.write("✅", skill)

            st.subheader("📌 Missing Skills")

            for skill in result["missing_skills"]:
                st.write("📌", skill)

            st.divider()

            st.header("🎯 Career Recommendations")

            recommendations = recommend_careers(skills)

            for item in recommendations:

                st.subheader(item["career"])

                st.metric(
                    "Skill Coverage",
                    f"{item['score']}%"
                )

                st.write(
                    "Matching skills:",
                    ", ".join(item["matched"])
                    if item["matched"]
                    else "No matching skills"
                )

                st.progress(item["score"] / 100)

        else:
            st.error("Could not read your resume.")

    else:
        st.warning(
            "Please upload your resume and enter a job description."
        )