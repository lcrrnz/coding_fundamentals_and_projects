def students_entry ():
    counter = 1
    student_amount = int(input("How many entries are we expecting? "))
    student_info_list = []
    while True:
        while  counter <= student_amount:
            student_entry_dictionary = {}
            print(f'Enter information for student #{counter}')
            student_entry_dictionary ["name"] = input("Enter student's name: ")
            student_entry_dictionary ["class"] = input("Enter student's class: ")
            while True:
                try:
                    spanish_score = int(input("Enter student's spanish score: "))
                    if spanish_score > 100 or spanish_score < 0:
                        print ("Scores are only allow from 0 to 100")
                    else:
                        student_entry_dictionary ["spanish score"] = spanish_score
                        break
                except ValueError as error:
                    print(f'Oops! that was not a valid number. Try again')
            while True:
                try:
                    english_score = int(input("Enter student's english score: "))
                    if english_score > 100 or english_score < 0:
                        print ("Scores are only allow from 0 to 100")
                    else:
                        student_entry_dictionary ["english score"] = english_score
                        break
                except ValueError as error:
                    print(f'Oops! that was not a valid number. Try again')
            while True:
                try:
                    socials_score = int(input("Enter student's socials score: "))
                    if socials_score > 100 or socials_score < 0:
                        print ("Scores are only allow from 0 to 100")
                    else:
                        student_entry_dictionary ["socials score"] = socials_score
                        break
                except ValueError as error:
                    print(f'Oops! that was not a valid number. Try again')
            while True:
                try:
                    science_score = int(input("Enter student's science score: "))
                    if science_score > 100 or science_score < 0:
                        print ("Scores are only allow from 0 to 100")
                    else:
                        student_entry_dictionary ["science score"] = science_score
                        break
                except ValueError as error:
                    print(f'Oops! that was not a valid number. Try again')
            counter += 1
            student_info_list.append(student_entry_dictionary)
        break
    return student_info_list