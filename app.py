#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Peter Simeth's basic flask pretty youtube downloader (v1.3)
https://github.com/petersimeth/basic-flask-template
© MIT licensed, 2018-2023
"""

from flask import Flask, render_template, request, redirect, url_for
from tkinter import *
from collections import Counter
import subprocess
import os
import csv
import pandas as pd


DEVELOPMENT_ENV = True


app = Flask(__name__, static_url_path='/static')
app_data = {
    "name": "python-challenge",
    "description": "It's time to put away the Excel sheet and enter the world of programming with Python. In this assignment, you'll use the concepts you've learned to complete two Python challenges, PyBank and PyPoll. Both tasks present a real-world situation where your newly developed Python scripting skills come in handy.",
    "author": "Thay Chansy",
    "html_title": "PyBank and PyPoll Web App",
    "project_name": "python-challenge",
    "keywords": "flask, webapp, python, pybank, pypoll",

}

@app.route("/")
def index():
    return render_template("index.html", app_data=app_data)


@app.route("/about")
def about():
    return render_template("about.html", app_data=app_data)


@app.route("/service")
def service():
    return render_template("service.html", app_data=app_data)


@app.route("/contact")
def contact():
    return render_template("contact.html", app_data=app_data)


@app.route("/pybank")
def pybank():
    total_months = 0
    total_profit_loss = 0
    months = 0
    previous_profit_loss = None  # Track changes
    max_increase = float('-inf')  
    min_decrease = float('inf')  
    max_increase_date = None
    min_decrease_date = None
    previous_profit_loss = 0
    changes = []
    dates = []

    df = pd.read_csv('./budget_data.csv')
    #total_months = len(df)
    total_months = len(df.index)

    with open('./budget_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
  
        for row in csv_reader:
            current_profit_loss = row[1]
            
            #total_months = len(months)
           
            total_profit_loss += round(float(current_profit_loss))

            if previous_profit_loss != 0:
                change = int(row[1]) - previous_profit_loss
                changes.append(change)
                dates.append(row[0])
            previous_profit_loss = int(row[1])

# Find the greatest increase in profits 
    max_increase = max(changes)

# Find the date corresponding to the greatest increase value
    max_increase_date = dates[changes.index(max_increase)]

# Find the greatest decrease in profits
    min_decrease = min(changes)

# Find the date corresponding to the greatest decrease value
    min_decrease_date = dates[changes.index(min_decrease)]

# Calculate average change
    average_change = sum(changes) / len(changes)
    average_change = round(float(average_change),2)
   
    
    data = {
                "dummy": "dummy",
                "total_months": total_months,
                "total_profit_loss": total_profit_loss,
                "average_change": average_change,
                "max_increase_date": max_increase_date,
                "max_increase": max_increase,
                "min_decrease_date": min_decrease_date,
                "min_decrease": min_decrease,

            }
    

    return render_template("pybank.html", app_data = app_data, data=data)

@app.route("/pypoll")
def pypoll():
# Declaring variables
    votes = []
    county = []
    candidates = []
    stockham = []
    deGette = []
    doane = []
    stockham_votes = 0
    deGette_votes = 0
    doane_votes = 0
    total_votes = 0

    df = pd.read_csv('./election_data.csv')
    total = len(df.index)
    
    with open('./election_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
  
        for row in csv_reader:
            votes.append(int(row[0]))
            county.append(row[1])
            candidates.append(row[2])
            

        for candidate in candidates:
            if candidate == "Charles Casper Stockham":
                stockham.append(candidates)
                stockham_votes = len(stockham)
                
            elif candidate == "Diana DeGette":
                deGette.append(candidates)
                deGette_votes = len(deGette)
            
            else:
                doane.append(candidates)
                doane_votes = len(doane)  

            total_votes += 1


    stockham_percent = round(((stockham_votes / total_votes) * 100), 3)
    deGette_percent = round(((deGette_votes / total_votes) * 100), 3)
    doane_percent = round(((doane_votes / total_votes) * 100), 3)
   
    # Winner 
    if stockham_percent > max(deGette_percent, doane_percent):
        winner = "Charles Casper Stockham"
    elif deGette_percent > max(stockham_percent, doane_percent):
        winner = "Diana DeGette"  
    else:
        winner = "Raymon Anthony Doane"


        
    data = {
                "dummy": "dummy",
                "total_votes": total,
                "stockham_votes": stockham_votes,
                "stockham_percent": stockham_percent,
                "deGette_votes": deGette_votes,
                "deGette_percent": deGette_percent,
                "doane_votes": doane_votes,
                "doane_percent": doane_percent,
                "Winner": winner,
            }   
    return render_template("pypoll.html", app_data=app_data, data=data)

if __name__ == "__main__":
    app.run(debug=DEVELOPMENT_ENV)
