 class Cicle:

     def __init__(self,r):
         self.r = r

     def area_maker(self):
         area = self.r*self.r*3.14
         print(f"S ={area}")

     def perimetr_maker(self):
         perimetr = 2*self.r*3.14
         print(perimetr)

 area_1 = Cicle(5)
 area_1.area_maker()
 area_1.perimetr_maker()

class Human:
    def __init__(self, name , surname, age, weight, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight
    def check_1(self):
        print("You will be 100 before" , 100-self.age+2022 , "ages ")

    def check_2(self):
        print("Your optimal weight is ",50 + (0.91 * self.height-152.4))

    def check_3(self):
        print(f"Greetings to you {self.surname} {self.name}")

human_1 = Human("Hakob", "Sargsyan" , 19, 56, 180)
human_1.check_1()
human_1.check_2()
human_1.check_3()