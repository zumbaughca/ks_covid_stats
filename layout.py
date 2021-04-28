import datetime

import dash_html_components as html
import dash_core_components as dcc
import plots
from datasets import Dataset
from datasets import Data


def create_layout():
    layout = html.Div([
        html.Div(
            html.H1('Kansas COVID Stats',
                       style={
                           'font-size': 70
                       }),
            style={
                'position': 'static',
                'width': '100%',
                'text-align': 'center',
                'margin-bottom': '40px'
            }
        ),
        html.Div([
            html.Div([
                html.Label('New Cases',
                           style={'display': 'block',
                                  'font-size': '40px'}),
                html.Label(Data.read_state_rolling().cases.iloc[-1],
                           style={
                               'font-size': '40px'
                           })
            ],
                style={
                    'border': '1px solid',
                    'border-radius': '15px',
                    'width': '325px',
                    'display': 'inline-block',
                    'margin-right': '50px',
                    'background-color': '#000080',
                    'color': '#FFFFFF'
                }),
            html.Div([
                html.Label('New Deaths',
                           style={'display': 'block',
                                  'font-size': '40px'}),
                html.Label(Data.read_state_rolling().deaths.iloc[-1],
                           style={
                               'font-size': '40px'
                           })
            ],
                style={
                    'border': '1px solid',
                    'border-radius': '15px',
                    'width': '325px',
                    'display': 'inline-block',
                    'margin-left': '50px',
                    'background-color': '#000080',
                    'color': '#FFFFFF'
                })
        ],
            style={
                'margin': '50px'
            }),
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
                                       {'label': 'Previous 30 days', 'value': 'month'},
                                       {'label': 'Cumulative total', 'value': 'all'}
                                   ],
                                   clearable=False,
                                   value='month',
                                   style={'width': '300px'})
                      ],
                     style={'display': 'inline-block',
                            'margin': 'auto',
                            'margin-bottom': '25px'}),
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
                       'width': '100%'})
        ],
        style={
            'margin': '10px'
        }),
        html.Div([
            html.H2("7 day rolling averages",
                       style={
                           'font-size': 50,
                           'margin-top': '30px',
                           'margin-bottom': '20px'
                       }),
        html.Div([
            dcc.Graph('rolling-cases',
                      figure=plots.create_choropleth(df=Dataset.get_last_day_data(df=Dataset.county_rolling_avg),
                                                     color_data='cases_avg_per_100k',
                                                     title='Cases per 100,000 residents'),
                      config={
                          'displayModeBar': None
                      },
                      style={
                          'float': 'left',
                          'width': '50%'
                      }),
            dcc.Graph('rolling-deaths',
                      figure=plots.create_choropleth(df=Dataset.get_last_day_data(df=Dataset.county_rolling_avg),
                                                     color_data='deaths_avg_per_100k',
                                                     title='Deaths per 100,000 residents'),
                      config={
                          'displayModeBar': None
                      },
                      style={
                          'float': 'right',
                          'width': '50%'
                      })
        ],
        style={
            'position': 'relative',
            'display': 'inline-block',
            'width': '100%'
        })],
            style={
                'display': 'block',
                'width': '100%',
                'text-align': 'center'
            }
        ),
        html.Label("Data source: The New York Times",
                   style={
                       'font-size': 24,
                       'float': 'right',
                       'margin': '30px',
                       'margin-top': '100px'
                   }),
        html.Label("Last updated: " + datetime.datetime.today().strftime("%m-%d-%Y"),
                   style={
                       'font-size': 24,
                       'float': 'right',
                       'margin': '30px',
                       'margin-top': '100px'
                   })
    ],
        style={
            'position': 'relative',
            'top': '0%',
            'display': 'block',
            'width': '100%',
            'height': '100%',
            'text-align': 'center'
        })

    return layout
