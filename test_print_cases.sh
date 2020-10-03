test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_for_stderr python print_cases.py --file covid-19-data/us-counties.cs --county_column 1 --result_column cases --county Boulder  --return_running_average True
assert_exit_code 1

run test_for_stderr python print_cases.py --file covid-19-data/us-counties.csv --county_column 1 --result_column casess --county Boulder  --return_running_average True
assert_exit_code 1
