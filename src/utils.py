def format_time(seconds: float | None) -> str:
    if seconds is None:
        return "N/A"

    minutes = int(seconds // 60)
    remainder = seconds % 60

    return f"{minutes}:{remainder:06.3f}"