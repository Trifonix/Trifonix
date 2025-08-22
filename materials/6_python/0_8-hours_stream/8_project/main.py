from Team import Team

my_team = Team("Смешарики", "Лучшая команда", ["Бараш", "Лосяш", "Крош"])

my_team.task_mngr.new_task("Провести стрим", stat="open", term="29.08.25")
my_team.task_mngr.new_task("Поставить лайк", stat="work")
my_team.task_mngr.new_task("Смонтировать видео", stat="test")
my_team.task_mngr.new_task("Опубликовать shorts", stat="done", term="30.08.25")

# my_team.task_mngr.show_all_today()
my_team.task_mngr.show_by_status("done")
