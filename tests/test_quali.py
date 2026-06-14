import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from qualifying import driver_exists, get_best_laps

def test_driver_exists():
    df = pd.DataFrame({"drv": ["HAM", "VER"]})

    assert driver_exists(df, "HAM")
    assert not driver_exists(df, "XYZ")

def test_best_laps():
    df = pd.DataFrame({
        "drv": ["HAM", "HAM", "HAM"],
        "qs": ["Q1", "Q1", "Q2"],
        "time": [81.2, 80.5, 79.8]
    })

    laps = get_best_laps(df, "HAM")

    assert laps["Q1"] == 80.5
    assert laps["Q2"] == 79.8
    assert laps["Q3"] is None