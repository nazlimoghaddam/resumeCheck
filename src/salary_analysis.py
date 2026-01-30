def salary_by_industry(df):
    return df.groupby("industry")["salary"].mean().sort_values(ascending=False)

def salary_by_location(df):
    return df.groupby("location")["salary"].mean().sort_values(ascending=False)
