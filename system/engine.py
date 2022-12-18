from system.core import Core


class Engine():

    def __init__(self, title):
        self.core = Core(title)

    def init(self):
        self.core.run()
