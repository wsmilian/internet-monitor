import requests
import time
import datetime

CHECK_URL = "https://www.google.com"
LOG_FILE = "internet_log.txt"
CHECK_INTERVAL = 10  # seconds

def log_event(status, msg):
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | {status} | {msg}\n")

def check_connectivity():
    try:
        response = requests.get(CHECK_URL, timeout=5)
        if response.status_code == 200:
            return True, "Online"
        else:
            return False, f"Status code: {response.status_code}"
    except Exception as e:
        return False, str(e)

def main():
    print("Starting internet monitor...")
    while True:
        online, message = check_connectivity()
        status = "UP" if online else "DOWN"
        log_event(status, message)
        print(f"{status}: {message}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
