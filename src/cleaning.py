import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("Initial Data:\n", df.head())
    return df

def handle_missing_values(df):
    df['age'] = df['age'].fillna(df['age'].median())
    df['income'] = df['income'].fillna(df['income'].median())
    return df

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df

def handle_outliers(df):
    # Remove extreme income values using IQR
    Q1 = df['income'].quantile(0.25)
    Q3 = df['income'].quantile(0.75)
    IQR = Q3 - Q1

    df = df[(df['income'] >= Q1 - 1.5 * IQR) & (df['income'] <= Q3 + 1.5 * IQR)]
    return df

def clean_data(path):
    df = load_data(path)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = handle_outliers(df)

    print("\nCleaned Data:\n", df.head())
    return df

if __name__ == "__main__":
    df = clean_data("D:/Internship/Thiranex_DataSceince/data/raw_data.csv")
    df.to_csv("D:/Internship/Thiranex_DataSceince/data/cleaned_data.csv", index=False)
