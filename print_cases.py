"""
Uses user defined parameters to extract
and return data from .csv files

Parameters:
    file_name: string
                    The path to the CSV file
    county: string
                    The name of the county to return data for
    result_column(s): integer(s) or string(s)
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
    results: array or list of lists
              Data extracted from the given CSV file

"""

import my_utils as mu
import argparse


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
                        Defaults to 4 and must correspond to an index\
                        found in the file.'
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
    results = []
    try:
        args.result_column = int(args.result_column)
    except ValueError:
        pass
    if ',' in args.result_column:
        result_array = []
        for result in args.result_column.split(','):
            result_array.append(str(result))
            args.result_column = result_array
        try:
            results = mu.get_columns(
                args.file_name,
                args.county_column,
                args.county,
                args.result_column,
                args.date_column)
        except ValueError:
            print('ValueError during get columns')
    else:
        try:
            results = mu.get_column(
                args.file_name,
                args.county_column,
                args.county,
                args.result_column,
                args.date_column)
        except ValueError:
            print('ValueError during get column')
    if args.return_daily_increment is True:
        try:
            results = mu.get_daily_count(
                get_cases(
                    args.file_name,
                    args.county_column,
                    args.county,
                    args.result_column,
                    args.date_column))
        except ValueError:
            print('Value Error during get daily increment.')
    if args.return_running_average is True:
        try:
            results, _ = mu.running_average(
                results,
                window_size=args.running_avg_window_size)
        except ValueError:
            print('ValueError during running average')
    for result in results:
        print(result)
    print()
    print()


if __name__ == '__main__':
    main()
