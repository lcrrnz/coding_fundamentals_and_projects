def sort_by_score(student):
    return student[1]

def top_three_highest(students_info):
    try:
        if not students_info:
            print("No student data available. Please enter students first")
            return {}
        print("Retrieving top 3 students. Please wait...")
        student_scores = []
        for student in students_info:
            name = student.get("name", "Unknown")  
            scores = [int (value) for key, value in student.items() if key.endswith("score")]  
            if scores:
                average_score = sum(scores) / len(scores)
            else:
                average_score = 0 
            student_scores.append((name, average_score))  
        student_scores.sort(key=sort_by_score, reverse=True)
        top_students = student_scores[:3]  
        print("\nTop Performing Students:")
        for name, score in top_students:
            print(f"{name}: {score:.2f}")
    except Exception as error:
        print(f"Unable to complete due to {error}")
        return {}
    return dict(top_students)