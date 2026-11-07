import streamlit as st

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from job_matcher import calculate_match
from career_recommender import recommend_careers


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="CareerAI | Career Guidance",
    page_icon="🚀",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.stApp {
    background-color: #F4F7FC;
}

.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1 {
    color: #173B70;
    font-weight: 800;
}

h2, h3 {
    color: #244B78;
}

div[data-testid="stMetric"] {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #DCE5F1;
    box-shadow: 0 3px 10px rgba(0,0,0,0.05);
}

.stButton button {
    background-color: #2463EB;
    color: white;
    border-radius: 8px;
    border: none;
    font-weight: bold;
    width: 100%;
}

.stButton button:hover {
    background-color: #1748B8;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #E8EFFA;
}

div[data-testid="stProgress"] > div > div {
    background-color: #2463EB;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.title("🚀 CareerAI")

st.subheader("AI-Powered Resume Analyzer & Career Guidance")

st.write(
    "Analyze your resume, match job requirements, "
    "identify missing skills and discover career opportunities."
)

st.divider()


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("🚀 CareerAI")

    st.markdown("### Your Career Assistant")

    st.write(
        "Get insights into your professional skills "
        "and discover opportunities for improvement."
    )

    st.divider()

    st.markdown("### Features")

    st.write("📄 Resume Analysis")
    st.write("📊 Job Matching")
    st.write("📌 Missing Skills")
    st.write("🎯 Career Recommendations")
    st.write("📈 Skill Coverage")

    st.divider()

    st.caption("CareerAI | AI-Powered Career Guidance")


# ---------------- INPUT SECTION ----------------

st.header("📂 Upload Your Details")

col1, col2 = st.columns(2)

with col1:

    uploaded_file = st.file_uploader(
        "📄 Upload Your Resume (PDF)",
        type=["pdf"]
    )

with col2:

    job_description = st.text_area(
        "💼 Paste Job Description",
        height=180,
        placeholder="Enter job title and required skills..."
    )


analyze = st.button(
    "🚀 Analyze My Resume",
    use_container_width=True
)


# ---------------- ANALYSIS ----------------

if analyze:

    if uploaded_file and job_description.strip():

        with st.spinner("Analyzing your resume..."):

            resume_text = extract_resume_text(uploaded_file)

            if resume_text and resume_text.strip():

                skills = extract_skills(resume_text)

                result = calculate_match(
                    resume_text,
                    job_description
                )

                recommendations = recommend_careers(skills)

                # ---------------- RESUME SKILLS ----------------

                st.divider()

                st.header("📄 Resume Analysis")

                st.subheader("Skills Found")

                if skills:

                    st.success(
                        "Your resume contains "
                        + str(len(skills))
                        + " recognized skills."
                    )

                    st.write(", ".join(skills))

                else:

                    st.warning("No known skills detected.")

                # ---------------- JOB MATCHING ----------------

                st.divider()

                st.header("📊 Job Matching Results")

                col1, col2, col3 = st.columns(3)

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

                with col3:

                    st.metric(
                        "Skills Found",
                        len(skills)
                    )

                match_score = max(
                    0,
                    min(100, float(result["match_score"]))
                )

                st.progress(
                    match_score / 100,
                    text=f"Overall Skill Match: {match_score:.2f}%"
                )

                # ---------------- MATCHED SKILLS ----------------

                col1, col2 = st.columns(2)

                with col1:

                    st.subheader("✅ Matched Skills")

                    if result["matched_skills"]:

                        for skill in result["matched_skills"]:

                            st.write("🟢", skill)

                    else:

                        st.info("No matching skills found.")

                with col2:

                    st.subheader("📌 Missing Skills")

                    if result["missing_skills"]:

                        for skill in result["missing_skills"]:

                            st.write("🔴", skill)

                    else:

                        st.success("No missing skills!")

                # ---------------- CAREER RECOMMENDATIONS ----------------

                st.divider()

                st.header("🎯 Career Recommendations")

                st.write(
                    "Explore career paths based on your "
                    "current resume skills."
                )

                if recommendations:

                    for item in recommendations:

                        with st.container():

                            st.subheader(
                                "💼 " + item["career"]
                            )

                            score = max(
                                0,
                                min(100, float(item["score"]))
                            )

                            st.metric(
                                "Skill Coverage",
                                f"{score:.2f}%"
                            )

                            st.progress(
                                score / 100
                            )

                            st.write(
                                "**Matching Skills:**",
                                ", ".join(item["matched"])
                                if item["matched"]
                                else "No matching skills"
                            )

                            st.divider()

                else:

                    st.info("No career recommendations available.")

                # ---------------- FINAL MESSAGE ----------------

                st.success(
                    "Resume analysis completed successfully!"
                )

                st.caption(
                    "CareerAI | Your journey towards a better career starts here."
                )

            else:

                st.error("Could not read your resume.")

    else:

        st.warning(
            "Please upload your resume and enter a job description."
        )


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "© 2026 CareerAI | AI-Powered Resume Analysis and Career Guidance"
)