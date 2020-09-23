"""Uses argparse parameters to extract
a defined column from a given .csv file

Parameters:
    file_name: string
                    The path to the CSV file
    county: string
                    The name of the county to return data for
    results_column: integer
                    The zero-based index of the column to return
    results_column_str: string
                    The name of the column to return will default to None
    county_column: integer
                    The index of the column with county names

Returns:
    cases: array of ints
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
                        type=int,
                        help='Column of file to be returned by the script. \
                        Defaults to 4 and must be an int use _str for strings.')
    
    parser.add_argument('--result_column_str', dest='result_column_str',
                        default=None,
                        type=str,
                        help='Column of file to be returned by the script. \
                        Defaults to None unless assigned as a string.')


    parser.add_argument('--county_column', dest='county_column',
                        type=int,
                        required=True,
                        help='Column of file to be queried by the script.')

    parser.add_argument('--county', dest='county',
                        type=str,
                        required=True,
                        help='Name of county to retrieve data from.')

    args = parser.parse_args()

    print(get_cases(args.file_name,
                    args.county_column,
                    args.county,
                    args.result_column_str,
                    args.result_column))


def get_cases(file_name, county_column, county, result_column_str=None, result_column=4):
    if result_column_str is None:
        return mu.get_column(file_name, county_column, county, result_column)
    else:
        return mu.get_column(file_name, county_column, county, result_column_str)


if __name__ == '__main__':
    main()
