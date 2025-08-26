from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.now()

    def __str__(self):
        return f'[{self.created_at}] {self.title}: {self.content}'
