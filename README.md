# Project3 - Mapping Food Deserts
Group Project to Map Food Deserts in Georgia

## Project Team (The GAP Team)
1. Ellis Purwanto - Data Visualization and Graphs
2. Marc Avoaka - Database Design
3. Shailesh Godkhindi - Data Analysis, Web Programming and Mapping

## Food Deserts
A Food Desert is an area that has limited access to affordable and nutritious food. Food deserts tend to be inhabited by low-income residents with reduced mobility; this makes them a less attractive market for large supermarket chains. Food deserts lack suppliers of fresh foods, such as meats, fruits, and vegetables. Instead, the available foods are often processed and high in sugar and fats, which are known contributors to the proliferation of obesity in the U.S.

### Beginning the data-gathering process
We found that the Percentage of Free or Reduced Lunches (Percent_FRL) at school is a strong indicator of poverty in an area: https://nces.ed.gov/blogs/nces/post/free-or-reduced-price-lunch-a-proxy-for-poverty

Using this metric, we identified 90 schools across 7 counties of Georgia with Percent_FRL of >= 92%. We collected these school names, physical addresses and the their Percent_FRL in a CSV file.

### Approach
1. Get the name and addresses of all the schools which have the >90% FRL (free-reduced lunch) (%FRL is used as an indicator of poverty).
2. Find out the number of grocery stores within 5-10 miles of these schools (usually people live near the schools and higher percentage FRL means that the neighborhood is poor).
3. Create a Heat Map these grocery stores.
4. Find out any Fast Food joints / Dollar Stores within 5 miles of these locations. Usually in Food Deserts there is proliferation of these establishments selling processed foods.
5. Create a Heat Map these Fast Food places / Dollar Stores.
