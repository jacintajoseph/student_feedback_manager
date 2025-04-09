# main.py

from feedback.entry import collect_feedback
from feedback.score_calc import calculate_average
from feedback.summary import summarize_feedback

def main():
    feedback_list = []
    while True:
        student_name = input("Enter student name (or type 'done' to finish): ")
        if student_name.lower() == 'done':
            break
        try:
            score = float(input("Enter feedback score (0-10): "))
        except ValueError:
            print("Invalid score! Please enter a number.")
            continue
        feedback = collect_feedback(student_name, score)
        feedback_list.append(feedback)

    print("\n📋 Feedback Summary:")
    print(summarize_feedback(feedback_list))
    print(f"\n⭐ Average Score: {calculate_average(feedback_list):.2f}")

if __name__ == "__main__":
    main()
