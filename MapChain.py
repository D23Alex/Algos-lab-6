import hashFunctions
from DoublyConnectedList import *
from ListElement import *


class MapChain:
    def __init__(self, size, hash_function=hashFunctions.uni_hash, chain_type=DoublyConnectedList, cell_type=ListElement):
        self.chainType = chain_type
        self.cellType = cell_type
        self.hashFunction = hash_function
        self.size = size
        self.list = [chain_type(cell_type) for i in range(size)]

    # Этот метод будет переопределён в производных классах
    def append(self, element):
        self.after_append()

    # Этот метод будет переопределён в производных классах
    def after_append(self):
        pass

    # объект если найдено, иначе false
    def search(self, key):
        chain_needed = self.list[self.hashFunction(key, self.size)]
        # поиск возвращает кортеж из найденной ячейки и найденной цепочки
        return chain_needed.search(key), chain_needed

    # Этот метод будет переопределён в производных классах
    def delete(self, key):
        self.after_delete()

    def after_delete(self):
        pass
