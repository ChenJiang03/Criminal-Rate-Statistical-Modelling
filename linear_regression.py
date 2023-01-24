"""CSC110 Fall 2021 Final Project: Linear Regression

Description
===============================
This file is used to
Create linear regression model between five relationships, including the relationship
between covid and total crime number, covid and money related crime number, covid and
unemployment rate, unemployment rate and total crime number, unemployment rate and
money related crime number. Within the linear regression model, we calculate the intercept,
slope of each linear regression, visualize each relationship and make predictions for the future
with the regression model we have built.

Copyright
===============================
This file is Copyright (c) 2021 Chen Jiang, Jiahao Gu,
Xavier Quan, Yufei Liu (Alphabetically Ordered)
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from data_conversion import clean_data


def total_crime_1() -> list:
    """
    return a list that contains total crime numbers
    """
    data = clean_data()
    total_crime = []
    for d in data:
        total_crime.append(int(d.n_total_crime))
    return total_crime


def money_crime_1() -> list:
    """
    return a list that contains total money related crime numbers
    """
    data = clean_data()
    money_crime = []
    for d in data:
        money_crime.append(d.n_money_related_crime)
    return money_crime


def unemployment_rate_1() -> list:
    """
    return a list that contains unemployment rate
    """
    data = clean_data()
    unemployment_rate = []
    for d in data:
        unemployment_rate.append(float(d.unemployment_rate))
    return unemployment_rate


def period_1() -> list:
    """
    return a list that contains time information as period
    """
    data = clean_data()
    period = []
    for d in data:
        period.append(d.n)
    return period


print("===============relationship between covid and total crime number================")

X = np.array(period_1()).reshape((-1, 1))
Y = np.array(total_crime_1())

MODEL = LinearRegression()

MODEL.fit(X, Y)

R_SQ = MODEL.score(X, Y)

print('coefficient of determination:', R_SQ)

print('intercept:', MODEL.intercept_)

print('slope:', MODEL.coef_)


def lgm_of_covid_and_total_crime_rate() -> None:
    """Draw the linear regression line and
    scatter plot between the covid and the total crime number"""
    plt.scatter(X, Y, color="red")
    plt.plot(X, MODEL.predict(X), color="green")
    plt.title("linear regression model of covid and total crime number")
    plt.xlabel("number of month starts from 2019.3")
    plt.ylabel("crime rate")
    plt.show()


print("===============relationship between covid and money crime rate================")
YM = np.array(money_crime_1())

MODELM = LinearRegression()

MODELM.fit(X, YM)

R_SQ_M = MODELM.score(X, YM)

print('coefficient of determination:', R_SQ_M)

print('intercept:', MODELM.intercept_)

print('slope:', MODELM.coef_)


def lgm_of_covid_and_money_crime_rate() -> None:
    """Draw the linear regression line and
    scatter plot between the covid and the money crime number"""
    plt.scatter(X, YM, color="blue")
    plt.plot(X, MODELM.predict(X), color="orange")
    plt.title("linear regression model of covid and money crime")
    plt.xlabel("number of monthes starts from 2019.3")
    plt.ylabel("money crime rate")
    plt.show()


print("===============relationship between covid and unemployment rate================")
YE = np.array(unemployment_rate_1())

MODELE = LinearRegression()

MODELE.fit(X, YE)

R_SQ_E = MODELE.score(X, YE)

print('coefficient of determination:', R_SQ_E)

print('intercept:', MODELE.intercept_)

print('slope:', MODELE.coef_)


def lgm_of_covid_and_unemployment_rate() -> None:
    """Draw the linear regression line and
    scatter plot between the covid and the unemployment rate"""
    plt.scatter(X, YE, color="black")
    plt.plot(X, MODELE.predict(X), color="brown")
    plt.title("linear regression model of covid and unemployment rate")
    plt.xlabel("number of monthes starts from 2019.3")
    plt.ylabel("unemployment rate")
    plt.show()


print("===============relationship between unemployment rate and crime================")
XE = np.array(unemployment_rate_1()).reshape((-1, 1))
YC = np.array(total_crime_1())

MODEL_EC = LinearRegression()

MODEL_EC.fit(XE, YC)

R_SQ_EC = MODEL_EC.score(XE, YC)

print('coefficient of determination:', R_SQ_EC)

print('intercept:', MODEL_EC.intercept_)

print('slope:', MODEL_EC.coef_)


def lgm_of_unemployment_rate_and_crime() -> None:
    """Draw the linear regression line and
    scatter plot between the unemployment rate and the total crime number"""
    plt.scatter(XE, YC, color="black")
    plt.plot(XE, MODEL_EC.predict(XE), color="brown")
    plt.title("linear regression model of unemployment rate and crime")
    plt.xlabel("unemployment rate")
    plt.ylabel("total crime number")
    plt.show()


print("===============relationship between unemployment rate and money_crime================")

MODEL_EM = LinearRegression()

MODEL_EM.fit(XE, YM)

R_SQ_EM = MODEL_EM.score(XE, YM)

print('coefficient of determination:', R_SQ_EM)

print('intercept:', MODEL_EM.intercept_)

print('slope:', MODEL_EM.coef_)


def lgm_of_unemployment_rate_and_money_crime() -> None:
    """Draw the linear regression line and
    scatter plot between the unemployment rate and the money related crime"""
    plt.scatter(XE, YM, color="orange")
    plt.plot(XE, MODEL_EM.predict(XE), color="red")
    plt.title("linear regression model of unemployment rate and money crime")
    plt.xlabel("unemployment rate")
    plt.ylabel("money crime number")
    plt.show()


def convert_period_to_number(future_year: int, future_month: int) -> int:
    """convert the period the user input to the number of money
    started from the beginning of the pandemic period

    Preconditions:
        - future_year > 2019 or future_month >= 3
    """

    n = 0
    if future_year == 2019:
        for _ in range(3, future_month + 1):
            n = n + 1
    if future_year > 2019:
        n = n + 10
        for _ in range(2020, future_year):
            n = n + 12
        for _ in range(1, future_month + 1):
            n = n + 1
    return n


def predict_future_total_crime(future_year: int, future_month: int) -> float:
    """predict the future total crime based on the time the user input

    Preconditions:
        - future_year > 2019 or future_month >= 3
    """
    p = convert_period_to_number(future_year, future_month)
    pred = MODEL.intercept_ + MODEL.coef_ * p
    return round(float(pred), 2)


def predict_future_money_crime(future_year: int, future_month: int) -> float:
    """predict the future money related crime based on the time the user input
    Preconditions:
        - future_year > 2019 or future_month >= 3
    """
    p = convert_period_to_number(future_year, future_month)
    pred = MODELM.intercept_ + MODELM.coef_ * p
    return round(float(pred), 2)


def predict_future_unemployment_rate(future_year: int, future_month: int) -> float:
    """predict the future unemployment rate based on the time the user input
    Preconditions:
        - future_year > 2019 or future_month >= 3
    """
    p = convert_period_to_number(future_year, future_month)
    pred = MODELE.intercept_ + MODELE.coef_ * p
    return round(float(pred), 2)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ["numpy", "matplotlib.pyplot", "sklearn.linear_model", "data_conversion"],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
