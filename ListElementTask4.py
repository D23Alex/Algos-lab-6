class ListElementTask4:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None
        # будем хранить ссылки на 2 элемента - тот что выдаётся командой next и тот что командой last
        # при удалении, добавлении изменяется соответствующим образом
        self.nextCommandElement = None
        self.previousCommandElement = None

    def __str__(self):
        return '{}: {}'.format(self.key, self.value)
