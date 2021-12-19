# абсолютно все классы не защищены от тупых действий(удаление первого элемента списка, удаление из пустого списка...)

import settings
from MapChainTask4 import *
from helpers import *
from hashFunctions import *


def execute(command, my_map, file):
    # тут ключ и значение совпадают и являются строкой
    if command[0] == 'get':
        element_found = my_map.search(command[1])[0]
        if element_found is False:
            file.write('<none>\n')
        else:
            file.write(element_found.value + '\n')
    elif command[0] == 'prev':
        element_found = my_map.search(command[1])[0]
        if element_found is False:
            file.write('<none>\n')
        elif element_found.previousCommandElement is None:
            file.write('<none>\n')
        else:
            file.write(element_found.previousCommandElement.value + '\n')

    elif command[0] == 'next':
        element_found = my_map.search(command[1])[0]
        if element_found is False:
            file.write('<none>\n')
        elif element_found.nextCommandElement is None:
            file.write('<none>\n')
        else:
            file.write(element_found.nextCommandElement.value + '\n')
    elif command[0] == 'put':
        my_map.append(ListElementTask4(command[1], command[2]))
    else:
        my_map.delete(command[1])


def main():
    size, data = inputs_by_line('input.txt')

    file_out = open('output.txt', 'w')
    file_out.close()
    file_out = open('output.txt', 'a')

    my_map = MapChainTask4(size)
    for command in data:
        execute(command, my_map, file_out)

    file_out.close()


main()
