class MyArrayList:
    def __init__(self):
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def get(self, index):
        if 0 <= index < len(self.elements):
            return self.elements[index]
        raise IndexError("Index out of bounds")

    def size(self):
        return len(self.elements)

    def clear(self):
        self.elements.clear()

    def remove(self, index):
        if 0 <= index < len(self.elements):
            del self.elements[index]
        else:
            raise IndexError("Index out of bounds")
