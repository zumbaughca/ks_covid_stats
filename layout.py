import dash_html_components as html
import dash_core_components as dcc


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
        html.Label("Data source: The New York Times",
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

    return layout
