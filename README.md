Portfolio Crisis Analyzer
The application was created for users looking to diversify their portfolio into sectors with low sensitivity to critical events such as Wars/Invasions, Economic Recessions and International Health Crisis(Eg. Covid). The programs allows users to enter their asset percentage allocation in 5 major financial sectors. Subsequently, they are provided with a customized analysis of the portfolio during periods of high market volatility. Lastly,the system returns a list of optimal portfolio allocations for each historical event. This with the intend of helping the average investor protecting their capital against periods of large financial distress.​

#Technologies This application is written in python 3.9.7 with the modules below;

fire - For the command line interface, help page, and entrypoint.

questionary - For interactive user prompts and dialogs

#Installation Guide Please install pandas and numpy modules to your python.

pip install pandas

pip install numpy

import matplotlib.pyplot as plt

import sys

import time

import datetime

import yfinance as yf

from yahoo_fin.stock_info import get_data

#Review

Data frame and portfolio weight requested from user are combined in calculations such as daily and annual returns, standart and annual deviations, sharp ratios, cumulative returns, weighted cumulative portfolio returns.

The program starts by launching a Command Line Interface or questionnaire which ask users to enter their current portfolio allocation in 5 sectors as percentages (Stocks, Real Estate, Precious Metals, Fixed Income, & Commodities) Please use 2 digits to enter percentages Eg 20, 20, 10,25, 25. image.png

Application utilizes historical data(from API) to calculate user's portfolio performance during the following events:​9/11 (2001) ​Iraq Invasion(2003)​Economic Recession(2008)​Covid19(2020) ​Russia/Ukraine conflict(2022) Application provides users with optimal portfolio allocation for each of the 5 events covered.

New filtered and coverted datas are plotted in graph via matplotlib and hvplot libraries.

#Contributors BARIS HALIFEOGLU HUANG KAI DANIEL CHA JAVIER
