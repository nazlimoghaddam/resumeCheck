from load_data import load_jobs
from skills_analysis import extract_skills
from salary_analysis import salary_by_industry
from industry_analysis import jobs_per_industry

def main():
    df = load_jobs("data/jobs.csv")

    skills = extract_skills(df["description"])
    print("\nTop In-Demand Skills:")
    for skill, count in skills.most_common(10):
        print(f"{skill}: {count}")

    print("\nAverage Salary by Industry:")
    print(salary_by_industry(df))

    print("\nJobs per Industry:")
    print(jobs_per_industry(df))

if __name__ == "__main__":
    main()
