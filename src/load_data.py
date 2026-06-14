from pathlib import Path
import pandas as pd


def load_data(filepath):
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    try:
        df = pd.read_json(path)
    except ValueError as exc:
        raise ValueError("Invalid JSON file") from exc

    return df