class Student: 
    def __init__(self, rollNo, name): 
        self.rollNo = rollNo 
        self.name = name 
    def display(self): 
        print(f'Student Roll No: {self.rollNo}') 
        print(f'Student Name: {self.name}') 
class Exam(Student): 
    def __init__(self, rollNo, name, subject): 
        super().__init__(rollNo, name) 
        self.subject = subject 
    def display(self): 
        super().display() 
        for i in range(len(self.subject)):
            print(f'Subject {i + 1} Marks: {self.subject[i]}') 
class Result(Exam): 
    total_marks = 0
    def __init__(self, rollNo, name, subject): 
        super().__init__(rollNo, name, subject) 
        self.total_marks = sum(subject) 
    def display(self): 
        super().display() 
        print(f'Total Marks: {self.total_marks}')

if __name__ == '__main__':
    student = Student(1, 'preet')
    student.display()
    print()
    exam = Exam(2, 'meet', [10, 20, 30])
    exam.display()
    print()
    result = Result(3, 'jeet', [30, 15, 17])
    result.display()
    print()
