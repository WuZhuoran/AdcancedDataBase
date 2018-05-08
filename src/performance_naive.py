import time

import pandas as pd

import select_without_tree

data_list = []
time_list = []


def performance(test_num):
    sample = pd.read_csv('../data/sample_10000.csv', header=None, nrows=test_num)

    for index, row in sample.iterrows():
        data_list.append([row[0], row[1]])

    for i in range(len(data_list)):
        start_time = time.time()
        result = select_without_tree.select_by_lat_lon(data_list[i][0], data_list[i][1], 25)
        end_time = time.time()

        time_list.append(end_time - start_time)

    sum_time = sum(time_list)
    avg_time = sum_time / len(time_list)

    print("Avg Time for random " + str(test_num) + " querys in Naive Way:")
    print(avg_time)
    print("Total Time for random " + str(test_num) + " querys in Naive Way:")
    print(sum_time)


if __name__ == "__main__":
    performance(1)
    performance(10)
    performance(200)
