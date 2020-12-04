test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest


run test_for_stderr python print_cases.py --file covid-19-data/us-counties.cs --county_column 1 --result_column cases --county Boulder --date_column 0
assert_exit_code 1

run test_for_stderr python print_cases.py --file covid-19-data/us-counties.csv --county_column 1 --result_column casess --county Boulder --date_column 0
assert_exit_code 1

run test_for_stderr python print_cases.py --file test.csv --county_column 1 --result_column cases --county Boulder --date_column 2
assert_exit_code 1

run test_for_stderr python print_cases.py --file test_date_disorder.csv --county_column 1 --result_column 'date,cases' --county Boulder --date_column 0
assert_exit_code 1
