from abc import ABC, abstractmethod
class jobs(ABC):
    def print(self, x):
        print(x)
    @abstractmethod
    def task(self):
        print("This is the abstract")
class buisness(jobs):
    def task(self):
        print("This is the buiness method")
obj = buisness()
obj.task()
obj.print(69)
obj1 = jobs()
obj1.task()
obj1.print(": a company owner")
