"""CSC110 Fall 2021 Final Project: Data Conversion

Description
===============================
This file is used to
Show a window of buttons that lead to the visualizations of
the models(linear regression and randomization test) we built.

Copyright
===============================
This file is Copyright (c) 2021 Chen Jiang, Jiahao Gu,
Xavier Quan, Yufei Liu (Alphabetically Ordered)
"""
import tkinter as tk
from linear_regression import lgm_of_covid_and_money_crime_rate, \
    lgm_of_covid_and_total_crime_rate, \
    lgm_of_covid_and_unemployment_rate, lgm_of_unemployment_rate_and_crime,\
    lgm_of_unemployment_rate_and_money_crime, predict_future_total_crime, \
    predict_future_money_crime, \
    predict_future_unemployment_rate
import randomization_test as rtest


def show_window() -> None:
    """
    Create the visualization window.
    """
    window = tk.Tk()

    window.title('Visualization Window')

    window.geometry('1080x730')

    window.configure(bg='lightblue')

    show_linear_regression_models(window)

    var1 = tk.StringVar()
    var2 = tk.StringVar()
    var3 = tk.StringVar()

    def mdontc() -> None:
        """
        Show the visualization of the randomization test of the mean difference of number
        of total crime and return the p-value of the test in the label.
        """
        pvalue1 = rtest.mean_diff_of_n_total_crime()
        var1.set(pvalue1)

    def mdomrc() -> None:
        """
        Show the visualization of the randomization test of the mean difference of
        money-related crime and return the p-value of the test in the label.
        """
        pvalue2 = rtest.mean_diff_of_n_money_crime()
        var2.set(pvalue2)

    def mdour() -> None:
        """
        Show the visualization of the randomization test of the mean difference of unemployment rate
        and return the p-value of the test in the label.
        """
        pvalue3 = rtest.mean_diff_of_unemployment_rate()
        var3.set(pvalue3)

    def show_randomizatin_test_models() -> None:
        """
        Create the buttons that lead to the randomization tests that we run.
        """
        tk.Label(window, bg='lightblue', fg='black', font=('Arial', 20),
                 text='Null Hypothesis: There is no difference in the mean of number of total'
                      'crime for months with and without COVID-19.').place(x=10, y=420)
        tk.Label(window, bg='lightblue', fg='black', font=('Arial', 20),
                 text='P-value: ').place(x=850, y=460)
        l1 = tk.Label(window, bg='white', fg='red', font=('Arial', 20), width=10, textvariable=var1)
        l1.place(x=940, y=460)
        b6 = tk.Button(window, text='Mean difference of number of total crime', width=80, height=2,
                       command=mdontc, bg='black', fg='black', font=('Arial', 17))
        b6.place(x=10, y=450)

        tk.Label(window, bg='lightblue', fg='black', font=('Arial', 20),
                 text='Null Hypothesis: There is no difference in the mean of money-related crime '
                      'for months with and without COVID-19.').place(x=10, y=520)
        tk.Label(window, bg='lightblue', fg='black', font=('Arial', 20),
                 text='P-value: ').place(x=850, y=560)
        l2 = tk.Label(window, bg='white', fg='red', font=('Arial', 20), width=10, textvariable=var2)
        l2.place(x=940, y=560)
        b7 = tk.Button(window, text='Mean difference of money-related crime', width=80, height=2,
                       command=mdomrc, bg='black', fg='black', font=('Arial', 17))
        b7.place(x=10, y=550)

        tk.Label(window, bg='lightblue', fg='black', font=('Arial', 20),
                 text='Null Hypothesis: There is no difference in the mean of unemployment rate '
                      'for months with and without COVID-19.').place(x=10, y=620)
        tk.Label(window, bg='lightblue', fg='black', font=('Arial', 20),
                 text='P-value: ').place(x=850, y=660)
        l3 = tk.Label(window, bg='white', fg='red', font=('Arial', 20), width=10, textvariable=var3)
        l3.place(x=940, y=660)
        b8 = tk.Button(window, text='Mean difference of unemployment rate', width=80, height=2,
                       command=mdour, bg='black', fg='black', font=('Arial', 17))
        b8.place(x=10, y=650)

    show_randomizatin_test_models()

    def run_prediction_window() -> None:
        """
        Create the prediction window as a overlap window.
        """
        pre = tk.Toplevel()

        pre.title('Prediction Window')

        pre.geometry('800x600')

        pre.configure(bg='lightblue')

        tk.Label(pre, bg='lightblue', fg='black', font=('Arial', 20),
                 text='The predicted value of future total crime: ').place(x=40, y=40)

        tk.Label(pre, bg='lightblue', fg='black', font=('Arial', 20),
                 text='The predicted value of future money crime: ').place(x=40, y=100)

        tk.Label(pre, bg='lightblue', fg='black', font=('Arial', 20),
                 text='The predicted value of future unemployment rate: ').place(x=40, y=160)

        tk.Label(pre, bg='lightblue', fg='black', font=('Arial', 18),
                 text='Please choose the year and month you want to predict about here '
                      'and click "Generate Output": ').place(x=20, y=250)

        tk.Label(pre, bg='lightblue', fg='black', font=('Arial', 20),
                 text='Month: ').place(x=30, y=350)

        tk.Label(pre, bg='lightblue', fg='black', font=('Arial', 20),
                 text='Year: ').place(x=340, y=350)

        var1 = tk.StringVar()
        l1 = tk.Label(pre, bg='white', fg='red', font=('Arial', 20), width=15, textvariable=var1)
        l1.place(x=500, y=40)

        var2 = tk.StringVar()
        l2 = tk.Label(pre, bg='white', fg='red', font=('Arial', 20), width=15, textvariable=var2)
        l2.place(x=500, y=100)

        var3 = tk.StringVar()
        l3 = tk.Label(pre, bg='white', fg='red', font=('Arial', 20), width=15, textvariable=var3)
        l3.place(x=500, y=160)

        var4 = tk.StringVar()
        var4.set((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
        lb1 = tk.Listbox(pre, listvariable=var4, exportselection=0,
                         height=12, bg='lightgreen', fg='black')
        lb1.place(x=100, y=350)

        var5 = tk.StringVar()
        var5.set((2019, 2020, 2021, 2022, 2023, 2024))
        lb2 = tk.Listbox(pre, listvariable=var5, exportselection=0, height=6,
                         bg='lightgreen', fg='black')
        lb2.place(x=400, y=350)

        def print_selection() -> None:
            """
            command to show the prediction
            """
            month = lb1.get(lb1.curselection())
            year = lb2.get(lb2.curselection())
            total_crime = predict_future_total_crime(year, month)
            money_crime = predict_future_money_crime(year, month)
            unemployment_rate = predict_future_unemployment_rate(year, month)
            var1.set(total_crime)
            var2.set(money_crime)
            var3.set(unemployment_rate)

        b1 = tk.Button(pre, text='Generate \n output', width=10, height=12, command=print_selection,
                       bg='black', fg='black', font=('Arial', 17))
        b1.place(x=650, y=300)

    run_prediction_window()

    window.mainloop()


def show_linear_regression_models(window: tk.Tk) -> None:
    """
    Create the buttons that lead to the linear regression models that we built.
    """
    b1 = tk.Button(window, text='Linear regression model of covid and total crime number', width=80,
                   height=2, command=lgm_of_covid_and_total_crime_rate, bg='black', fg='black',
                   font=('Arial', 17))
    b1.place(x=10, y=20)

    b2 = tk.Button(window, text='Linear regression model of covid and money crime number', width=80,
                   height=2, command=lgm_of_covid_and_money_crime_rate, bg='black', fg='black',
                   font=('Arial', 17))
    b2.place(x=10, y=100)

    b3 = tk.Button(window, text='Linear regression model of covid and unemployment rate', width=80,
                   height=2, command=lgm_of_covid_and_unemployment_rate, bg='black', fg='black',
                   font=('Arial', 17))
    b3.place(x=10, y=180)

    b4 = tk.Button(window, text='Linear regression model of unemployment rate and crime', width=80,
                   height=2, command=lgm_of_unemployment_rate_and_crime, bg='black', fg='black',
                   font=('Arial', 17))
    b4.place(x=10, y=260)

    b5 = tk.Button(window, text='Linear regression model of unemployment rate and money crime',
                   width=80, height=2, command=lgm_of_unemployment_rate_and_money_crime, bg='black',
                   fg='black',
                   font=('Arial', 17))
    b5.place(x=10, y=340)


# if __name__ == '__main__':
#     import python_ta
#     python_ta.check_all(config={
#         'extra-imports': ["tkinter", "linear_regression", "ramdomization_test"],
#         'allowed-io': [],
#         'max-line-length': 100,
#         'disable': ['R1705', 'C0200']
#     })
