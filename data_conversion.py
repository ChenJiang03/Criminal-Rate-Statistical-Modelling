"""CSC110 Fall 2021 Final Project: Data Conversion

Description
===============================
This file is used to
1. define a class called Data containing aspects that we are interested in within
   a month that is in the dataset.
2. convert two datasets in csv format to a list containing numerous of datatype Data
   that we have defined.

Copyright
===============================
This file is Copyright (c) 2021 Chen Jiang, Jiahao Gu,
Xavier Quan, Yufei Liu (Alphabetically Ordered)
"""
import csv
from dataclasses import dataclass


@dataclass
class Data:
    """An analyzed format of aspects that we are interested in within a month that is in the dataset

    Attributes:
        - n: The number of month past March 2019
        - month: the name of the month and year.
        - is_covid: whether the month in in the period of COVID-19, assuming it started in Canada
          after January 2020.
        - n_total_crime: The total number of crime in that month. Total crime includes all the
          illegal action except total assaults, because it is divided into various sub-crime
          in the data set.
        - n_money_related_crime: The total number of money-related crime in that month.
          Money-related crime includes robbery, shoplifting and Motor vehicle theft.
        - unemployment_rate: The unemployment rate of that month

    Representation Invariants:
        - self.n > 0
        - self.month != ''
        - self.n_total_crime >= 0
        - self.n_money_related_crime >= 0
        - self.unemployment_rate >= 0

    Sample Usage:
    >>> Data(n=1, month='March 2019', is_covid=False, n_total_crime=55487, \
     n_money_related_crime=17148, unemployment_rate=6.3)
    """
    n: int
    month: str
    is_covid: bool
    n_total_crime: int
    n_money_related_crime: int
    unemployment_rate: float


def reformat_crime_data(file: str) -> list[tuple]:
    """Return a list of tuples containing each line after the 9th line from the data in the file
    about the number of crime.

    Preconditions:
        - file is the path to a csv file containing course data about the number of crime.
    """
    with open(file, newline='') as file1:
        reader = csv.reader(file1)
        for _ in range(9):
            next(reader)
        data = list(map(tuple, reader))
    return data


def reformat_unemployment_data(file: str) -> list[tuple]:
    """Return a list of tuples containing each line after the 11st line from the data in the file
    about unemployment rate.

    Preconditions:
        - file is the path to a csv file containing course data about unemployment rate
    """
    with open(file, newline='') as file2:
        reader = csv.reader(file2)
        for _ in range(11):
            next(reader)
        data2 = list(map(tuple, reader))
    return data2


def clean_data() -> list[Data]:
    """Return a list of Data with key information extracted from previously reformatted data.
    """
    cleaned_data = []
    data = reformat_crime_data('crimerate.csv')
    data2 = reformat_unemployment_data('unemploymentrate.csv')
    for x in range(1, 32):
        num = 0
        month = data[0][x]
        for i in range(2, 14):
            num = num + int(''.join(str.split(data[i][x], ',')))
        n_total_crime = num
        x1 = int(''.join(str.split(data[5][x], ',')))
        x2 = int(''.join(str.split(data[9][x], ',')))
        x3 = int(''.join(str.split(data[10][x], ',')))
        n_money_related_crime = x1 + x2 + x3
        unemployment_rate = data2[11][x + 1]
        if x < 11:
            is_covid = False
        else:
            is_covid = True
        crime_data = Data(x, month, is_covid, n_total_crime,
                          n_money_related_crime, float(unemployment_rate))
        cleaned_data.append(crime_data)
    return cleaned_data


# if __name__ == '__main__':
#     import python_ta
#     python_ta.check_all(config={
#         'extra-imports': ["csv", "dataclasses"],
#         'allowed-io': ["reformat_crime_data", "reformat_unemployment_data"],
#         'max-line-length': 100,
#         'disable': ['R1705', 'C0200']
#     })
