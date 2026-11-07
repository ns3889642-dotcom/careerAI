def recommend_careers(skills):

    careers = {
        "Python Developer": [
            "Python", "Git", "SQL"
        ],

        "Data Analyst": [
            "Python", "Pandas", "NumPy",
            "SQL", "Matplotlib"
        ],

        "Machine Learning Engineer": [
            "Python", "Machine Learning",
            "Scikit-learn", "NumPy", "Pandas"
        ],

        "Frontend Developer": [
            "HTML", "CSS", "JavaScript", "React"
        ],

        "Java Developer": [
            "Java", "SQL", "Git"
        ]
    }

    recommendations = []

    for career, required_skills in careers.items():

        matched = [
            skill for skill in required_skills
            if skill in skills
        ]

        score = (
            len(matched) / len(required_skills)
        ) * 100

        recommendations.append({
            "career": career,
            "score": round(score, 2),
            "matched": matched
        })

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations