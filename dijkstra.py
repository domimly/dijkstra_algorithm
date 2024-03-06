from pqdict import pqdict


def dijkstra(array: [[int]]):

    n = 0  # for check if only two zeros in matrix
    zeros_indexes = []

    array_size = [0, 0]
    array_size[0] = len(array)
    array_size[1] = len(array[0])

    for i in range(array_size[0]):
        for j in range(array_size[1]):
            if array[i][j] == 0:
                zeros_indexes.append((i, j))
                n += 1
    if n != 2:
        print("There's too many 0 points (should be 2)")
        exit(1)

    dist = [[999999 for j in range(array_size[1])] for i in range(array_size[0])]
    prev_on_path = [
        [(-1, -1) for j in range(array_size[1])] for i in range(array_size[0])
    ]

    dist[zeros_indexes[0][0]][zeros_indexes[0][1]] = 0

    queue = pqdict()

    for i in range(array_size[0]):
        for j in range(array_size[1]):
            queue.additem((i, j), 999999)

    queue.updateitem(zeros_indexes[0], 0)

    while len(queue) > 0:
        tmp = queue.pop()
        for i, j in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            if (
                tmp[0] + i < array_size[0]
                and tmp[0] + i >= 0
                and tmp[1] + j < array_size[1]
                and tmp[1] + j >= 0
            ):
                dist_from_tmp = dist[tmp[0]][tmp[1]] + array[tmp[0] + i][tmp[1] + j]
                if dist_from_tmp < dist[tmp[0] + i][tmp[1] + j]:
                    dist[tmp[0] + i][tmp[1] + j] = dist_from_tmp
                    prev_on_path[tmp[0] + i][tmp[1] + j] = tmp
                    queue.updateitem((tmp[0] + i, tmp[1] + j), dist_from_tmp)

    path = [[" " for j in range(array_size[1])] for i in range(array_size[0])]

    previous = (zeros_indexes[1][0], zeros_indexes[1][1])

    while previous != (-1, -1):
        path[previous[0]][previous[1]] = str(array[previous[0]][previous[1]])
        previous = prev_on_path[previous[0]][previous[1]]

    for i in path:
        for j in i:
            print(j, end="")
        print()
