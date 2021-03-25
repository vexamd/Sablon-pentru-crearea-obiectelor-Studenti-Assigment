class person:
    name = ""
    address = ""
    phone = ""
    index_number = ""
class student (person):
    course = ""
    def __init__(self, name, address, phone, course, index_number,):
        self.course = course
        self.name=name
        self.address=address
        self.phone=phone
        self.index_number=index_number
        
    def getinfo(self):
        print("Student: ", self.name, "Address: ", self.address, "Phone: ", self.phone, "Course: ", self.course, "Index Number: ", self.index_number)
        
st1=student("Adrian Josu", "Chisinau", "37378425874", "Python Developer", "MD-7715")
st1.getinfo()
st2=student("Beatrice Delia", "Iasi", "4068754675", "Python Developer", "7654")
st2.getinfo()
st3=student("Botezat Maria", "Chisinau", "37368257924", "Back-End Developer", "MD-2062")
st3.getinfo()
        
