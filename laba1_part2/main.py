from vector import Vector


def counter(lens, average):
    k = 0
    for x in lens:
        if x > average:
            k += 1
    return k


files = ['input01.txt', 'input02.txt', 'input03.txt', 'input04.txt']
for file in files:
    maxi_dim = [0, 10 ** 13]
    maxi_len = [0, 100000]
    maxi_coord = [0, 0]
    mini_coord = [0, 0]
    lens = []
    with open(file) as f:
        for line in f:
            data = [int(el) for el in line.split()]
            if data != []:
                vec = Vector(data)
                cur_dim = vec.dim()
                cur_len = vec.lenght()
                maxi_data = max(data)
                mini_data = min(data)
                lens.append(cur_len)

                if cur_dim == maxi_dim[0]:
                    if cur_len < maxi_dim[1]:
                        vector_dim = 'Vector ' + str(data)
                        maxi_dim = [cur_dim, cur_len]
                elif cur_dim > maxi_dim[0]:
                    vector_dim = 'Vector ' + str(data)
                    maxi_dim = [cur_dim, cur_len]

                if cur_len == maxi_len[0]:
                    if cur_dim < maxi_len[1]:
                        vector_len = 'Vector ' + str(data)
                        maxi_len = [cur_len, cur_dim]
                elif cur_len > maxi_dim[0]:
                    vector_len = 'Vector ' + str(data)
                    maxi_len = [cur_len, cur_dim]

                if maxi_data == maxi_coord[0]:
                    if mini_data < maxi_coord[1]:
                        maxi_coord = [maxi_data, mini_data]
                        vector_max_coord = 'Vector ' + str(data)
                elif maxi_data > maxi_coord[0]:
                    maxi_coord = [maxi_data, mini_data]
                    vector_max_coord = 'Vector ' + str(data)

                if mini_data == mini_coord[0]:
                    if maxi_data > mini_coord[1]:
                        mini_coord = [mini_data, maxi_data]
                        vector_min_coord = 'Vector ' + str(data)
                elif mini_data < mini_coord[0]:
                    mini_coord = [mini_data, maxi_data]
                    vector_min_coord = 'Vector ' + str(data)



    print(f'Vector with maximum dim in {file}:', vector_dim, '\nDim:', maxi_dim[0], '\nLen:', maxi_dim[1])
    print(f'Vector with maximum len in {file}:', vector_len, '\nDim:', maxi_len[1], '\nLen:', maxi_len[0])
    print('Average length of the vectors:', sum(lens) / len(lens))
    print('The number of vectors with a length greater than the average length:', counter(lens, sum(lens) / len(lens)))
    print('Vector with the maximum coord:', vector_max_coord)
    print('Vector with the minimum coord:', vector_min_coord)
    print('\n')

