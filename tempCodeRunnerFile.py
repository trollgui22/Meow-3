class PushButton:
    def __init__(self, x, y, width, height, image, batch):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.sprite = pyglet.sprite.Sprite(self.image, self.x, self.y, batch=batch)
        self.sprite.scale = 0.1
        self.sprite.opacity = 0

    def on_mouse_press(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            self.sprite.opacity = 255
            time.sleep(0.1)
            self.sprite.opacity = 0

    def on_draw(self):
        self.sprite.draw()
