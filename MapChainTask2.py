from MapChain import *


# в этом классе при добавлении существующего key, value - перезаписывается
class MapChainTask2(MapChain):
    def append(self, element):
        cell_found, chain_found = self.search(element.key)
        # если нашли что-то - перезаписываем.
        if cell_found is not False:
            # добваляем в начало
            cell_found.value = element.value
        else:
            # если не найдено
            chain_found.insert_after(element, chain_found.first)

    def delete(self, key):
        cell_found, chain_found = self.search(key)
        # если не нашли - ничего не делаем, а если нашли - удаляем
        if cell_found is not False:
            chain_found.delete(cell_found)
