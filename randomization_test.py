"""CSC110 Fall 2021 Final Project: Randomization test

Description
===============================
This file is used to apply randomization teston to the mean of Canadian unemployment rate,
number of total crime, number of money-related crime before and after COVID-19 breakout
in Canada (January 2020). Produce graphs of the sampling distributions and calculates p-value.

Copyright
===============================
This file is Copyright (c) 2021 Chen Jiang, Jiahao Gu,
Xavier Quan, Yufei Liu (Alphabetically Ordered)
"""
import random
import matplotlib.pyplot as plt
from data_conversion import clean_data

CLEANED = clean_data()
REPETITIONS = 1000
NUMTRUE = len([1 for d in CLEANED if d.is_covid])


def calculate_p_value(simulated_value: list[str], test_sta: float, repetitions: int) -> float:
    """Return the calculated p-value with given simulated values, test statistics and repetitions
    """
    lst_more_extreme = [x for x in simulated_value if abs(float(x)) >= abs(test_sta)]
    return len(lst_more_extreme) / repetitions


def mean_diff_of_unemployment_rate() -> float:
    """Apply randomization test to the mean of Canadian unemployment rate before and after
    COVID-19 breakout in Canada (January 2020). Produce a graph of the sampling distribution
    and return the calculated p-value.
    """
    sta_list_true = [a.unemployment_rate for a in CLEANED if a.is_covid]
    sta_list_false = [b.unemployment_rate for b in CLEANED if not b.is_covid]
    test_sta = sum([float(c) for c in sta_list_true]) / len(sta_list_true) - \
        sum([float(c) for c in sta_list_false]) / len(sta_list_false)
    simulated_value = ['' for _ in range(REPETITIONS)]

    for i in range(REPETITIONS):
        dictionary = {}
        lst = list(range(len(CLEANED)))
        for y in CLEANED:
            x = random.choice(lst)
            lst.remove(x)
            dictionary[x] = y
        for x in dictionary:
            if x <= NUMTRUE:
                dictionary[x].is_covid = True
            else:
                dictionary[x].is_covid = False
        list_true = [dictionary[d].unemployment_rate for d in dictionary if dictionary[d].is_covid]
        list_false = [dictionary[e].unemployment_rate for e in dictionary
                      if not dictionary[e].is_covid]
        mean_true = sum([float(f) for f in list_true]) / len(list_true)
        mean_false = sum([float(g) for g in list_false]) / len(list_false)
        diff_mean = mean_true - mean_false
        simulated_value[i] = diff_mean

    for x in CLEANED:
        if x.n < 11:
            x.is_covid = False
        else:
            x.is_covid = True

    plt.hist(simulated_value)
    plt.axvline(-test_sta, color='red')
    plt.axvline(test_sta, color='red')
    plt.xlabel('Mean difference')
    plt.ylabel('Count')
    plt.title('mean difference of Unemployment rate')

    return calculate_p_value(simulated_value, test_sta, REPETITIONS)


def mean_diff_of_n_total_crime() -> float:
    """Apply randomization test to the mean of number of total crime in Canada
    before and after COVID-19 breakout in Canada (January 2020). Produce a graph of
    the sampling distribution and return the calculated p-value.
    """
    sta_list_true = [a.n_total_crime for a in CLEANED if a.is_covid]
    sta_list_false = [b.n_total_crime for b in CLEANED if not b.is_covid]
    test_sta = sum([float(c) for c in sta_list_true]) / len(sta_list_true) - \
        sum([float(c) for c in sta_list_false]) / len(sta_list_false)
    simulated_value = ['' for _ in range(REPETITIONS)]

    for i in range(REPETITIONS):
        dictionary = {}
        lst = list(range(len(CLEANED)))
        for y in CLEANED:
            x = random.choice(lst)
            lst.remove(x)
            dictionary[x] = y
        for x in dictionary:
            if x <= NUMTRUE:
                dictionary[x].is_covid = True
            else:
                dictionary[x].is_covid = False
        list_true = [dictionary[d].n_total_crime for d in dictionary if dictionary[d].is_covid]
        list_false = [dictionary[e].n_total_crime for e in dictionary
                      if not dictionary[e].is_covid]
        mean_true = sum([float(f) for f in list_true]) / len(list_true)
        mean_false = sum([float(g) for g in list_false]) / len(list_false)
        diff_mean = mean_true - mean_false
        simulated_value[i] = diff_mean

    for x in CLEANED:
        if x.n < 11:
            x.is_covid = False
        else:
            x.is_covid = True

    plt.hist(simulated_value)
    plt.axvline(-test_sta, color='red')
    plt.axvline(test_sta, color='red')
    plt.xlabel('Mean difference')
    plt.ylabel('Count')
    plt.title('mean difference of number of total crimes')

    return calculate_p_value(simulated_value, test_sta, REPETITIONS)


def mean_diff_of_n_money_crime() -> float:
    """Apply randomization test to the mean of number of money-related crime in Canada
    before and after COVID-19 breakout in Canada (January 2020). Produce a graph of
    the sampling distribution and return the calculated p-value.
    """
    sta_list_true = [a.n_money_related_crime for a in CLEANED if a.is_covid]
    sta_list_false = [b.n_money_related_crime for b in CLEANED if not b.is_covid]
    test_sta = sum([float(c) for c in sta_list_true]) / len(sta_list_true) - \
        sum([float(c) for c in sta_list_false]) / len(sta_list_false)
    simulated_value = ['' for _ in range(REPETITIONS)]

    for i in range(REPETITIONS):
        dictionary = {}
        lst = list(range(len(CLEANED)))
        for y in CLEANED:
            x = random.choice(lst)
            lst.remove(x)
            dictionary[x] = y
        for x in dictionary:
            if x <= NUMTRUE:
                dictionary[x].is_covid = True
            else:
                dictionary[x].is_covid = False
        list_true = [dictionary[d].n_money_related_crime for d in dictionary
                     if dictionary[d].is_covid]
        list_false = [dictionary[e].n_money_related_crime for e in dictionary
                      if not dictionary[e].is_covid]
        mean_true = sum([float(f) for f in list_true]) / len(list_true)
        mean_false = sum([float(g) for g in list_false]) / len(list_false)
        diff_mean = mean_true - mean_false
        simulated_value[i] = diff_mean

    for x in CLEANED:
        if x.n < 11:
            x.is_covid = False
        else:
            x.is_covid = True

    plt.hist(simulated_value)
    plt.axvline(-test_sta, color='red')
    plt.axvline(test_sta, color='red')
    plt.xlabel('Mean difference')
    plt.ylabel('Count')
    plt.title('mean difference of number of money-related crimes')

    return calculate_p_value(simulated_value, test_sta, REPETITIONS)


# if __name__ == '__main__':
#     import python_ta
#     python_ta.check_all(config={
#         'extra-imports': ["random", "matplotlib.pyplot", "data_conversion"],
#         'allowed-io': [],
#         'max-line-length': 100,
#         'disable': ['R1705', 'C0200']
#     })
