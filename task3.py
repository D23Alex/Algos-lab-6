# абсолютно все классы не защищены от тупых действий(удаление первого элемента списка, удаление из пустого списка...)

import settings
from MapChainTask3 import *
from helpers import *
from hashFunctions import *


def execute(command, my_map, file):
    # тут ключ и значение совпадают и являются строкой
    if command[0] == 'add':
        my_map.append(ListElement(command[1], command[1]))
    elif command[0] == 'check':
        file.write(str(my_map.list[int(command[1])]))
        file.write('\n')
    elif command[0] == 'find':
        answer = my_map.search(command[1])[0]
        if answer is False:
            file.write('no' + '\n')
        else:
            file.write('yes' + '\n')
    else:
        my_map.delete(command[1])


def main():
    size, n, data = inputs_by_line_task3('input.txt')

    file_out = open('output.txt', 'w')
    file_out.close()
    file_out = open('output.txt', 'a')

    my_map = MapChainTask3(size)
    for command in data:
        execute(command, my_map, file_out)

    file_out.close()


main()
