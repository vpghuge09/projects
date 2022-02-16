class Student():
    def __init__(self,sid,snm):
        self.stud_Id=sid
        self.stud_name=snm

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)