import subprocess
import os

count_command = f'python ./cfbadge/get_tasks_count.py'
count = subprocess.check_output(count_command, shell=True).strip().decode()

with open('./cfbadge/badge_template.svg', 'r') as f:
    badge = f.read()

badge = badge.replace('{count}', count)

if not os.path.exists('./cfbadge/output'):
    os.makedirs('./cfbadge/output')

if os.path.exists('./cfbadge/output/badge_updated.svg'):
    os.remove('./cfbadge/output/badge_updated.svg')

with open('./cfbadge/output/badge_updated.svg', 'w') as f:
    f.write(badge)