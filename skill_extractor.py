import re

SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "HTML",
    "CSS",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Scikit-learn",
    "Flask",
    "Django",
    "React",
    "Node.js",
    "Git",
    "GitHub",
    "MongoDB",
    "MySQL",
    "Communication",
    "Problem Solving"
]

def extract_skills(text):

    found_skills = []

    for skill in SKILLS:

        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills