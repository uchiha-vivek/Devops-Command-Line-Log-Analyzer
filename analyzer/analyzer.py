import re
from datetime import datetime
from collections import Counter

LOG_PATTERN = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (INFO|WARNING|ERROR) (.*)")

class LogAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.logs = []
        self.load_logs()

    def load_logs(self):
        with open(self.filepath, "r") as file:
            for line in file:
                match = LOG_PATTERN.match(line)
                if match:
                    timestamp, level, message = match.groups()
                    self.logs.append({
                        "timestamp": datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                        "level": level,
                        "message": message.strip()
                    })

    def filter_by_level(self, level):
        return [log for log in self.logs if log["level"] == level.upper()]

    def filter_by_time_range(self, start_time, end_time):
        return [log for log in self.logs if start_time <= log["timestamp"] <= end_time]

    def summary(self):
        levels = Counter(log["level"] for log in self.logs)
        print("\nLog Summary:")
        for level, count in levels.items():
            print(f"  {level}: {count}")

        print("\nTop 3 Errors:")
        errors = [log["message"] for log in self.logs if log["level"] == "ERROR"]
        for msg, count in Counter(errors).most_common(3):
            print(f"  {msg} ({count} times)")
