from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from skill_extractor import extract_skills


def calculate_match(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = [
        skill for skill in job_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    if job_skills:
        match_score = (
            len(matched_skills) / len(job_skills)
        ) * 100
    else:
        match_score = 0

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        matrix[0:1], matrix[1:2]
    )[0][0] * 100

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": round(match_score, 2),
        "similarity": round(similarity, 2)
    }