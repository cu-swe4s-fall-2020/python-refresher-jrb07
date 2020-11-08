
pycodestyle print_cases.py

pycodestyle my_utils.py

pycodestyle test_my_utils.py

pycodestyle hash_table.py

pycodestyle test_hash_table.py

python print_cases.py --file test_pop_data.csv --county_column 1 --result_column '4,9' --county Boulder

python print_cases.py --file covid-19-data/us-counties.csv --county_column 1 --result_column 'date,cases' --county Boulder

python print_cases.py --file covid-19-data/us-counties.csv --county_column 1 --result_column cases --county Boulder --date_column 0 | head -21 > test.csv

python test_my_utils.py

sh test_print_cases.sh
