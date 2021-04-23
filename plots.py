import pandas as pd
import plotly.express as px

def create_choropleth(df: pd.DataFrame, values, time):
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
    fig = px.choropleth(data_frame=df, locations=df.index,
                        geojson=df.geometry,
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


def create_scatter(df: pd.DataFrame, value, time):
    response = 'new_monthly_cases'
    dataset = df
    y_label = value.capitalize()
    title = "Cumulative " + value + " over 30 days"
    if value == 'deaths':
        response = 'new_monthly_deaths'
    if time == 'all':
        title = "Cumulative " + value + " since March 7, 2020"
        if value == 'cases':
            response = 'cases'
        else:
            response = 'deaths'

    fig = px.scatter(data_frame=dataset,
                     x=dataset.index,
                     y=dataset[response],
                     template="simple_white")
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