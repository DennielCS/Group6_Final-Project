# feedback_handler.py
# Handles feedback operations and file management for RainCheck

import os
from datetime import datetime

FEEDBACK_FILE = "feedback.txt"

# Load feedback from file
def load_feedback():
    feedback_list = []
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    entry_id, subject, topic, rating, comment, session_date = line.split("|")
                    feedback_list.append({
                        "entry_id": int(entry_id),
                        "subject": subject,
                        "topic": topic,
                        "rating": int(rating),
                        "comment": comment,
                        "session_date": session_date
                    })
    return feedback_list

# Save feedback to file
def save_feedback(feedback_list):
    with open(FEEDBACK_FILE, "w") as f:
        for entry in feedback_list:
            f.write(f"{entry['entry_id']}|{entry['subject']}|{entry['topic']}|{entry['rating']}|{entry['comment']}|{entry['session_date']}\n")

# Add new feedback entry
def add_feedback(feedback_list):
    print("\n--- Add Feedback ---")
    subject = input("Enter subject: ").strip()
    topic = input("Enter lecture/topic: ").strip()
    while True:
        try:
            rating = int(input("Enter rating (1-5): ").strip())
            if 1 <= rating <= 5:
                break
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 5.")
    comment = input("Enter comment (optional): ").strip()
    session_date = datetime.now().strftime("%Y-%m-%d")
    entry_id = feedback_list[-1]["entry_id"] + 1 if feedback_list else 1
    feedback_list.append({
        "entry_id": entry_id,
        "subject": subject,
        "topic": topic,
        "rating": rating,
        "comment": comment,
        "session_date": session_date
    })
    save_feedback(feedback_list)
    print("Feedback added successfully!\n")

# View all feedback entries
def view_feedback(feedback_list):
    if not feedback_list:
        print("\nNo feedback entries yet.\n")
        return
    print("\n--- All Feedback ---")
    for entry in feedback_list:
        print(f"ID: {entry['entry_id']} | Subject: {entry['subject']} | Topic: {entry['topic']} | Rating: {entry['rating']} | Comment: {entry['comment']} | Date: {entry['session_date']}")
    print()

# View average ratings per subject
def average_ratings(feedback_list):
    if not feedback_list:
        print("\nNo feedback entries yet.\n")
        return
    averages = {}
    counts = {}
    for entry in feedback_list:
        subj = entry["subject"]
        averages[subj] = averages.get(subj, 0) + entry["rating"]
        counts[subj] = counts.get(subj, 0) + 1
    print("\n--- Average Ratings per Subject ---")
    for subj in averages:
        avg = averages[subj] / counts[subj]
        print(f"{subj}: {avg:.2f}")
    print()

# Search feedback by topic or date
def search_feedback(feedback_list):
    if not feedback_list:
        print("\nNo feedback entries yet.\n")
        return
    choice = input("Search by (1) Topic or (2) Date? Enter 1 or 2: ").strip()
    if choice == "1":
        topic_search = input("Enter topic keyword: ").strip().lower()
        results = [e for e in feedback_list if topic_search in e["topic"].lower()]
    elif choice == "2":
        date_search = input("Enter date (YYYY-MM-DD): ").strip()
        results = [e for e in feedback_list if e["session_date"] == date_search]
    else:
        print("Invalid choice.\n")
        return
    if not results:
        print("No matching feedback found.\n")
        return
    print("\n--- Search Results ---")
    for entry in results:
        print(f"ID: {entry['entry_id']} | Subject: {entry['subject']} | Topic: {entry['topic']} | Rating: {entry['rating']} | Comment: {entry['comment']} | Date: {entry['session_date']}")
    print()
