from load_data import load_data
from utils import format_time
from qualifying import get_best_laps, driver_exists, get_session_best



def main():

    df = load_data("data/session_laptimes.json")
    # print(f"Rows: {len(df)}")
    # print(f"Drivers: {sorted(df['drv'].unique())}")
    # print(f"Sessions: {sorted(df['qs'].unique())}")

    driver = input("Driver code: ").strip().upper()

    if not driver_exists(df, driver):
        print("Driver not found.")
        return
    
    print(f"\nDriver: {driver}")
    results = get_best_laps(df, driver)

    print("\nBest Qualifying Laps:")
    for session, lap in results.items():
        print(f"{session}: {format_time(lap)}")

    print("\nSession Best Laps:")
    print(get_session_best(df, "Q1").sort_values("time")
          
)


if __name__ == "__main__":
    main()
