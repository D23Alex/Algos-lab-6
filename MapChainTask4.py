from MapChain import *
from ListElementTask4 import *


# в этом классе value не важны и при добавлении ищем элемент, если он есть - ничего не делаем, иначе добавляем в начало
# сделано так, чтобы в любой момент времени у любого элемента в свойствах ...
# были последний добавленный перед ним элемент и первый добавленный после него элемент
class MapChainTask4(MapChain):
    def __init__(self, size, hash_function=hashFunctions.ascii_task_3, chain_type=DoublyConnectedList,
                 cell_type=ListElement):
        self.chainType = chain_type
        self.cellType = cell_type
        self.hashFunction = hash_function
        self.size = size
        self.list = [chain_type(cell_type) for i in range(size)]
        self.lastAppendedElement = None

    def append(self, element):
        cell_found, chain_found = self.search(element.key)
        # если нашли что-то - изменяем значение. Если не нашли - добавим новый элемент
        if not cell_found:
            # добваляем в начало
            chain_found.insert_after(element, chain_found.first)
            if self.lastAppendedElement is not None:
                self.lastAppendedElement.nextCommandElement = element
            element.previousCommandElement = self.lastAppendedElement
            self.lastAppendedElement = element
        else:
            # если мы тут, значит нашли - просто поменяем значение
            cell_found.value = element.value

    def delete(self, key):
        cell_found, chain_found = self.search(key)
        # если не нашли - ничего не делаем, а если нашли - удаляем
        if cell_found is not False:
            # на всякий случай а то вдруг мусорщик удалит найденную штуку
            cell = cell_found
            chain_found.delete(cell_found)
            # теперь после удаления надо проставить предыдущему и след. элементу правильные nextCommand и previousCom.
            if cell.previousCommandElement is not None:
                cell.previousCommandElement.nextCommandElement = cell.nextCommandElement
            if cell.nextCommandElement is not None:
                cell.nextCommandElement.previousCommandElement = cell.previousCommandElement
            # а что если удалили последний элемент? надо починить ссылку на последний элемент
            if cell == self.lastAppendedElement:
                self.lastAppendedElement = cell.previousCommandElement
