class ListElement:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return '{}: {}'.format(self.key, self.value)
    