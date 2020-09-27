"""Uses argparse parameters to extract
a defined column from a given .csv file

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

    args = parser.parse_args()

    print()
    print('Results:')

    if args.return_daily_increment is True:
        results = get_daily_count(args.file_name,
                                  args.county_column,
                                  args.county,
                                  args.result_column)
    else:
        results = get_cases(args.file_name,
                            args.county_column,
                            args.county,
                            args.result_column)
    if args.return_running_average is True:
        results = running_average(results,
                                  window_size=args.running_avg_window_size)

    for result in results:
        print(result)

    print()
    print()


def running_average(data, window_size):
    return mu.running_average(data, window_size)


def get_daily_count(file_name, county_column, county, result_column=4):
    try:
        result_column = int(result_column)
    except ValueError:
        pass
    return mu.get_daily_count(file_name, county_column, county,
                              result_column)


def get_cases(file_name, county_column, county, result_column=4):
    try:
        result_column = int(result_column)
    except ValueError:
        pass
    return mu.get_column(file_name, county_column, county,
                         result_column)


if __name__ == '__main__':
    main()
