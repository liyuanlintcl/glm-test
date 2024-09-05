class A:
    def __init__(self, value):
        self.value = value

    def set(self, v):
        self.value = v

    def get(self):
        return self

class B(A):
    def __init__(self, value):
        super().__init__(value)

    def get(self):
        v = super().get()
        v.set(self.value)

if __name__ == '__main__':
    a = A(1)
    a.set(0)
    a.get()
    b = B(1)
    b.set(0)
    b.get()

