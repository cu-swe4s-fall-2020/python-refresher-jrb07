"""Contains useful functions for file parsing."""

import array


# TODO: Handle all exceptions gracefully.

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
            # Handle string passed as result_column to index
            if isinstance(result_column, str):
                A = line.rstrip().split(',')
                result_column = A.index(result_column)
            continue

        A = line.rstrip().split(',')

        if A[query_column] == query_value:
            results.append(A[result_column])

    return results
