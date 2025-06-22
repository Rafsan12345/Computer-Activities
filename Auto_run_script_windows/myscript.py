from datetime import datetime
import os

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

# Absolute path দিন, যেন যে directory থেকেই চালানো হোক না কেন কাজ করে
log_file = r"C:\Users\DCL\startup_log.txt"

# ডিরেক্টরি এক্সিস্ট করে কি না চেক করুন
os.makedirs(os.path.dirname(log_file), exist_ok=True)

try:
    with open(log_file, "a") as file:
        file.write(f"System started at: {timestamp}\n")
except Exception as e:
    with open(r"C:\Users\DCL\error_log.txt", "a") as f:
        f.write(str(e) + "\n")
