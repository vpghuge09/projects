class Staff():
    def __init__(self,sid,snm):
        self.staff_id=sid
        self.staff_name=snm

    def __str__(self):
        return f"{self.__dict__}"
    def __repr__(self):
        return str(self)



st=Staff(1,"vijay")





