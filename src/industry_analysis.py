def jobs_per_industry(df):
    return df["industry"].value_counts()

def top_companies(df, n=5):
    return df["company"].value_counts().head(n)
