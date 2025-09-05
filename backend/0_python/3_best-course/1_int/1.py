# Какие __магические__ методы превращают объект в int?

class MyNumber:
    def __init__(self, number: int) -> None:
        self.number = number
    
    def __int__(self) -> int:
        return self.number

print(int(MyNumber(5))) # 5
