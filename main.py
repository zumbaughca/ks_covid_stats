from datasets import Dataset
from helpers import DataHelpers
import plotly.express as px
import pandas as pd
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

current_data = Dataset.get_last_day_data()
month_sum_data = Dataset.get_aggregate_sum()
total_sum_data = Dataset.get_total_sum_data()
month_county = Dataset.get_sum_by_county()


app = Dash(__name__, title="Kansas COVID Stats")
server = app.server

"""
    HTML Layout:
    <main div>
        <direction label></>
        <dropdown div   style = inline block>
            <cummulative or new dropdown></>
            <cases or deaths dropdown></>
        </dropdown div>
        <graph div style = inline block>
            <map div style = block>
                <map label></>
                <choropleth map></>
            </map div>
            <scatter plot div>
                <scatter plot label></>
                <scatter plot></>
            </scatter plot div>
        </graph div>
    </main div>
"""

app.layout = html.Div([
    html.Div(
        html.Label('Kansas COVID Stats',
                   style={
                       'position': 'relative',
                       'font-size': 70
                   }),
        style={
            'width': '100%',
            'text-align': 'center'
        }
    ),
    html.Div([

        html.Div([dcc.Dropdown(id='case-death-selector',
                               options=[
                                   {'label': 'Cases', 'value': 'cases'},
                                   {'label': 'Deaths', 'value': 'deaths'}
                               ],
                               clearable=False,
                               value='cases',
                               style={'width': '300px'}),
                  dcc.Dropdown(id='day-total-selector',
                               options=[
                                   {'label': 'Cummulative total for last 30 days', 'value': 'month'},
                                   {'label': 'Cummulative total', 'value': 'all'}
                               ],
                               clearable=False,
                               value='month',
                               style={'width': '300px'})
                  ],
                 style={'display': 'inline-block',
                        'margin': 'auto'})
    ], style={'text-align': 'center'}),
    html.Div([
        dcc.Graph('covid-graph', style={'float': 'left',
                                        'width': '50%'},
                  figure={
                      'layout': dict(
                          legend=dict(
                              orientation="h",
                              y=0
                          )
                      )
                  },
                  config={
                      'scrollZoom': False,
                      'displayModeBar': False
                  }
                  ),
        dcc.Graph('trend-graph', style={'float': 'right',
                                        'top': '0%',
                                        'width': '50%'},
                  config={
                      'scrollZoom': False,
                      'doubleClick': False,
                      'displayModeBar': False,
                      'staticPlot': True
                  })
    ],
        style={'display': 'inline-block',
               'width': '100%'}),
    html.Label("Data provided by the New York Times",
               style={
                   'font-size': 24,
                   'float': 'right',
                   'margin': '30px'
               })
],
    style={
        'display': 'block',
        'width': '100%'
    })

@app.callback(
    Output('covid-graph', 'figure'),
    Input('case-death-selector', 'value'),
    Input('day-total-selector', 'value')
)
def create_plot(values, time):
    color_data = 'new_cases'
    title = "30 day average " + values + " per day"
    if values == 'deaths' and time == 'month':
        color_data = 'new_deaths'
    if values == 'deaths' and time == 'all':
        color_data = 'deaths'
    if values == 'cases' and time == 'all':
        color_data = 'cases'
    if time == 'all':
        title = "Total " + values
    fig = px.choropleth(data_frame=month_county, locations=current_data.index,
                        geojson=current_data.geometry,
                        color=color_data,
                        labels={'new_cases': 'Cases',
                                'new_deaths': 'Deaths',
                                'cases': 'Cases',
                                'deaths': 'Deaths'})
    fig.update_geos(fitbounds='locations')
    fig.update_layout(dragmode=False,
                      legend=dict(orientation="h",
                                  yanchor="bottom",
                                  xanchor="left",
                                  y=0,
                                  x=0,
                                  title=""),
                      title={
                          'text': title,
                          'x': 0.5
                      },
                      font=dict(
                          size=18
                      ))

    return fig

@app.callback(
    Output('trend-graph', 'figure'),
    Input('case-death-selector', 'value'),
    Input('day-total-selector', 'value')
)
def create_scatter(value, time):
    response = 'new_monthly_cases'
    dataset = month_sum_data
    y_label = value.capitalize()
    title = "Cumulative " + value + " over 30 days"
    if value == 'deaths':
        response = 'new_monthly_deaths'
    if time == 'all':
        dataset = total_sum_data
        title = "Cumulative " + value + " since March 7, 2020"
        if value == 'cases':
            response = 'cases'
        else:
            response = 'deaths'

    fig = px.scatter(data_frame=dataset,
                     x=dataset.index,
                     y=dataset[response])
    fig.update_layout(
        yaxis_title=y_label,
        xaxis_title="Date",
        title={
            'text': title,
            'x': 0.5
        },
        font=dict(
            size=18
        )
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

