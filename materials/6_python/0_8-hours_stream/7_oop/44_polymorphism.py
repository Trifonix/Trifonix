# Полиморфизм

class Animal:
  def __init__(self, name, age, fed):
    self.name = name
    self.age = age
    self.fed = fed

  def feed(self):
    if not self.fed:
      print(f"{self.name} говорит: Ням-Ням")
      self.fed = True

class Dog(Animal):
  def __init__(self, name, age, fed, walks):
    super().__init__(name, age, fed)
    self.walks = walks

  def feed(self):
    if not self.fed:
      print(f"{self.name} говорит: опять сухой корм. А я хотел баранину")
      self.fed = True

class Cat(Animal):
  def __init__(self, name, age, fed, count_mice):
    super().__init__(name, age, fed)
    self.count_mise = count_mice

  def feed(self):
    if not self.fed:
      if self.count_mise > 0:
        print(f"{self.name} говорит: я съел мыш")
        self.fed = True
        self.count_mise -= 1
      else:
        print(f"{self.name} говорит: меня покормил молоком хозяин")
        self.fed = True

class Capybara(Animal):
  def __init__(self, name, age, fed):
    super().__init__(name, age, fed)

dog = Dog("Жучка", 5, False, 3)
cat = Cat("Барсик", 10, False, 10)
capy = Capybara("Кап", 4, False)

dog.feed()
cat.feed()
capy.feed()
