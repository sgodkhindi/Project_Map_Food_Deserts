# Dependencies
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import requests

#-------------------- RESOURCES --------------------#

# Color Themes
colors = {
    'background': '#3a3f44',
    'text': '#aaa',
    'AgePopBar': ['rgb(255, 125, 125)', 'rgb(255, 114, 151)', 'rgb(255, 102, 183)', 'rgb(255, 91, 221)', 'rgb(246, 80, 255)', 'rgb(196, 68, 255)', 'rgb(140, 57, 255)', 'rgb(78, 45, 255)', 'rgb(34, 58, 255)', 'rgb(23, 109, 255)', 'rgb(11, 166, 255)', 'rgb(0, 229, 255)']
}


# API Pull Census.gov
censusUrl = 'https://api.census.gov/data/2019/pep/charagegroups?get=NAME,POP,AGEGROUP,RACE&for=county:009,063,101,167,185,209,317&in=state:13'
censusRes = requests.get(censusUrl).json()
censusDf = pd.DataFrame(censusRes[1:], columns = censusRes[0])
censusDf = censusDf.astype({'AGEGROUP':'int','POP':'float'})

# Change Race Code to Desc Values
raceDesc = ['Not Specified', 'White', 'African American', 'American Indian', 'Asian', 'Pacific Islander', 'Mixed', 'White or Mixed', 'African American or Mixed', 'American Indian or Mixed', 'Asian or Mixed', 'Pacific Islander or Mixed']
for x in range(12):
    censusDf['RACE'] = np.where(censusDf['RACE'] == str(x), raceDesc[x], censusDf['RACE'])

# Export to CSV
censusDf.to_csv('./Resources/Census_Data.csv', index = False)
censusPath = './Resources/Census_Data.csv'

#-------------------- INITIALIZE --------------------#

# Dash
app = dash.Dash(external_stylesheets = [dbc.themes.SLATE])

# Census Data
censusData = pd.read_csv(censusPath).sort_values(by = 'NAME', ascending = True)

#-------------------- OPTIONS --------------------#

# Dropdown Options
DropOpt = []
counties = censusData['NAME'].unique()
for county in counties:
    countyID = censusData[censusData['NAME'] == county]['county'].values[0]
    DropOpt.append({
        'label': county,
        'value': countyID
    })

#-------------------- APP LAYOUT --------------------#

# Main
app.layout = dbc.Container(
    [
        html.H1('Georgia Food Deserts',
                style = {
                    'textAlign': 'center',
                    'marginTop': 40,
                    'marginBottom': 40
                }),
        html.P('Select a County'),
        dcc.Dropdown(id = 'CountyDrop',
                     options = DropOpt,
                     value = DropOpt[0]['value'],
                     style = {
                        'textAlign': 'center',
                        'marginTop': 40,
                        'marginBottom': 40
                     }
        ),
        html.Hr(),
        dbc.Card(
            [
                # Age Group Population Bar
                html.Div(
                    [
                        html.H1('Age Group Populations',
                                style = {
                                    'textAlign': 'center',
                                    'marginTop': 40,
                                    'marginBottom': 40
                                }),
                        dcc.Graph(id = 'AgePopBar')
                    ]
                )
            ]
        )
        
    ],
    fluid = True
)

#-------------------- CHARTS AND GRAPHS --------------------#

# Make Interactive
@app.callback(Output(component_id = 'AgePopBar',
                     component_property = 'figure'),
              [Input(component_id = 'CountyDrop',
                     component_property = 'value')])

# FUNC: Create Bar Chart showing Age Group Populations
def AgePopBarUpdate(DropVal):
    curCountyData = censusData[censusData['county'] == DropVal]
    filData = curCountyData[(curCountyData['AGEGROUP'] <= 18) & (curCountyData['AGEGROUP'] != 0)].sort_values(by='NAME', ascending=True)
    curCounty = filData['NAME'].array[0]
    fig = px.bar(filData.sort_values(by='RACE', ascending=True),
                 x = "AGEGROUP",
                 y = "POP",
                 color = "RACE",
                 text_auto = False,
                 color_discrete_sequence = colors['AgePopBar'])
    fig.update_layout(title = f'{curCounty} Age Group Populations',
                      xaxis_title = 'Age Group',
                      yaxis_title = 'Population',
                      plot_bgcolor = colors['background'],
                      paper_bgcolor = colors['background'],
                      font_color = colors['text'])
    return fig

#-------------------- FLASK APP --------------------#

# Run Flask Application
if __name__ == '__main__': 
    app.run_server()