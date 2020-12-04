import my_utils
import argparse
from operator import itemgetter
import sys
import argparse


def get_rates(state):
    '''
    This function will return the rate of covid 19 cases in a given state
    '''
    case_file = 'covid-19-data/us-counties.csv'
    query_column = 2
    query_value = state
    result_columns = (0, 1, 4)
    target_date = '2020-11-02'
    result = my_utils.get_columns(case_file,
                                  query_column,
                                  query_value,
                                  result_columns, 0)
    co_cases = []

    for i in range(len(result[0])):
        co_cases.append([result[0][i], result[1][i], result[2][i]])

    population_file = 'co-est2019-alldata.csv'
    query_column = 5
    result_columns = (6, 7)

    result = my_utils.get_columns(population_file,
                                  query_column,
                                  query_value,
                                  result_columns)
    co_pops = []
    for i in range(len(result[0])):
        co_pops.append([result[0][i], int(result[1][i])])

    co_pops.sort(key=itemgetter(0))

    for co in co_cases:
        query = co[1]
        pop = my_utils.binary_search(query + ' County', co_pops)
        if pop is not None:
            if co[0] == target_date:
                print(co[2]/pop, end=' ')

    return [co_cases, co_pops]


def main():
    desc = 'Opens census data and gets the rates for a specified state.'

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('--state', dest='state',
                        type=str,
                        required=True,
                        help='Name of the state to return values for.')
    
    args = parser.parse_args()
    
    get_rates(args.state)


if __name__ == '__main__':
    main()
