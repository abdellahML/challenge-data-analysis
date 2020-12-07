# Data analysis
## Context

This project is the continuation of the scraping project.  
In this previous project, we scrapded the [immoweb.be](https://www.immoweb.be/fr?gclid=CjwKCAiAwrf-BRA9EiwAUWwKXsUT4YQfghNwPgEK8S_-LnlVDhbQAF_8WqyEJRGYyieUBOEcm-DZlxoC_rEQAvD_BwE) website.
You can find the details of this previous project [here](https://github.com/Ezamey/challenge-collecting-data).

## Description

In this project we clean, analyse and interpret the data from the immoweb website.  
You can find the [challenge-data-analysis.pdf](challenge-data-analysis.pdf) with some explanations of the results, but you can have more visualization if you run the files by yourself.  

## Usage

The files to run is the `interpretation.ipynb` and the `abdellah.ipynd`.

The first is about some questions about the belgian real estate market.
In this file, the dataset is cleaned, you can see the correlation matrix and the visualization for the best and worst region, province and cities.

The second is more about the analysis of the datas.
It shows the correlation matrix between our datas and analyse the links between them.

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
