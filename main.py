import argparse
from datetime import datetime
from analyzer.analyzer import LogAnalyzer

def main():
    parser = argparse.ArgumentParser(description="Simple Log Analyzer Command Line Tool")
    parser.add_argument("--file", required=True, help="Path to the log file")
    parser.add_argument("--level", choices=["INFO", "WARNING", "ERROR"], help="Filter logs by level")
    parser.add_argument("--start", help="Start time (YYYY-MM-DD HH:MM:SS)")
    parser.add_argument("--end", help="End time (YYYY-MM-DD HH:MM:SS)")
    parser.add_argument("--summary", action="store_true", help="Show summary report")

    args = parser.parse_args()

    analyzer = LogAnalyzer(args.file)

    if args.level:
        logs = analyzer.filter_by_level(args.level)
        print(f"\nLogs with level {args.level}:")
        for log in logs:
            print(f"{log['timestamp']} {log['level']} {log['message']}")

    if args.start and args.end:
        start = datetime.strptime(args.start, "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime(args.end, "%Y-%m-%d %H:%M:%S")
        logs = analyzer.filter_by_time_range(start, end)
        print(f"\nLogs from {args.start} to {args.end}:")
        for log in logs:
            print(f"{log['timestamp']} {log['level']} {log['message']}")

    if args.summary:
        analyzer.summary()

if __name__ == "__main__":
    main()
