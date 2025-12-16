# Проверка, установлен ли pip
''' pip --version '''
# pip 25.3

# Установка пакета requests
''' pip install requests '''
# Requirement already satisfied: requests

# Установка конкретной версии numpy
''' pip install numpy==1.21.0 '''
# pip._vendor.pyproject_hooks._impl.BackendUnavailable: Cannot import 'setuptools.build_meta'

# Обновление пакета requests до последней версии
''' pip install --upgrade requests '''
# Successfully installed requests-2.32.5

# Удаление пакета requests
''' pip uninstall -y requests '''

# Список всех установленных пакетов
''' pip list '''
# wsproto                   1.2.0
