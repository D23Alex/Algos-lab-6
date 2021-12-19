# абсолютно все классы не защищены от тупых действий(удаление первого элемента списка, удаление из пустого списка...)

import settings
from MapChainTask2 import *
from helpers import *


def execute(command, my_map, file):
    key = int(command[1])
    if command[0] == 'add':
        my_map.append(ListElement(key, command[2]))
    elif command[0] == 'find':
        answer = my_map.search(key)[0]
        if answer is False:
            file.write('not found' + '\n')
        else:
            file.write(answer.value + '\n')
    else:
        my_map.delete(key)


def main():
    size, data = inputs_by_line('input.txt')

    file_out = open('output.txt', 'w')
    file_out.close()
    file_out = open('output.txt', 'a')

    my_map = MapChainTask2(size)
    for command in data:
        execute(command, my_map, file_out)

    file_out.close()


def test():
    a = DoublyConnectedList(ListElement)
    a.insert_after(ListElement(1,'aboba1'), a.first)
    print(a)


main()
