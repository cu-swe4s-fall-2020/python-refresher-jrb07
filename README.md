
# Welcome to the python-refresher project

## The purpose of this project is to learn about best practices when using Git and Python with a practical example.

The project executes by running the python script print_cases.py which uses the library my_utils.py to extract desired data from CSV files.

The  example included in this project extracts case data from a CSV file included in COVID-19 data provided by the NYT. 

**To use this project navigate to the main directory and execute the shell file run.sh**

For example execute the command the following command in a terminal 
``` $ bash run.sh```

The data for this project can be found at [NYT Data Repo](https://github.com/nytimes/covid-19-data.git)




Input parameters for print_cases.py can be found below or by running ```$ python print_cases.py -h```

Inputs
1. file_name 
    - string 
        - The path to the CSV file
2. county
    - string 
        - The name of the county to return data for
3. results_column(s)
    - integer(s) or string(s)
        - The zero-based index/indices or the name(s) of the column(s) to return
4. county_column
    - integer 
        - The index of the column with county names
5. return_daily_increment 
    - boolean
        - Decides whether results are returned as daily increments.
6. return_running_avg
    - boolean
        - Decides whether to return running averages from results
7. running_avg_window_size 
    - integer
        - Determines the window size for the running average


Returns
1. results
    - array of ints or list of arrays of ints
        - Data extracted from the given CSV file
