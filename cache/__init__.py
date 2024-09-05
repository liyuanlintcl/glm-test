import importlib
import os

from .base import Base
from .cacheA import CacheA
from .cacheB import CacheB

cache = CacheA() if os.environ.get('CACHE') == 'cacheA' else CacheB()

class CacheHandler:
    def __init__(self):
        cache_type = os.environ.get('CACHE')
        cache_module = importlib.import_module('cache.' + cache_type)
        self.cache = getattr(cache_module, cache_type[0].upper() + cache_type[1:])()

    def __getattr__(self, name):
        return getattr(self.cache, name)

cache_ = CacheHandler()

def cache_get(key):
    return cache.get(key)

def cache_set(key, value):
    return cache.set(key, value)