from Institute.Faculty import Staff
from Institute.college_info import College_Info

from Institute.college_service import College

service=College(1,2,3)

service.add_Faculty(Staff(1,"adi"))
service.add_Faculty(Staff(2,"jite"))


service.show_all()
