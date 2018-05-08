import csv
from time import time

from python_rtree import performance_test
from rtree_nn import *


def r_base_test(min=1, max=10, length=-1):
    def data_generate(path, length):
        """
        Data Header: business_id,name,stars,categories,latitude,longitude
        :param path: Data File Path
        :param length: Test File Length, -1 is default file length
        :return: return dict data
        """

        data = {}
        data_length = 0

        with open(path, "r") as f:
            if length == -1:
                reader = list(csv.reader(f))
            else:
                reader = list(csv.reader(f))[0: length]

            data_length = len(reader) - 1

            i = 0
            for row in reader[1:]:
                [_, _, _, _, x, y] = row

                if not x:
                    x = 0.0
                else:
                    x = float(x)

                if not y:
                    y = 0.0
                else:
                    y = float(y)

                data[i] = {'xmin': x, 'xmax': x + 0.01, 'ymin': y, 'ymax': y + 0.01}
                i += 1

        # data_length = length
        return data

    csv_path = r"../../data/yelp_business_min.csv"
    data = data_generate(csv_path, length)
    data_length = len(data.keys())

    root = Rtree(m=min, M=max)
    n = []

    for i in range(data_length):
        n.append(node(MBR=data[i], index=i))
    t0 = time()
    print("Data Loading Complete, in total " + str(data_length) + " row data")

    print("Start Building Index")

    for i in range(data_length):
        root = Insert(root, n[i])

    t1 = time()
    # print ('Inserting ...')
    print("Index Building Complete, in total " + str(data_length) + " row data, time: ")
    print(t1 - t0)

    # --------- use performance_test get the avg search time ---- #
    print("Min = " + str(min) + "; Max = " + str(max))
    avg_time, sum_time = performance_test.performance_test(root, [10, 150], 1)
    print("Avg Time for random 1 querys in Naive Way:")
    print(avg_time)
    print("Total Time for random 1 querys in Naive Way:")
    print(sum_time)

    avg_time, sum_time = performance_test.performance_test(root, [10, 150], 10)
    print("Avg Time for random 10 querys in Naive Way:")
    print(avg_time)
    print("Total Time for random 10 querys in Naive Way:")
    print(sum_time)

    avg_time, sum_time = performance_test.performance_test(root, [10, 150], 200)
    print("Avg Time for random 200 querys in Naive Way:")
    print(avg_time)
    print("Total Time for random 200 querys in Naive Way:")
    print(sum_time)

    # avg_time, sum_time = performance_test.performance_test(root, [10, 150], 10000)
    # print("Avg Time for random 10000 querys in Naive Way:")
    # print(avg_time)
    # print("Total Time for random 10000 querys in Naive Way:")
    # print(sum_time)


if __name__ == "__main__":
    r_base_test(min=1, max=25)
