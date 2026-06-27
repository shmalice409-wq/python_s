class Student:  # python 用大写
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


stu1 = Student("zxc", 44)
print(stu1.name, stu1.age)
stu2 = Student("zxy", 22)

print(f"stu1:{stu1}")
print(f"stu2:{stu2}")

# 添加属性

stu1.name = "zyy"
stu1.age = 12

print(stu1.name, stu1.age)
print(stu2.name, stu2.age)
