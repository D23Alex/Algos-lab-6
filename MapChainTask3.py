from MapChain import *


# в этом классе при добавлении ищем элемент, если он есть - ничего не делаем, иначе добавляем в начало
class MapChainTask3(MapChain):
    def __init__(self, size, hash_function=hashFunctions.ascii_task_3, chain_type=DoublyConnectedList,
                 cell_type=ListElement):
        self.chainType = chain_type
        self.cellType = cell_type
        self.hashFunction = hash_function
        self.size = size
        self.list = [chain_type(cell_type) for i in range(size)]

    def append(self, element):
        cell_found, chain_found = self.search(element.key)
        # если нашли что-то - ничего не делаем. Если не нашли - добавим новый элемент
        if not cell_found:
            # добваляем в начало
            chain_found.insert_after(element, chain_found.first)

    def delete(self, key):
        cell_found, chain_found = self.search(key)
        # если не нашли - ничего не делаем, а если нашли - удаляем
        if cell_found is not False:
            chain_found.delete(cell_found)
