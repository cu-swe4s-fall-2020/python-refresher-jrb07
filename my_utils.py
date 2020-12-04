"""
Contains custom functions that will perform various file and
text parsing to extract data from CSV files based
on given user defined parameters.
"""

import array
import sys
import numpy as np
from dateutil.parser import parse
from datetime import timedelta
import pandas as pd


def binary_search(query, pairs):
    start = -1
    end = len(pairs)

    while(end - start > 1):
        mid = (end + start)//2

        if query == pairs[mid][0]:
            return pairs[mid][1]
        elif query < pairs[mid][0]:
            end = mid
        else:
            start = mid
    return None


def linear_search(query, pairs):
    for key, value in pairs:
        if query == key:
            return value


def get_columns(file_name,
                query_column,
                query_value,
                result_columns=[],
                date_column=1):
    '''
    This function leverages get column to create a list
    of results that includes data from multiple result columns.
    '''
    if result_columns == []:
        print('result column assigned as an empty array please re-assign')
        raise ValueError(sys.exit(6))
    results = []
    for i in range(len(result_columns)):
        results.append(get_column(
            file_name,
            query_column,
            query_value,
            result_columns[i],
            date_column))

    return results


def get_column(file_name,
               query_column,
               query_value,
               result_column=1,
               date_column=1):
    """
    Opens a CSV file and retrieves the desired column data based on
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
                date_column = integer
                                    The index of the column containing dates
    """
    results = []

    f = open_file(file_name)

    header = None
    date = None
    _date = None
    delta_date = None

    for line in f:
        if header is None:
            header = line,
            result_column = handle_result_column(result_column, line)
            continue

        A = line.rstrip().split(',')
        if A[query_column] == query_value:
            try:
                results.append(A[result_column])
            except ValueError:
                print('Could not append result.')
                sys.exit(6)

            if date_column is not None:
                if is_date(A[date_column]):
                    date = parse(A[date_column])
                else:
                    f.close()
                    print('Date column was not assigned correctly.')
                    raise ValueError(sys.exit(6))
                if _date is None:
                    _date = date
                    continue
                delta_date = date - _date
                if delta_date.days >= 0:
                    _date = date
                else:
                    f.close()
                    print('Dates are out of order.')
                    raise ValueError(sys.exit(6))

    f.close()

    return results


def open_file(file_name):
    '''
    Will try to open a file with the given file
    name and handles exceptions that may occur.
    '''
    try:
        f = open(file_name, 'r', encoding='latin-1')
    except FileNotFoundError:
        print('The file ' + file_name
              + ' could not be found. Please try again.')
        sys.exit(1)
    except PermissionError:
        print(file_name
              + ' could not be accessed. Please try again.')
        sys.exit(2)

    return f


def get_daily_count(data):
    '''
    Returns an array of results that represent the change in
    value from index to index in the array.
    '''
    results = []
    last_x = None

    for x in data:
        if last_x is None:
            last_x = x
            continue
        try:
            delta = x - last_x
        except TypeError:
            delta = int(x) - int(last_x)
        results.append(delta)
        last_x = x

    return results


def running_average(data,
                    window_size=5):
    '''
    Takes in an array of data then scans and averages the
    values of that array based on the provided window size.
    '''
    results = []
    average = 0
    if data is None:
        print('No data passed to running_average')
        raise ValueError(sys.exit(3))
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


def handle_result_column(result_column,
                         line):
    try:
        result_column = int(result_column)
        return result_column
    except ValueError:
        pass
    '''
    Converts a string result_column to the corresponding
    integer ID of that column if it exists.
    '''
    A = line.rstrip().split(',')
    try:
        result_column = A.index(result_column)
    except ValueError:
        print('result_column_str was assigned as ' + str(result_column)
              + ' and is out of range. '
              + 'Available result columns are '
              + str(A))
        sys.exit(4)
    return result_column


def is_date(string,
            fuzzy=False):
    '''
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    '''
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False
