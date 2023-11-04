#!/usr/bin/env python
# coding: utf-8

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
url = ('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN'
       '-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

data = pd.read_csv(url)

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
app.title = "Automobile Statistics Dashboard"

# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]

# List of years
year_list = [i for i in range(1980, 2024, 1)]

# Create the layout of the app
app.layout = html.Div([
    # TASK 2.1 Add title to the dashboard
    html.H1(
        "Automobile Sales Dashboard",
        style={
            "textAlign": "centre",
            "color": "#000000",
        }
    ),

    # TASK 2.2: Add two dropdown menus
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id="dropdown-statistics",
            options=dropdown_options,
            value="Select Statistics",
            placeholder="Select a report type"
        )
    ]),

    html.Div(
        dcc.Dropdown(
            id="select-year",
            options=[{"label": i, "value": i} for i in year_list],
            value='Select Year'
        )
    ),

    # TASK 2.3: Add a division for output display
    html.Div([
        html.Div(
            id='output-container',
            className='chart-grid',
            style={"display": "flex"}
        )
    ]),

    html.Div([], id='plot1'),

    html.Div(
        [
            html.Div([], id='plot2'),
            html.Div([], id='plot3')
        ],
        style={'display': 'flex'}
    ),

    # TASK3: Add a division with two empty divisions inside. See above disvision for example.
    # Enter your code below. Make sure you have correct formatting.
    html.Div([
        html.Div([], id='plot4'),
        html.Div([], id='plot5')
    ],
        style={'display': 'flex'}
    ),
])


# TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value')
)
def update_input_container(selected_statistics):
    return not (selected_statistics == 'Yearly Statistics')


@app.callback(
    Output(component_id='output-container', component_property='children'),
    [
        Input(component_id='dropdown-statistics', component_property='value'),
        Input(component_id='select-year', component_property='value')
    ]
)
def update_output_container(stat_type: str, year):
    if stat_type == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]

        # Plot 1 Automobile sales fluctuate over Recession Period (year wise) using line chart
        # grouping data for plotting
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        # Plotting the line graph
        R_chart1 = dcc.Graph(
            figure=px.line(
                yearly_rec,
                x='........',
                y='........',
                title="........"
            )
        )

    # Plot 2 Calculate the average number of vehicles sold by vehicle type and represent as a Bar chart
    # ...

    # Plot 3 : Pie chart for total expenditure share by vehicle type during recessions
    # grouping data for plotting
    exp_rec = recession_data.groupby(None)
    R_chart3 = dcc.Graph(
        figure=px.pie(None, values='............', names='..........', title="............")
    )

    # Plot 4 Develop a Bar chart for the effect of unemployment rate on vehicle type and sales
    # ...

    return [
        html.Div(
            className='chart-item',
            children=[
                html.Div(children=""),
                html.Div(children="")
            ]
        ),
        html.Div(
            className='chart-item',
            children=[
                html.Div(children="......"),
                html.Div(children="......")
            ]
        )
    ]


# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True)
