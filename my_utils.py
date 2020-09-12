
def get_column(file_name, query_column, query_value, result_column):
    # Create a python list called res which will be populated with an result_column data
    res = []
    
    # Open a file using the provided file name with the optional argument 'r' to open the file as read-only
    f = open(file_name, 'r')
    
    # Skip the header this is boiler-plate when reading files with headers
    header = None
    
    # Loop through each line in file f
    for line in f:
        # Skip the header this is boiler-plate when reading files with headers
        if header is None:
            header = line,
            continue
            
        # Split by ',' then rstrip is used to strip special characters like /n
        A = line.rstrip().split(',')
        
        # Check if the query_column of the current line matches the query_value
        if A[query_column] == query_value:
            # Append the result column data to the res list
            res.append(A[result_column])
            
    return res
