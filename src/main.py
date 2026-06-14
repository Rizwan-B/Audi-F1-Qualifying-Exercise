from load_data import load_data
from utils import format_time
from qualifying import get_best_laps, driver_exists, get_quali_position



def main():

    df = load_data("data/session_laptimes.json")

    driver = input("Driver code: ").strip().upper()

    if not driver_exists(df, driver):
            print(
                f"Driver '{driver}' not found.\n"
                f"Available drivers: "
                f"{', '.join(sorted(df['drv'].unique()))}"
            )
            return
    
    results = get_best_laps(df, driver)
    position = get_quali_position(df, driver)


    print(f"\nDriver: {driver}")    

    print("\nBest Qualifying Laps:")
    for session, lap in results.items():
        print(f"{session}: {format_time(lap)}")


    print(f"\nFinal Qualifying Position: P{position}")

if __name__ == "__main__":
    main()
