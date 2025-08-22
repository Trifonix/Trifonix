from datetime import datetime
from Task import Task

class Team:
  class TaskManager:
    def __init__(self, task_list=[]):
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

  def __init__(self, name, desc, list):
    self.name = name
    self.desc = desc
    self.list = list
    self.task_mngr = Team.TaskManager()
