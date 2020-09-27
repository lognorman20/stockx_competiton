# StockX Sneaker Price Prediction Project

The purpose of this project is to predict the resale price of a sneaker based on several factors like the type of sneaker and buyer region.

![GitHub last commit](https://img.shields.io/github/last-commit/lognorman20/stockx_competiton)
![GitHub issues](https://img.shields.io/github/issues-raw/lognorman20/stockx_competiton)
![GitHub pull requests](https://img.shields.io/github/issues-pr/lognorman20/stockx_competiton)
![GitHub](https://img.shields.io/github/license/lognorman20/stockx_competiton)

## Demo
![Demo](https://github.com/lognorman20/stockx_competiton/visualizations/demo.gif)

## Table of Contents
- [Title](#stockx-sneaker-price-prediction-project)
- [Demo-Preview](#demo-preview)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contribute](#contribute)
    - [Sponsor](#sponsor)
    - [Adding new features or fixing bugs](#adding-new-features-or-fixing-bugs)
- [License](#license)
- [Footer](#footer)

## Getting Started

### Installation

Create a blank Anaconda environment + install the requirements file.
```bash
# Creates new environment called 'stockx-env'
conda create -n stockx-env python=3.7
# Activates the environment we just made
conda activate stockx-env
# Install the requirements
pip install -r requirements.txt
```

### Run the flask app

Make sure to run the app from the `Application/` directory.
```bash
cd Application
python app.py
```
## Data
### Description of the data from StockX

"The data we’re giving you consists of a random sample of all Off-White x Nike and Yeezy 350 sales from between 9/1/2017 (the month that Off-White first debuted “The Ten” collection) and the present. There are 99,956 total sales in the data set; 27,794 Off-White sales, and 72,162 Yeezy sales. The sample consists of U.S. sales only.

To create this sample, we took a random, fixed percentage of StockX sales (X%) for each colorway, on each day, since September 2017. So, for each day the Off-White Jordan 1 was on the market, we randomly selected X% of its sale from each day. (It’s not important to know what X is; all that matters is that it’s a random sample, and that the same fixed X% of sales was selected from every day, for every sneaker). Every row in the spreadsheet represents an individual StockX sale. There are no averages or order counts; this is just a random sample of daily sales data."

