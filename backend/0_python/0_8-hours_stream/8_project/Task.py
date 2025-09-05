from datetime import datetime

class Task:
  total_number = 0

  def __init__(self, name, desc='', stat='open', term=datetime.today(), exec=None):
    self.set_name(name)
    self.set_desc(desc)
    self.set_stat(stat)
    self.set_term(term)
    self.set_exec(exec)
    self.id = Task.total_number
    Task.total_number += 1
  
  def get_name(self):
    return self.name
  def get_desc(self):
    return self.desc
  def get_stat(self):
    return self.stat
  def get_term(self):
    return self.term
  def get_exec(self):
    return self.exec

  def set_name(self, value):
    self.name = value
  def set_desc(self, value):
    self.desc = value
  def set_stat(self, value):
    value = value.lower()
    if value in {"open", "work", "test", "done"}:
      self.stat = value
    else:
      print("Ошибка статуса!")
      raise ValueError

  def set_term(self, value):
    if isinstance(value, datetime):
      self.term = value
    else:
      self.term = datetime.strptime(value, "%d.%m.%y")
  def set_exec(self, value):
    self.exec = value
  
  def __str__(self):
    b = "\n#==== ====#\n"
    e = "\n#==== ====#"
    if self.desc != '':
      s = f"{b}Задача:\n{self.name}\n\nОписание:\n{self.desc}{e}"
    else:
      s = f"{b}Задача:\n{self.name}{e}"
    return s
