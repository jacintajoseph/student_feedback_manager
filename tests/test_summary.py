from feedback.summary import summarize_feedback

def test_summarize_feedback():
    feedback_data = [
        {"name": "Alice", "score": 95, "comment": "Great"},
        {"name": "Bob", "score": 82, "comment": "Good"},
        {"name": "Carol", "score": 68, "comment": "Okay"},
        {"name": "Dave", "score": 45, "comment": "Needs improvement"},
        {"name": "Eve", "score": 30, "comment": "Poor"}
    ]

    result = summarize_feedback(feedback_data)
    
    assert len(result["top_scores"]) == 3
    assert result["grade_counts"]["A"] == 1
    assert result["grade_counts"]["B"] == 1
    assert result["grade_counts"]["C"] == 1
    assert result["grade_counts"]["D"] == 1
    assert result["grade_counts"]["F"] == 1
