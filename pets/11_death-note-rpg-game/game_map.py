class GameMap:
    def __init__(self):
        self.locations = ["Школа", "Город", "Дом Ягами", "Место встречи с Рюком"]
        self.current_index = 0
    
    def current_location(self):
        return self.locations[self.current_index]
    
    def move_next(self):
        if self.current_index < len(self.locations) - 1:
            self.current_index += 1
        return self.current_location()
