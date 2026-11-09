import streamlit as st

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from job_matcher import calculate_match
from career_recommender import recommend_careers
from report_generator import generate_report


# ----------------------------------
# PAGE CONFIGURATION
# ----------------------------------

st.set_page_config(
    page_title="CareerAI | Smart Career Guidance",
    page_icon="🚀",
    layout="wide"
)


# ----------------------------------
# CUSTOM CSS
# ----------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #071426, #101d38);
    color: #ffffff;
}

header[data-testid="stHeader"] {
    background: transparent;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #101a32, #172b4d);
}

section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

.main-title {
    background: linear-gradient(90deg, #06b6d4, #6366f1);
    padding: 35px;
    border-radius: 18px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
}

.main-title h1 {
    color: white;
    font-size: 42px;
}

.main-title p {
    color: white;
    font-size: 17px;
}

.section-card {
    background: #172b4d;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #334b70;
    margin-bottom: 15px;
}

div[data-testid="stMetric"] {
    background: #172b4d;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #334b70;
}

div[data-testid="stMetric"] label {
    color: #cbd5e1 !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    color: #38bdf8 !important;
}

.stButton button,
.stDownloadButton button {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 20px;
    font-weight: bold;
    width: 100%;
}

.stButton button:hover,
.stDownloadButton button:hover {
    background: linear-gradient(90deg, #0891b2, #4f46e5);
    color: white;
    border: none;
}

input, textarea {
    background-color: #ffffff !important;
    color: #111827 !important;
}

[data-testid="stFileUploader"] {
    background: #172b4d;
    padding: 12px;
    border-radius: 12px;
}

[data-testid="stFileUploader"] * {
    color: white;
}

hr {
    border-color: #334b70;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------------
# SIDEBAR
# ----------------------------------

with st.sidebar:

    st.title("🚀 CareerAI")

    st.subheader("Your Smart Career Assistant")

    st.write(
        "Get insights into your professional "
        "skills and discover opportunities for improvement."
    )

    st.divider()

    st.subheader("✨ Features")

    st.markdown("""
    📄 Resume Analysis

    📊 Job Matching

    📌 Missing Skills

    🎯 Career Recommendations

    📈 Skill Coverage

    📥 PDF Report
    """)

    st.divider()

    st.caption("AI-Powered Career Guidance")


# ----------------------------------
# MAIN HEADER
# ----------------------------------

st.markdown("""
<div class="main-title">
    <h1>🚀 CareerAI</h1>
    <h3>AI-Powered Resume Analyzer & Career Guidance</h3>
    <p>Discover your strengths. Improve your skills. Build your future.</p>
</div>
""", unsafe_allow_html=True)


# ----------------------------------
# UPLOAD SECTION
# ----------------------------------

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
        height=150,
        placeholder="Paste the job description here..."
    )


st.write("")

analyze_button = st.button(
    "🚀 Analyze My Resume",
    use_container_width=True
)


# ----------------------------------
# RESUME ANALYSIS
# ----------------------------------

if analyze_button:

    if uploaded_file is None:

        st.warning("Please upload your resume PDF.")

    elif not job_description.strip():

        st.warning("Please enter a job description.")

    else:

        try:

            with st.spinner("Analyzing your resume... Please wait."):

                # Extract resume text
                resume_text = extract_resume_text(uploaded_file)

                if not resume_text.strip():

                    st.error("Could not read your resume. Please try another PDF.")

                else:

                    # Extract skills
                    skills = extract_skills(resume_text)

                    # Calculate job match
                    result = calculate_match(
                        resume_text,
                        job_description
                    )

                    # Calculate career recommendations
                    recommendations = recommend_careers(skills)

                    # Safely limit progress percentage
                    match_score = max(
                        0,
                        min(100, float(result["match_score"]))
                    )

                    similarity = max(
                        0,
                        min(100, float(result["similarity"]))
                    )

                    st.success("Resume analyzed successfully!")

                    # ----------------------------------
                    # RESUME ANALYSIS
                    # ----------------------------------

                    st.divider()

                    st.header("📄 Resume Analysis")

                    st.subheader("Skills Found")

                    st.metric(
                        "Total Recognized Skills",
                        len(skills)
                    )

                    if skills:

                        st.write(", ".join(skills))

                    else:

                        st.warning("No known skills detected.")

                    # ----------------------------------
                    # JOB MATCHING RESULTS
                    # ----------------------------------

                    st.divider()

                    st.header("📊 Job Matching Results")

                    col1, col2, col3 = st.columns(3)

                    with col1:

                        st.metric(
                            "Skill Match",
                            f"{match_score:.2f}%"
                        )

                    with col2:

                        st.metric(
                            "Text Similarity",
                            f"{similarity:.2f}%"
                        )

                    with col3:

                        st.metric(
                            "Skills Found",
                            len(skills)
                        )

                    st.write("Overall Skill Match")

                    st.progress(match_score / 100)

                    # ----------------------------------
                    # MATCHED AND MISSING SKILLS
                    # ----------------------------------

                    st.divider()

                    col1, col2 = st.columns(2)

                    with col1:

                        st.subheader("✅ Matched Skills")

                        matched_skills = result.get(
                            "matched_skills", []
                        )

                        if matched_skills:

                            for skill in matched_skills:

                                st.write("🟢", skill)

                        else:

                            st.info("No matching skills found.")

                    with col2:

                        st.subheader("📌 Missing Skills")

                        missing_skills = result.get(
                            "missing_skills", []
                        )

                        if missing_skills:

                            for skill in missing_skills:

                                st.write("🔴", skill)

                        else:

                            st.success("No missing skills detected!")

                    # ----------------------------------
                    # CAREER RECOMMENDATIONS
                    # ----------------------------------

                    st.divider()

                    st.header("🎯 Career Recommendations")

                    if recommendations:

                        for item in recommendations:

                            st.subheader(item["career"])

                            score = max(
                                0,
                                min(100, float(item["score"]))
                            )

                            st.metric(
                                "Skill Coverage",
                                f"{score:.2f}%"
                            )

                            st.progress(score / 100)

                            matched = item.get("matched", [])

                            st.write(
                                "Matching skills:",
                                ", ".join(matched)
                                if matched
                                else "No matching skills"
                            )

                    else:

                        st.info("No career recommendations available.")

                    # ----------------------------------
                    # PDF REPORT DOWNLOAD
                    # ----------------------------------

                    st.divider()

                    st.header("📥 Download Your Report")

                    st.write(
                        "Download your complete resume analysis "
                        "and career recommendations as a PDF."
                    )

                    try:

                        pdf_report = generate_report(
                            skills,
                            result,
                            recommendations
                        )

                        st.download_button(
                            label="📄 Download PDF Report",
                            data=pdf_report,
                            file_name="CareerAI_Analysis_Report.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )

                    except Exception as pdf_error:

                        st.error(
                            f"Could not generate PDF report: {pdf_error}"
                        )

                    st.divider()

                    st.success(
                        "Thank you for using CareerAI! 🚀"
                    )

        except Exception as error:

            st.error(
                f"Something went wrong: {error}"
            )


# ----------------------------------
# FOOTER
# ----------------------------------

st.divider()

st.markdown(
    "<center>🚀 CareerAI | AI-Powered Career Guidance</center>",
    unsafe_allow_html=True
)