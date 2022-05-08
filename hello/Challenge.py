# This file opens a csv file and visualizes the data per category

import csv
from datetime import datetime

import matplotlib.pyplot as plt

# import the data from the csv file
import numpy as np

# import a library for Linear Regression
from sklearn import linear_model


def visualize(categories, months, incidents, useLog=False):
    # visualize the data
    for category in categories:
        plt.plot(months[category][12:], incidents[category][12:], label=category)

    # add a title
    plt.title('Verkehrsunfälle nach Kategorie')
    # add a label to the x-axis
    plt.xlabel('Monate')
    # add a label to the y-axis
    plt.ylabel('Anzahl')
    # add a legend
    plt.legend()
    if useLog:
        plt.yscale('log')
    # show the plot
    plt.show()


def get_prediction(year, month):
    # get the prediction for the given month
    # the prediction is the average of the last 12 months
    # the year and month are given as integers
    # the return value is a float

    # check if the date is in the data

    pass


def get_month_diff(date1, date2):
    return ((date1.date().year - date2.date().year) * 12) + date1.date().month - date2.date().month


filename = 'data/monatszahlen2112_verkehrsunfaelle.csv'
with open(filename) as f:
    reader = csv.reader(f, delimiter=';')
    data = list(reader)

data_arr = np.array(data)

# create a list of the categories
categories = data_arr[1:, 0]
# remove all duplicates
categories = np.unique(categories)

# remove all elements of data_arr for that the second column isn't "insgesamt"
data_arr = data_arr[data_arr[:, 1] == 'insgesamt']

# create a list of the months per category
months = {}
for category in categories:
    months[category] = data_arr[1:, 3][data_arr[1:, 0] == category]

# create a list of the incidents per category
incidents = {}
for category in categories:
    incidents[category] = data_arr[1:, 4][data_arr[1:, 0] == category]

for category in categories:
    # remove incidents in which monat is "Summe"
    incidents[category] = incidents[category][months[category] != "Summe"]
    # remove months in which monat is "Summe"
    months[category] = months[category][months[category] != "Summe"]

    # remove months in which incident is ''
    months[category] = months[category][incidents[category] != '']
    # remove incidents in which incident is ''
    incidents[category] = incidents[category][incidents[category] != '']

    # convert the incidents to integers
    incidents[category] = incidents[category].astype(int)


month_diff = {}
for category in categories:
    # convert the months to dates using the strptime function
    # add a '/' between the year and the month
    months[category] = [m[:4] + '/' + m[4:] for m in months[category]]
    months[category] = [datetime.strptime(x, '%Y/%m') for x in months[category]]

    # sort the months and incidents by the order of the months
    months[category], incidents[category] = (list(t) for t in zip(*sorted(zip(months[category], incidents[category]))))

zero_date = min(months[categories[0]])
for category in categories:
    # calculate the num of months difference to the zero_date in the category
    month_diff[category] = np.array([get_month_diff(m, zero_date) for m in months[category]])

# visualize(categories, months, incidents, useLog=True)


# forecast the values for:
# Category: 'Alkoholunfälle'
# Type: 'insgesamt
# Year: '2021'
# Month: '01'

# set up a simple linear regression model for the predictions
models = {}
for category in categories:
    models[category] = linear_model.LinearRegression()
    models[category].fit(np.array(month_diff[category]).reshape(-1, 1), incidents[category])


new_type = 'Alkoholunfälle'
new_month = '2021/01'
new_date = datetime.strptime(new_month, '%Y/%m')
months[new_type].append(new_date)
new_month_diff = get_month_diff(new_date, zero_date)

# we use a really simple model that only predicts the mean of the data
# incidents[new_type].append(np.mean(incidents[new_type]))

# convert the new date to the needed format for the model
new_date = np.array([new_month_diff]).reshape(-1, 1)
prediction = models[new_type].predict(new_date)
# prediction = get_prediction(year=)

incidents[new_type].append(prediction)

visualize(categories[0:1], months, incidents)





