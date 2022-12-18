from levels.test_camera import Test_camera


class Game():

    def __init__(self, core, title):
        self.core = core
        self.title = title
        self.fps = 0

    def setup(self):
        self.test_camera = Test_camera(self.core)

    def update(self):
        self.test_camera.update()

    def draw(self):
        self.test_camera.draw()

    def after_draw(self):
        pass

    def before_flip(self):
        pass
