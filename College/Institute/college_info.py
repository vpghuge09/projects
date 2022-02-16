from Institute.Faculty import Staff

class College_Info:

    def __init__(self,cid,cnam,cacc):       #[product1,product2...]
        self.collgeId = cid
        self.collegeName = cnam
        self.collgeFacutly = []              #list of products
        self.collgeAccount = cacc

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

