feedback={
    "positie":45,
    "Neutral":18,
    "Negative":7
    }
total_feedback=sum(feedback.values())
print("Total Feedback",total_feedback)

highest_feedback=max(feedback,key=feedback.get)
print("Highest Feedback Type",highest_feedback)
                   
