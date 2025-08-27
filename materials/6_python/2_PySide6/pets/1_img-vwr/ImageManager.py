import os

class ImageManager:
    def __init__(self):
        self.images = []
        self.current_index = -1

    def scan_directory(self, directory):
        self.images = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    self.images.append(os.path.join(root, file))
        if self.images:
            self.current_index = 0

    def get_current_image(self):
        if 0 <= self.current_index < len(self.images):
            return self.images[self.current_index]
        return None

    def next_image(self):
        if self.images:
            self.current_index = (self.current_index + 1) % len(self.images)

    def prev_image(self):
        if self.images:
            self.current_index = (self.current_index - 1) % len(self.images)
