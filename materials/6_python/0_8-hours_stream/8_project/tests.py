from Team import Team
from datetime import datetime
from Task import Task

def test_task():
  for _ in range(10):
    t = Task(
      name="Провести стрим", 
      desc="Подробное описание таски",
      stat="open",
      term="22.08.25",
      exec=Team.Employee("Каркарыч")
    )
    assert t.name == "Провести стрим"
    assert t.desc == "Подробное описание таски"
    assert t.stat == "open"
    assert t.term == datetime.strptime("22.08.25", "%d.%m.%y")
    assert t.exec.name == "Каркарыч"

def test_team():
  for _ in range(10):
    bar = Team.Employee("Бараш")
    los = Team.Employee("Лосяш")
    kro = Team.Employee("Крош")
    my_team = Team("Смешарики", "Лучшая команда", [bar, los, kro])
    assert my_team.name == "Смешарики"
    assert my_team.desc == "Лучшая команда"
    assert len(my_team.list) == 3
    assert len(my_team.task_mngr.task_list) == 0
    test_employee = Team.Employee("Test Test")
    my_team.add_empl(test_employee)
    assert len(my_team.list) == 4
    my_team.del_empl(test_employee)
    assert len(my_team.list) == 3
    t1 = Task(
      name="Провести стрим", 
      desc="Подробное описание таски",
      stat="open",
      term="22.08.25",
      exec=Team.Employee("Каркарыч")
    )
    t2 = Task(
      name="Смонтировать видео", 
      desc="Подробное описание таски",
      stat="open",
      term="22.08.25",
      exec=Team.Employee("Каркарыч")
    )
    my_team.new_task(t1)
    my_team.new_task(t2)
    tm = my_team.get_task_mngr()
    assert len(tm.task_list) == 2
    my_team.del_task(t2)
    assert len(tm.task_list) == 1
    tm.show_all()
    tm.show_all_today()
    for status in ["open", "work", "test", "done"]:
      tm.show_by_status("done")
