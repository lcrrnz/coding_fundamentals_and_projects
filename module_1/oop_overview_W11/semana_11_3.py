#Duplique el proyecto [Sistema de Control de Estudiantes] y modifíquelo para usar objetos para guardar la información de los estudiantes (creando una clase de `Student`).
#Hay que cambiar los estudiantes de diccionarios a objetos.
#Hay que convertir la data del csv (que viene por defecto en formato de diccionario) a objetos al importarla.
#Hay que convertir los objetos a diccionarios para poder exportarlos a csv.
#Hay que modificar el acceso a los keys para accesar a atributos.
# student[’Name’] → student.name
import csv

class Student:
    def __init__(self):
        self.name = ""
        self.group = ""
        self.spanish_score = 0.0
        self.english_score = 0.0
        self.socials_score = 0.0
        self.science_score = 0.0

    def student_entry(self):
        self.name = input("Enter student's name: ")
        self.group = input("Enter student's group: ")

        def get_score(subject):
            while True:
                try:
                    score = float(input(f"Enter {subject} score (0-100): "))
                    if 0 <= score <= 100:
                        return score
                    else:
                        print("Invalid score! Must be between 0 and 100.")
                except ValueError:
                    print("Oops! That was not a valid number. Try again.")

        self.spanish_score = get_score("Spanish")
        self.english_score = get_score("English")
        self.socials_score = get_score("Socials")
        self.science_score = get_score("Science")

    def to_dic(self):
        return {
            "name": self.name,
            "group": self.group,
            "spanish score": self.spanish_score,
            "english score": self.english_score,
            "socials score": self.socials_score,
            "science score": self.science_score
        }


class DataProcessor:
    def scores_average(self, students_list):
        try:
            if not students_list:
                print("No student data available. Please enter students first")
                return {}
            print("Calculating scores averages. Please wait...")
            subject_scores = {
                "spanish score": [],
                "english score": [],
                "socials score": [],
                "science score": []
            }
            for student in students_list:
                subject_scores["spanish score"].append(student.spanish_score)
                subject_scores["english score"].append(student.english_score)
                subject_scores["socials score"].append(student.socials_score)
                subject_scores["science score"].append(student.science_score)
            averages = {}
            for subject, scores in subject_scores.items():
                if scores:  
                    averages[subject] = sum(scores) / len(scores)
            print(f'Average scores per subject:\n {averages}')
            return averages
        except Exception as error:
            print(f"Unable to complete due to {error}")
            return {}
    
    def top_three_highest(self, student_list):
        def sort_by_score(student_tuple):
            return student_tuple[1]
        try:
            if not student_list:
                print("No student data available. Please enter students first")
                return {}
            print("Retrieving top 3 students. Please wait...")
            student_scores = []
            for student in student_list:
                name = student.name
                scores = [
                    student.spanish_score,
                    student.english_score,
                    student.socials_score,
                    student.science_score
                ]
                average_score = sum(scores) / len(scores)
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

class CSVHandler:
    def csv_creation(self,file_path,data, keys):
        try:
            if not data:
                print("No student data available. Please enter students first.")
                return
            else:
                print("Exporting data. Please wait...")
                with open (file_path,'w',newline="") as file:
                    writer = csv.DictWriter(file,fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(data)
                print("File succesfully created.")
        except PermissionError as error:
            print(f'Unable to create file due to {error}')
        

    def csv_reader(self,path):
        data_dic=[
        ]
        try:
            with open (path,"r",newline="") as file:
                reader = csv.DictReader(file, delimiter=",")
                data_dic = list(reader)
            print(f"CSV file '{path}' successfully imported!")
        except FileNotFoundError:
            print(f"No previous CSV file found or data could not be imported. '{path}' was not found.")
            return []
        except Exception as error:
            print(f"Something went wrong while importing data: {error}")
            return []
        return data_dic




student1 = Student()
student1.student_entry()    
students = [student1]
processor = DataProcessor()
processor.scores_average(students)     
processor.top_three_highest(students)
handler = CSVHandler()
rows = [stu.to_dic() for stu in students]
keys = ('name','group','spanish score','english score','socials score','science score')
handler.csv_creation ("students.csv", rows, keys)