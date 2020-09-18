"""Contains useful functions for file parsing."""

import array
import sys


def get_column(file_name, query_column, query_value, result_column=1):
    """Opens a CSV file and retrieves the desired column data based on inputs
    Inputs:
                file_name = string
                                    The name of the file to open
                query_column = integer
                                    The index of the column to query
                query_value = string
                                    The name of the value to query
                result_column = integer
                                    The index of the column to return
    """
    results = array.array('i', [])

    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print(file_name + ' could not be found. Please try again.')
        sys.exit(1)
    except PermissionError:
        print(file_name + ' could not be accessed. Please try again.')
        sys.exit(1)

    header = None

    for line in f:
        if header is None:
            header = line,
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
                      + str(len(A)) + '.' + ' Please try again.')
                sys.exit(1)

    return results
