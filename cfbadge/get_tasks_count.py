import requests

handle = 'Trifonix'

url = f'https://codeforces.com/api/user.status?handle={handle}'

response = requests.get(url)

if response.status_code == 200:
    submissions = response.json()['result']
    accepted_tasks = set()
    for submission in submissions:
        if submission['verdict'] == 'OK':
            current_task = f"{submission['problem']['contestId']}"
            accepted_tasks.add(current_task)
    print(len(accepted_tasks))