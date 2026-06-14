from load_data import load_data
from utils import format_time
from qualifying import get_best_laps, driver_exists



def main():

    df = load_data("data/session_laptimes.json")
    print(f"Rows: {len(df)}")
    print(f"Drivers: {sorted(df['drv'].unique())}")
    print(f"Sessions: {sorted(df['qs'].unique())}")



    driver = input("Driver code: ").strip().upper()

    if not driver_exists(df, driver):
        print("Driver not found.")
        return

    results = get_best_laps(df, driver)

    
    print(f"\nDriver: {driver}")
    print(f"Best laps: {results}")

    
    for session, lap in results.items():
        print(f"{session}: {format_time(lap)}")


if __name__ == "__main__":
    main()
