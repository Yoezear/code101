class Person:
  def __init__(self, name, age, cid):
    self.name = name
    self.age = age
    self.cid = cid

  def walk(self):
    print(f"{self.name} is walking.")

  def talk(self):
    print(f"{self.name} is talking.")

  def eat(self):
    print(f"{self.name} is eating.")

  def sleep(self):
    print(f"{self.name} is sleeping.")


class Student(Person):
  def __init__(self, name, age, cid, grade):
    super().__init__(name, age, cid)
    self.grade = grade

class Teacher(Person):
  def __init__(self, name, age, cid, subject):
    super().__init__(name, age, cid)
    self.subject = subject

