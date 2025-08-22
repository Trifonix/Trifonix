from datetime import datetime
from Task import Task

class Team:
  class TaskManager:
    def __init__(self, task_list=None):
      if task_list is None:
        task_list = []
      self.task_list = task_list

    def new_task(self, *args, **kwargs):
      t = Task(*args, **kwargs)
      self.task_list.append(t)

    def del_task(self, id):
      for x in self.task_list:
        if x.id == id:
          self.task_list.remove(x)
          break
    
    def show_all(self):
      for x in self.task_list:
        print(x)
    
    def show_all_today(self):
      for x in self.task_list:
        if x.term <= datetime.today():
          print(x)
    
    def show_by_status(self, stat):
      for x in self.task_list:
        if x.stat == stat:
          print(x)

  class Employee:
    def __init__(self, name):
      self.name = name
    
    def get_name(self):
      return self.name

    def set_name(self, value):
      self.name = value
  
  def __init__(self, name, desc, list):
    self.set_name(name)
    self.set_desc(desc)
    self.set_list(list)
    self.task_mngr = Team.TaskManager()

  def get_name(self):
    return self.name
  def get_desc(self):
    return self.desk
  def get_list(self):
    return self.list
  def get_task_mngr(self):
    return self.task_mngr

  def set_name(self, value):
    self.name = value
  def set_desc(self, value):
    self.desk = value
  def set_list(self, value):
    self.list = []
    for x in value:
      if isinstance(x, Team.Employee):
        self.add_empl(x)
      else:
        raise ValueError("Попытка создать команду с не-сотрудником")
  def add_empl(self, empl):
    self.list.append(empl)
  def del_empl(self, empl):
    self.list.remove(empl)

  def new_task(self, *args, **kwargs):
    tm = self.get_task_mngr()
    tm.new_task(*args, **kwargs)

  def del_task(self, id):
    tm = self.get_task_mngr()
    tm.del_task(id)
