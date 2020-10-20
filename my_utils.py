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


def get_column(file_name, query_column, query_value,
               result_column=1, date_column=1):
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
    results = array.array('i', [])

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
            if isDate(A[date_column]):
                date = parse(A[date_column])
            else:
                raise ValueError
                sys.exit(3)
            results.append(int(A[result_column]))
            if _date is None:
                _date = date
                continue
            delta_date = date - _date
            if delta_date.days == 1 or delta_date.days == 0:
                _date = date
            else:
                raise ValueError
                sys.exit(2)

    f.close()

    return results


def open_file(file_name):
    '''
    Will try to open a file with the given file
    name and handles exceptions that may occur.
    '''
    try:
        f = open(file_name, 'r')
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
        delta = x - last_x
        results.append(delta)
        last_x = x

    return results


def running_average(data, window_size=5):
    '''
    Takes in an array of data then scans and averages the
    values of that array based on the provided window size.
    '''
    results = []
    average = 0
    if data is None:
        print('No data passed to running_average')
        sys.exit(3)
    try:
        data[window_size]
    except IndexError:
        print('Updating window_size from ' + str(window_size) +
              ' to ' + str(len(data)))
        window_size = len(data)
        return np.mean(data), window_size

    for i in range(len(data)-window_size+1):
        results.append(np.mean(data[i:i+window_size]))

    return results, window_size


def handle_result_column(result_column, line):
    '''
    Converts a string result_column to the corresponding
    integer ID of that column if it exists.
    '''
    A = line.rstrip().split(',')
    if isinstance(result_column, str):
        try:
            result_column = A.index(result_column)
        except ValueError:
            print('result_column_str was assigned as ' + result_column
                  + ' and is out of range. '
                  + 'Available result columns are '
                  + str(A))
            sys.exit(4)
    return result_column


def is_date(string, fuzzy=False):
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
