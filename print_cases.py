"""
Uses user defined parameters to extract
and return data from .csv files

Parameters:
    file_name: string
                    The path to the CSV file
    county: string
                    The name of the county to return data for
    result_column: integer or string
                    The zero-based index or name of the column to return
    county_column: integer
                    The index of the column with county names
    return_daily_increment: boolean
                    Decides whether results are returned as daily increments.
    return_running_avg: boolean
                    Decides whether to return running averages from results
     running_avg_window_size: integer
                    Determines the window size for the running average
Returns:
    results: array
              Data extracted from the given CSV file

"""

import argparse
import my_utils as mu
import sys


def main():
    desc = 'Opens a file and extracts data from a specific column.'

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--file', dest='file_name',
                        type=str,
                        required=True,
                        help='Name of the file to be opened by the script.')

    parser.add_argument('--result_column', dest='result_column',
                        default=4,
                        help='Column of file to be returned by the script.\
                        Defaults to 4 and can be an int or a string name.'
                        )

    parser.add_argument('--county_column', dest='county_column',
                        type=int,
                        required=True,
                        help='Column of file to be queried by the script.')

    parser.add_argument('--county', dest='county',
                        type=str,
                        required=True,
                        help='Name of county to retrieve data from.')

    parser.add_argument('--return_daily_increment',
                        dest='return_daily_increment',
                        type=bool,
                        default=False,
                        help='Decides whether results\
                        are returned as daily increments.')

    parser.add_argument('--return_running_average',
                        dest='return_running_average',
                        type=bool,
                        default=False,
                        help='Decides whether to return\
                        running averages from results.')

    parser.add_argument('--running_avg_window_size',
                        dest='running_avg_window_size',
                        type=int,
                        default=5,
                        help='Determines the window\
                        size for the running average.')

    parser.add_argument('--date_column',
                        dest='date_column',
                        type=int,
                        default=0,
                        help='Determines the date column.')

    args = parser.parse_args()

    print()
    print('Results:')
    if args.return_daily_increment is True:
        try:
            results = get_daily_count(args.file_name,
                                      args.county_column,
                                      args.county,
                                      args.result_column,
                                      args.date_column)
        except ValueError:
            print('ValueError in get daily count', file=sys.stdout)
            print(file=sys.stdout)
            sys.exit(6)
    else:
        try:
            results = get_cases(args.file_name,
                                args.county_column,
                                args.county,
                                args.result_column,
                                args.date_column)
        except ValueError:
            print('ValueError during get cases', file=sys.stdout)
            sys.exit(6)
    if args.return_running_average is True:
        try:
            results, _ = running_average(results,
                                         window_size=args.
                                         running_avg_window_size)
        except ValueError:
            print('ValueError during running average', file=sys.stdout)
            sys.exit(6)
    for result in results:
        print(result)
    print()
    print()


def running_average(data, window_size):
    '''
    Passes user-defined parameters to my_utils.py running_average
    function and returns the results.
    '''
    return mu.running_average(data, window_size)


def get_daily_count(file_name, county_column, county,
                    result_column=4, date_column=1):
    '''
    Passes user-defined parameters to my_utils.py get_daily_count
    function and returns the results.
    '''
    result_column = parse_result_column(result_column)
    return mu.get_daily_count(get_cases(file_name, county_column, county,
                              result_column, date_column))


def get_cases(file_name, county_column, county,
              result_column=4, date_column=1):
    '''
    Passes user-defined parameters to my_utils.py get_column function
    and returns the results.
    '''
    result_column = parse_result_column(result_column)
    return mu.get_column(file_name, county_column, county,
                         result_column, date_column)


def parse_result_column(result_column):
    '''
    Attempts to cast result column as an int.
    '''
    try:
        result_column = int(result_column)
    except ValueError:
        pass
    return result_column


if __name__ == '__main__':
    main()
