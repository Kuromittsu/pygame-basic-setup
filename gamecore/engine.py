from gamecore.core import Core


class Engine():

    def __init__(self, title: str):
        self.core = Core(title)

    def init(self):
        self.core.run()
