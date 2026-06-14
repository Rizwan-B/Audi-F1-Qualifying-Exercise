import pandas as pd

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
