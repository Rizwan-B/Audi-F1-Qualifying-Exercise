import pandas as pd


def main():
    
    df = pd.read_json("data/session_laptimes.json")

    print(df.head())
    print()
    print(df.columns.tolist())


if __name__ == "__main__":
    main()
