from collections import Counter
import re

common_skills = [
    "python", "sql", "excel", "machine learning", "django",
    "api", "data analysis", "AWS", "Javascript"
]

def extract_skills(descriptions):
    skill_counts = Counter()

    for desc in descriptions:
        text = desc.lower()
        for skill in common_skills:
            if re.search(rf"\b{skill}\b", text):
                skill_counts[skill] +=1
    return skill_counts