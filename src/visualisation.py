import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure output folder exists
os.makedirs("output/plots", exist_ok=True)

def load_data():
    return pd.read_csv("D:/Internship/Thiranex_DataSceince/data/cleaned_data.csv")

def plot_income_distribution(df):
    plt.figure()
    sns.histplot(df['income'], kde=True)
    plt.title("Income Distribution")
    plt.xlabel("Income")
    plt.ylabel("Frequency")
    plt.savefig("output/plots/income_distribution.png")
    plt.close()

def plot_gender_purchases(df):
    plt.figure()
    sns.barplot(x='gender', y='purchases', data=df)
    plt.title("Purchases by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Purchases")
    plt.savefig("output/plots/gender_purchases.png")
    plt.close()

def plot_age_vs_income(df):
    plt.figure()
    sns.scatterplot(x='age', y='income', data=df)
    plt.title("Age vs Income")
    plt.xlabel("Age")
    plt.ylabel("Income")
    plt.savefig("output/plots/age_vs_income.png")
    plt.close()

def main():
    df = load_data()

    plot_income_distribution(df)
    plot_gender_purchases(df)
    plot_age_vs_income(df)

    print("✅ All plots saved in output/plots/")

if __name__ == "__main__":
    main()
