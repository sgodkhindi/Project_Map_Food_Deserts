# Project3 - Mapping Food Deserts
### Group Project to Map Food Deserts in Georgia 

## Project Team (The GAP Team)
1. Ellis Purwanto - Data Visualization and Graphs
2. Marc Avoaka - Database Design
3. Shailesh Godkhindi - Data Analysis, Web Programming and Mapping

## Key Deliverables
### Jupyter Notebooks
- [County_Data_Analysis ](Food_Deserts_Data_County.ipynb)
- [Data_Visualization & Graphs](ellisNotebooks/Plotly_Graphs.ipynb)

### Database Components
- [Database_Diagram](SQL/Food_Deserts.png)
- [Database Schema](SQL/Schema.SQL)
- [Database Queries](SQL/queries.sql)

### Web Application
- [Web Application](Webpage/app.py)

## Food Deserts
A Food Desert is an area that has limited access to affordable and nutritious food. Food deserts tend to be inhabited by low-income residents with reduced mobility; this makes them a less attractive market for large supermarket chains. Food deserts lack suppliers of fresh foods, such as meats, fruits, and vegetables. Instead, the available foods are often processed and high in sugar and fats, which are known contributors to the proliferation of obesity in the U.S.

## Development Process
### Beginning the data-gathering process
We found that the Percentage of Free or Reduced Lunches (Percent_FRL) at school is a strong indicator of poverty in an area: https://nces.ed.gov/blogs/nces/post/free-or-reduced-price-lunch-a-proxy-for-poverty

Using this metric and the Per Capita Income data from https://fred.stlouisfed.org/release/tables?eid=266512&rid=175, the team identified 15 counties in GA.

These 15 counties are as follows:
1. Baldwin County
2. Clayton County
3. Cobb County
4. Coffee County
5. Colquitt County
6. DeKalb County
7. Echols County
8. Forsyth County
9. Fulton County
10. Gwinnett County
11. Johnson County
12. Lowndes County
13. Meriwether County
14. Montgomery County
15. Washington County
16. Wilkes County

### Data Analysis Preparation
Once these15 counties were identified the team took the following steps to get all the source data together:
1. List all the 15 counties along with the - Per Capita Income and Percent_FRL
2. Locate the Latitude and Longitude of the County Courthouse for each county. Usually the Courthouse is the centermost point in the county.
3. Create an input file with all this information.
