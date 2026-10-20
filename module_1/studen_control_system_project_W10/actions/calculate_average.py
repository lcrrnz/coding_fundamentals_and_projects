def scores_average(students_info):
    try:
        if not students_info:
            print("No student data available. Please enter students first")
            return {}
        print("Calculating scores averages. Please wait...")
        subject_scores = {
            "spanish score": [],
            "english score": [],
            "socials score": [],
            "science score": []
        }
        for student in students_info:
            for key, value in student.items():
                if key in subject_scores:  
                    subject_scores[key].append(int(value))  
        averages = {}
        for subject, scores in subject_scores.items():
            if scores:  
                averages[subject] = sum(scores) / len(scores)
        print(f'Average scores per subject:\n {averages}')
        return averages
    except Exception as error:
        print(f"Unable to complete due to {error}")
        return {}
