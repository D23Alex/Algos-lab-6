def inputs_by_line(file_name):
    file_open = open(file_name, 'r')
    data = []
    while True:
        # считываем строку
        line = file_open.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        data.append([i for i in line.split()])
    n = int(data[0][0])
    del data[0]
    file_open.close()
    return n, data


def inputs_by_line_task3(file_name):
    file_open = open(file_name, 'r')
    data = []
    while True:
        # считываем строку
        line = file_open.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        data.append([i for i in line.split()])
    n = int(data[0][0])
    t = int(data[1][0])
    del data[0]
    del data[0]
    file_open.close()
    return n, t, data
