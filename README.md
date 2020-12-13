# Data analysis
## Context

This project is the continuation of the scraping project.  
In this previous project, we scrapded the [immoweb.be](https://www.immoweb.be/fr?gclid=CjwKCAiAwrf-BRA9EiwAUWwKXsUT4YQfghNwPgEK8S_-LnlVDhbQAF_8WqyEJRGYyieUBOEcm-DZlxoC_rEQAvD_BwE) website.
You can find the details of this previous project [here](https://github.com/Ezamey/challenge-collecting-data).

## Description

In this project we clean, analyse and interpret the data from the immoweb website.  
You can find the [challenge-data-analysis.pdf](challenge-data-analysis.pdf) with some explanations of the results, but you can have more visualization if you run the files by yourself.  

## Usage

You have to run the `interpretation.ipynb` file, import the function `abdellah` from `Main_abdellah.py`and run it.

The first is about some questions related to the belgian real estate market.
The dataset is cleaned. You can see the correlation and the visualization of the most and less expensive region, province and cities, respectively.

The second contains the analysis of the data.
For the qualitative data and the quantitative data, the correlation between variables, between variables and the target variable are calculated and displayed.
An individual and an overall data analysis is done to collect relevant informations, 

## The most explanatory variables based on this data analysis
the property's price, the number of rooms,the construction year, the flanders region localisation and the wallonia region localisation variables are the most influential based on their individual correlation with the target variable, the price per square meter variable.


## Python Libraries

The needed libraries are in the requirement.txt. To install it, use the command below:  

`python -m pip install -r requirements.txt`  

We use pandas for cleaning the data, and seaborn and matplotlib to display these datas.

*Links to the official documentation of libraries :*
- [Pandas](https://pandas.pydata.org/docs/reference/index.html#api)  
- [Seaborn](http://seaborn.pydata.org/api.html)   
- [Matplotlib](https://matplotlib.org/)


  
-----
### Authors

*Axelle Paquet, junior AI developer at BeCode;*

*Abdellah El Ghibzouri, junior AI developer at BeCode;*

*Melvin Leroy, junior AI developer at BeCode.*
