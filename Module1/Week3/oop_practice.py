#2a
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,yob):
        self.name = name 
        self.yob = yob 
    
    @abstractmethod
    def describe(self):
        return f"Person - Name: {self.name} - YoB: {self.yob}"

class Student(Person):
    def __init__(self,name,yob,grade):
        super().__init__(name,yob)
        self.grade = grade
    
    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")

class Doctor(Person):
    def __init__(self,name,yob,specialist):
        super().__init__(name,yob)
        self.specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Speacialist: {self.specialist}")

class Teacher(Person):
    def __init__(self,name,yob,subject):
        super().__init__(name,yob)
        self.subject = subject 
    
    def describe(self):
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")

#2b
class Ward:
    def __init__(self,name):
        self.name = name 
        self.w_list = []
    
    def add_person(self,person):
        self.w_list.append(person)
    
    def describe(self):
        print(f"Ward Name: {self.name}")
        if self.w_list == []: 
            return 
        for i in self.w_list:
            i.describe()
    
    #2c 
    def count_doctor(self):
        result = 0
        for i in self.w_list:
            if type(i).__name__ == 'Doctor':
                result += 1
        return result 

    #2d 
    def sort_age(self):
        self.w_list.sort(key=lambda x: x.yob, reverse=True)
    
    #2e 
    def compute_average(self):
        teachers_yob = [i.yob for i in self.w_list if type(i).__name__ == 'Teacher']
        return sum(teachers_yob)/len(teachers_yob)