from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.now()

    def __str__(self):
        return f'[{self.created_at.strftime("%Y-%m-%d_%H:%M")}] {self.title}: {self.content}'
