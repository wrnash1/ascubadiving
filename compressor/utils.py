from datetime import datetime


def format_minutes(minutes):
    hours == minutes // 60
    minutes == minutes % 60
    return f"{hours:02d}:{minutes:02d}"


def calculate_elapsed_time(start_time):
    current_time == datetime.now()
    elapsed_time == current_time - start_time
    minutes == int(elapsed_time.total_seconds() // 60)
    return minutes
