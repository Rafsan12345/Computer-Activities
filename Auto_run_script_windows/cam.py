#!/usr/bin/env python3
# take_photo_on_start.py
# লেখক: আপনিเอง
# কাজ: সিস্টেম স্টার্ট হলে চালালে ওয়েবক্যাম থেকে একটি ছবি তুলে সেভ করবে

import cv2
import os
from datetime import datetime
import sys
import time

# ছবি সেভ করার ফোল্ডার (আপনি চাইলে পরিবর্তন করবেন)
SAVE_DIR = os.path.expanduser(r"~\Pictures\StartupPhotos")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def take_photo_and_save(save_dir):
    ensure_dir(save_dir)
    # ক্যামেরা ইনডেক্স 0 (সাধারণত বিল্ট-ইন/ডিফল্ট ওয়েবক্যাম)
    cam_index = 0
    cap = cv2.VideoCapture(cam_index, cv2.CAP_DSHOW)  # Windows-এ ভাল কাজ করে
    if not cap.isOpened():
        # কিছু ডেলেই পুনরায় চেক করা যেতে পারে
        print("Error: ক্যামেরা খোলা গেল না।")
        return False

    # ক্যামেরা ঝামেলা কমাতে সামান্য অপেক্ষা
    time.sleep(0.5)
    ret, frame = cap.read()
    cap.release()
    if not ret or frame is None:
        print("Error: ক্যামেরা থেকে ছবি নেওয়া গেল না।")
        return False

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"photo_{timestamp}.jpg"
    filepath = os.path.join(save_dir, filename)
    # JPEG মান ধরে রাখবে
    cv2.imwrite(filepath, frame)
    print(f"Saved photo: {filepath}")
    return True

def main():
    # যদি কোনো আর্গুমেন্ট দিয়ে আলাদা ফোল্ডার চাইলে নেওয়া যাবে
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = SAVE_DIR

    success = take_photo_and_save(folder)
    if not success:
        # লগিং বা রি-ট্রাই লজিক রাখতে চাইলে এখানে বাড়াবে
        pass

if __name__ == "__main__":
    main()
