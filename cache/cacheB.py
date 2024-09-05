from .base import Base


class CacheB(Base):
    def __init__(self):
        super().__init__()

    def get(self, key):
        key = key + 'B'
        return self.dict[key]

    def set(self, key, value):
        key = key + 'B'
        self.dict[key] = value