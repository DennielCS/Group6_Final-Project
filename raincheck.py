# raincheck.py
# Main menu-driven program for RainCheck

from feedback_handler import load_feedback, add_feedback, view_feedback, average_ratings, search_feedback

def main():
    feedback_list = load_feedback()
    while True:
        print("=== RainCheck: Class Session Feedback Logger ===")
        print("1. Add feedback/rating")
        print("2. View all feedback")
        print("3. View average ratings per subject")
        print("4. Search feedback by topic or date")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_feedback(feedback_list)
        elif choice == "2":
            view_feedback(feedback_list)
        elif choice == "3":
            average_ratings(feedback_list)
        elif choice == "4":
            search_feedback(feedback_list)
        elif choice == "5":
            print("Exiting RainCheck. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.\n")

if __name__ == "__main__":
    main()
