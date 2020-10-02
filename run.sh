pycodestyle print_cases.py
pycodestyle my_utils.py
pycodestyle test_my_utils.py

python print_cases.py --file covid-19-data/us-counties.csv --county_column 1 --result_column cases --county Boulder | head -20 > test.csv
assert_exit_code 1

python test_my_utils.py

sh test_print_cases.sh