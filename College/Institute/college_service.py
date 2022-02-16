
from Institute.Faculty import Staff
from Institute.college_info import College_Info
from Institute.Student import Student

class College:
    def __init__(self, cid, cnm, cac):
       self.College_Info = College_Info(cid, cnm, cac)

    def __str__(self):
       return f'''{self.__dict__}'''

    def __repr__(self):
       return str(self)

    def add_Faculty(self,fac:Staff):
        self.College_Info.collgeFacutly.append(fac)
        print(f" faculty {fac} added")

    def show_all(self):
        print( self.College_Info.collgeFacutly)