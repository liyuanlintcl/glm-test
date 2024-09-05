from .base import Base

class CacheA(Base):
    def __init__(self):
        super().__init__()

    def get(self, key):
        key = key + 'A'
        return self.dict[key]

    def set(self, key, value):
        key = key + 'A'
        self.dict[key] = value