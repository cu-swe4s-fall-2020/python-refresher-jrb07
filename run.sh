pycodestyle print_cases.py
pycodestyle my_utils.py
pycodestyle test_my_utils.py

python print_cases.py --file covid-19-data/us-counties.csv --county_column 1 --result_column cases --county Boulder | head -21 > test.csv

python test_my_utils.py

sh test_print_cases.sh