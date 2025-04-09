def summarize_feedback(feedback_list):
    top_scores = sorted(feedback_list, key=lambda x: x['score'], reverse=True)[:3]
    
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for feedback in feedback_list:
        score = feedback['score']
        if score >= 90:
            grade_counts["A"] += 1
        elif score >= 75:
            grade_counts["B"] += 1
        elif score >= 60:
            grade_counts["C"] += 1
        elif score >= 40:
            grade_counts["D"] += 1
        else:
            grade_counts["F"] += 1
    
    return {"top_scores": top_scores, "grade_counts": grade_counts}
