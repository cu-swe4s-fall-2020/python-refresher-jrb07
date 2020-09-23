
# Welcome to the python-refresher project

## The purpose of this project is to learn about best practices when using Git and Python with a practical example.

The project executes by running the python script print_cases.py which uses the library my_utils.py to extract desired data from CSV files.

The  example included in this project extracts case data from a CSV file included in COVID-19 data provided by the NYT. 

**To use this project navigate to the main directory and execute the shell file run.sh**

For example execute the command the following command in a terminal 
``` $ bash run.sh```

The data for this project can be found at [NYT Data Repo](https://github.com/nytimes/covid-19-data.git)




Input parameters for print_cases.py can be found below or by running ```$ python print_cases.py -h```

Parameters:
-file_name: string
                    The path to the CSV file
-county: string
                    The name of the county to return data for
-results_column: integer
                    The zero-based index of the column to return
- results_column_str: string
                    The name of the column to return will default to None
-county_column: integer
                    The index of the column with county names

Returns:
-cases: array of ints
              Data extracted from the given CSV file
