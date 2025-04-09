from feedback.entry import collect_feedback

def test_collect_feedback():
    result = collect_feedback("Alice", 85, "Good class!")
    assert result["name"] == "Alice"
    assert result["score"] == 85
    assert result["comment"] == "Good class!"
