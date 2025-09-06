from Team import Team

if __name__ == "__main__":
  bar = Team.Employee("Бараш")
  los = Team.Employee("Лосяш")
  kro = Team.Employee("Крош")
  my_team = Team("Смешарики", "Лучшая команда", [bar, los, kro])
  tm = my_team.get_task_mngr()

  nol = Team.Employee("Нолик")
  sim = Team.Employee("Симка")
  my_team2 = Team("Фиксики", "Нормальная команда", [nol, sim])
  tm2 = my_team2.get_task_mngr()

  #tm.new_task()
  tm.new_task("Поставить лайк", stat="work")
  tm.new_task("Смонтировать видео", stat="test")
  tm.new_task("Опубликовать shorts", stat="done", term="30.08.25")

  # tm.show_all_today()
  tm.show_by_status("work")

  tm2.new_task("Починить всё", term="01.02.11", stat="done")
  tm2.show_by_status("done")
