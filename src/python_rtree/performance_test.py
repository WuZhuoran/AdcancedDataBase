from time import time

import pandas as pd


def performance_test(tree_root, search_range, test_num):
    """
    test the avg time of search in the tree
    ----------------------------
    :param tree_root: the root of tree
    :param search_range: the range of the test dataset
    :return: the average time of search
    """
    time_list = []
    data_list = []

    sample = pd.read_csv('../../data/sample_10000.csv', header=None, nrows=test_num)

    for index, row in sample.iterrows():
        data_list.append([row[0], row[1]])

    # for i in range(test_num):
        # data_list.append([random.randint(0, search_range[0]),random.randint(0, search_range[1])])

    for i in range(len(data_list)):
        MBR = {'xmin': data_list[i][0], 'xmax': data_list[i][0] + 0.1,
               'ymin': data_list[i][1], 'ymax': data_list[i][1] + 0.1}

        start_time = time()
        result = tree_root.Search(MBR)
        end_time = time()

        time_list.append(end_time - start_time)

        sum_time = sum(time_list)
        avg_time = sum_time / len(time_list)

    return avg_time, sum_time


if __name__ == "__main__":
    performance_test()
