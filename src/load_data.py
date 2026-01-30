import pandas as pd
#droping the columns where the description is empty

def load_jobs(file_path):
    df = pd.read_csv(file_path)
    df.dropna(subset=["description"], inplace=True)
    return df