import pandas as pd

# Checks if a driver exists in the dataframe.
def driver_exists(df: pd.DataFrame, driver):
    return driver.upper() in df["drv"].unique()


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

# Returns the best lap for each driver in a given session.
def get_session_best(df, session):

    session_df = df[df["qs"] == session].copy()

    session_df["time"] = pd.to_numeric(session_df["time"], errors="coerce")

    return (session_df.groupby("drv", as_index=False)["time"].min())


def get_quali_position(df):

    q1 = get_session_best(df, "Q1")
    q2 = get_session_best(df, "Q2")
    q3 = get_session_best(df, "Q3")

    q1_drivers = set(q1["drv"])
    q2_drivers = set(q2["drv"])
    q3_drivers = set(q3["drv"])

    # The top 10 
    q3_sorted = q3.sort_values("time")

    # Drivers eliminated in Q2
    q2_eliminated = q2[q2["drv"].isin(q2_drivers - q3_drivers)].sort_values("time")

    # Drivers eliminated in Q1
    q1_eliminated = q1[q1["drv"].isin(q1_drivers - q2_drivers)].sort_values("time")

    results = {}
    position = 1

    for _, row in q3_sorted.iterrows():
        results[row["drv"]] = position
        position += 1

    for _, row in q2_eliminated.iterrows():
        results[row["drv"]] = position
        position += 1

    for _, row in q1_eliminated.iterrows():
        results[row["drv"]] = position
        position += 1

    return results