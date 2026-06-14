import pandas as pd
from load_data import load_data
from utils import format_time

# Returns the best lap for a driver in Q1, Q2 and Q3.
def get_best_laps(df, driver):
    
    driver = driver.upper() # Converts all iuputs to uppercase to match the driver codes in the dataframe.
    driver_df = df[df["drv"] == driver].copy()

    results = {}

    for session in ["Q1", "Q2", "Q3"]:

        session_df = driver_df[driver_df["qs"] == session].copy()

        # Converts to numeric values, errors become NaN.
        session_df["time"] = pd.to_numeric( session_df["time"], errors="coerce") 
        best_time = session_df["time"].min()

        
        if pd.isna(best_time):
            results[session] = None
        else:
            results[session] = float(best_time)

    return results


def main():

    df = load_data("data/session_laptimes.json")
    print(f"Rows: {len(df)}")
    print(f"Drivers: {sorted(df['drv'].unique())}")
    print(f"Sessions: {sorted(df['qs'].unique())}")



    driver = input("Driver code: ").strip().upper()

    results = get_best_laps(df, driver)

    
    print(f"\nDriver: {driver}")
    print(f"Best laps: {results}")

    
    for session, lap in results.items():
        print(f"{session}: {format_time(lap)}")


if __name__ == "__main__":
    main()
