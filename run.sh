
pycodestyle print_cases.py

pycodestyle my_utils.py

pycodestyle test_my_utils.py

python print_cases.py --file co-est2019-alldata.csv --county_column 1 --result_column 'COUNTY,POPESTIMATE2010' --county Boulder

python print_cases.py --file covid-19-data/us-counties.csv --county_column 1 --result_column 'date,cases' --county Boulder

python print_cases.py --file covid-19-data/us-counties.csv --county_column 1 --result_column cases --county Boulder --date_column 0 | head -21 > test.csv

python test_my_utils.py

sh test_print_cases.sh
