"""
Contains custom functions that will accomplish various file and
text parsing to extract data from files based
on given user defined parameters.
"""

import array
import sys
import numpy as np


def get_column(file_name, query_column, query_value, result_column=1):
    """Opens a CSV file and retrieves the desired column data based on
    the following parameters.
    Parameters:
                file_name = string
                                    The name of the file to open
                query_column = integer
                                    The index of the column to query
                query_value = string
                                    The name of the value to query
                result_column = integer or string
                                    The index or name of the column to return
    """
    results = array.array('i', [])

    f = open_file(file_name)

    header = None

    for line in f:
        if header is None:
            header = line,
            result_column = handle_result_column(result_column, line)
            continue

        A = line.rstrip().split(',')

        if A[query_column] == query_value:
            try:
                results.append(int(A[result_column]))
            except IndexError:
                index = str(result_column)
                print('result_column was assigned as '
                      + str(result_column)
                      + ' and is out of range. The range is 0-'
                      + str(len(A)-1) + '.' + ' Please try again.')
                sys.exit(1)
    f.close()

    return results


def open_file(file_name):
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        #         print('The file ' + file_name
        #               + ' could not be found. Please try again.')
        sys.exit(1)
    except PermissionError:
        #         print(file_name
        #               + ' could not be accessed. Please try again.')
        sys.exit(1)

    return f


def get_daily_count(data):
    results = []
    last_x = None

    for x in data:
        if last_x is None:
            last_x = x
            continue
        delta = x - last_x
        results.append(delta)
        last_x = x

    return results


def running_average(data, window_size=5):
    results = []
    average = 0
    if data is None:
        #         print('No data passed to running_average')
        sys.exit(2)
    try:
        data[window_size]
    except IndexError:
        #         print('Updating window_size from ' + str(window_size) +
        #               ' to ' + str(len(data)))
        window_size = len(data)
        return np.mean(data), window_size

    for i in range(len(data)-window_size+1):
        results.append(np.mean(data[i:i+window_size]))

    return results, window_size


def handle_result_column(result_column, line):
    A = line.rstrip().split(',')
    if isinstance(result_column, str):
        try:
            result_column = A.index(result_column)
        except ValueError:
            print('result_column_str was assigned as ' + result_column
                  + ' and is out of range. '
                  + 'Available result columns are '
                  + str(A))
            sys.exit(1)
    return result_column
