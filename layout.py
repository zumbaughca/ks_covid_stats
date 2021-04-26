import dash_html_components as html
import dash_core_components as dcc
import plots
from datasets import Dataset


def create_layout():
    layout = html.Div([
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
                                       {'label': 'Previous 30 days', 'value': 'month'},
                                       {'label': 'Cumulative total', 'value': 'all'}
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
        html.Div([
            html.Label("7 day rolling averages",
                       style={
                           'font-size': 50,
                           'margin-top': '30px'
                       }),
        html.Div([
            dcc.Graph('rolling-cases',
                      figure=plots.create_choropleth(df=Dataset.get_last_day_data(df=Dataset.rolling_avg),
                                                     color_data='cases_avg_per_100k',
                                                     title='Average daily new cases per 100,000 residents'),
                      config={
                          'displayModeBar': None
                      },
                      style={
                          'float': 'left',
                          'width': '50%'
                      }),
            dcc.Graph('rolling-deaths',
                      figure=plots.create_choropleth(df=Dataset.get_last_day_data(df=Dataset.rolling_avg),
                                                     color_data='deaths_avg_per_100k',
                                                     title='Average daily new deaths per 100,000 residents'),
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
                   })
    ],
        style={
            'display': 'block',
            'width': '100%',
            'text-align': 'center'
        })

    return layout
