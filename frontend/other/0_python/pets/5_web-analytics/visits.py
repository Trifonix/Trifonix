from datetime import datetime

class Visit:
    def __init__(self, ip: str, user_agent: str):
        self.ip = ip
        self.user_agent = user_agent
        self.time = datetime.now()

visits_list = []
