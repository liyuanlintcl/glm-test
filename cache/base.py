class Base:
    def __init__(self):
        self.dict = {}

    def get(self, key):
        raise NotImplemented

    def set(self, key, value):
        raise NotImplemented