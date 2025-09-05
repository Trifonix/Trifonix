class MyNumber:
    def __init__(self, number: int) -> None:
        self.number = number
    
    def __int__(self) -> int:
        return float(self.number) # Error: float return!

print(int(MyNumber(5)))
# TypeError: __int__ returned non-int (type float)
