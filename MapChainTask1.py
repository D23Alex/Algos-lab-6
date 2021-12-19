from MapChain import *


# в этом классе value не важны и при добавлении ищем элемент, если он есть - ничего не делаем, иначе добавляем в начало
class MapChainTask1(MapChain):
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
