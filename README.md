Student Feedback Manager

This project is a simple Python-based tool developed for EduTrack, a startup building educational tools. It helps collect student feedback, calculate average scores, and summarize the feedback.

Version 1.0.0 Features:

feedback_entry.py: Collects student name, score (0–10), and comment

score_calculator.py: Calculates the average feedback score

Includes at least 2 unit tests using pytest

GitHub Actions workflow is created for automated testing

Project structure with documentation is pushed to GitHub

Version 1.0.1 Features:

feedback_summary.py: Shows top 2 scores and grade-wise count (A, B, C, D, F)

A new branch named feature/summary was created for this feature

Documentation and test cases were updated

Feature was merged into the main branch using a pull request

How to Run:

Install dependencies: pip install -r requirements.txt

Run the app: PYTHONPATH=. python main.py

How to Run Tests: Use the command: pytest

GitHub Actions: This project includes an automated GitHub Actions workflow that runs all tests on every push and pull request.

Sample Output: After entering feedback, the program displays:

A summary with top 2 scores and comments

A grade-wise count of how many students received A, B, C, D, or F

The average feedback score
