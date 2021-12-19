# абсолютно все классы не защищены от тупых действий(типа удаления первого элемента списка)
from random import randint

import settings
import hashFunctions
from ListElement import  *


def test():
    my_set = MapChainTask1(8)
    my_set.append(ListElement(2, 1))
    my_set.append(ListElement(5, 1))
    my_set.append(ListElement(3, 1))
    a = my_set.search(2)
    b = my_set.search(4)
    pass


def inputs(file):
    file_open = open(file, 'r')
    data = [i for i in file_open.read().split()]
    file_open.close()
    size = int(data[0])
    del data[0]
    return size, data


def execute(command, key, my_set, file):
    if command == 'A':
        # value будем ставить 1 - не имеет значения в 1 задаче
        my_set.append(ListElement(key, 1))
    elif command == 'D':
        my_set.delete(key)
    else:
        if my_set.search(key)[0] is False:
            file.write('N\n')
        else:
            file.write('Y\n')


def main():
    size, data = inputs('input.txt')

    file_out = open('output.txt', 'w')
    file_out.close()
    file_out = open('output.txt', 'a')

    my_set = MapChainTask1(size)
    for i in range(0, 2 * size - 1, 2):
        execute(data[i], int(data[i + 1]), my_set, file_out)

    file_out.close()


main()

