
"""Contains useful functions for file parsing."""


def main():
    desc = 'Opens a file and extracts data from a specific column.'

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--file', dest='file_name',
                        type=str,
                        required=True,
                        help='Name of the file to be opened by the script.')

    parser.add_argument('--column', dest='result_column',
                        type=int,
                        required=True,
                        help='Column of file to be returned by the script.')

    parser.add_argument('--max', dest='max_results',
                        type=int,
                        default=10,
                        help='Number of results to return to stdout.')

    args = parser.parse_args()


def get_column(file_name, query_column, query_value, result_column=1):
    """Opens a CSV file and retrieves the desired column data based on inputs
    Inputs:
                file_name = string
                                    The name of the file to open
                query_column = integer
                                    The index of the column to query
                query_value = string
                                    The name of the value to query
                result_colum = integer or string
                                    The index or name of the column to return
    """
    results = []

    f = open(file_name, 'r')

    header = None

    for line in f:
        if header is None:
            header = line,
            # Handle string passed as result_column to index
            if isinstance(result_column, str):
                A = line.rstrip().split(',')
                result_column = A.index(result_column)
            continue

        A = line.rstrip().split(',')

        if A[query_column] == query_value:
            results.append(A[result_column])

    return results


if __name__ == '__main__':
    main()
