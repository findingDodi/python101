
class PixelBox:

    def __init__(self, pos_x, color):
        self.pixel_box_pos_x = pos_x
        self.pixel_box_pos_y = -1
        self.pixel_box_color = color

    def fall(self):
        self.pixel_box_pos_y += 1
