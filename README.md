# Kansas COVID Stats

This is currently a work in progress and the accuracy of data is not guranteed. The goal of this project is to provide concise COVID case and death incidents in Kansas.

# Table of contents
* [Data Source](#Data-Source)
* [30 Day Data](#30-day-data)
* [Cumulative Data](#cumulative-data)


# Data Source
The datasets used in this project have been obtained from [The New York Times](https://github.com/nytimes/covid-19-data). Data used in this project include [us-counties-recent](https://github.com/nytimes/covid-19-data/blob/master/us-counties-recent.csv) and [us-states](https://github.com/nytimes/covid-19-data/blob/master/us-states.csv). As stated by The New York Times, the data may not present the full picture of the pandemic in Kansas. 

# 30 Day Data
Data for the previous 30 days (beginning the day prior to accessing the site) are provided for both cases and deaths. The choropleth map presents the average number of cases/deaths per day over the 30 day period. It is calculated by averaging the daily number of cases/deaths over that time period for the whole state. The scatter plot depicts the change in cases/deaths over that period. The baseline, 30 days prior, is set at zero and future dates are the change from baseline. When making interpretations it is important to keep the context (scale) in mind.

# Cumulative Data
Cumulative data can be viewed on the county level (choropleth map) or statewide. County level data are presented as the total number of cases/deaths reported since the start of the pandemic. Statewide data are presented in the scatter plot and represent the total number of cases/deaths reported in Kansas at that time since the pandemic started. It is important to remember that the data do not represent the number of active cases, which is considerably lower than the cumulative data and likely the 30 day data as well. That said, in conjunction these should paint a picture of the current status of COVID in Kansas. 
