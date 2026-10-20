import sys
sys.path.append("C:/Users/Coqui/Documents/Curso Python/lifter/my_first_repository/Semana_10_project")  

from my_first_repository.module_1.studen_control_system_project_W10.actions.enter_student_info import students_entry
from my_first_repository.module_1.studen_control_system_project_W10.actions.view_student_info import view_info_storaged
from my_first_repository.module_1.studen_control_system_project_W10.actions.calculate_average import scores_average
from my_first_repository.module_1.studen_control_system_project_W10.actions.top_scores import top_three_highest
from my_first_repository.module_1.studen_control_system_project_W10.data.export_score_csv import csv_file_creation
from my_first_repository.module_1.studen_control_system_project_W10.data.import_score_csv import find_and_read_file

def data_base_menu():
    print("Welcome to the student's database")
    print("Select a menu option to start")
    student_data = None
    file_path = ("students_score.csv")
    while True:
        try:
            select_option = int(input("\nSelect a menu option to start \n 1.Enter students info \n 2.View data stored \n 3.Students average scores \n 4.View Top3 Highest Scorecard  \n 5.Export data to CSV \n 6.Import data from CSV \n 7.Close program \n"))
            if select_option == 1:
                new_entries= students_entry()
                if student_data is None:
                    student_data = new_entries
                else:
                    student_data.extend(new_entries)
            elif select_option == 2:
                view_info_storaged(student_data) 
            elif select_option == 3:
                scores_average(student_data)
            elif select_option == 4:
                if student_data is None:
                    print("No student data available. Please enter students first.")
                else:
                    top_three_highest(student_data)
            elif select_option == 5:
                keys = ('name','class','spanish score','english score','socials score','science score')
                csv_file_creation(file_path,student_data,keys)
            elif select_option == 6:
                student_data = find_and_read_file(file_path)
            elif select_option == 7:
                print("Closing program. Thanks for using!")
                break
            else:
                print("Invalid option. Please select a valid menu number.")  
        except ValueError:
            print("Oops! That was not a valid number. Try again.") 