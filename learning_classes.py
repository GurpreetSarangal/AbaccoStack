from curses.ascii import isalpha, isdigit


class person:
    
    def __init__(self,name, age):
        self.name = name
        self.age = age
        pass

    def birthday(self):
        self.age = self.age + 1

    def __str__(self):
        return self.name


class teacher(person):
    def __init__(self, name, age, experties):
        person.__init__(self, name, age)
        self.experties = experties


# test_teacher = teacher("test_teacher", 80, "python")
# print(test_teacher.name)
# print(test_teacher.age)
# print(test_teacher.experties)

# per1 = person("Parneet", 100)
# per2 = person("Gurpreet", 90)
# print(per1.name)
# print(per1.age)

# print(per2)
# move = ""

# if len(move) < 2 or len(move) >2 or not isalpha(move[1]) or not isdigit(move[0]):
#     print("please input a valid move")
# else:
#     print("valid")