
class PixelBox:

    def __init__(self, pos_x, color):
        self.pos_x = pos_x
        self.pos_y = -1
        self.color = color

    def fall(self):
        self.pos_y += 1
