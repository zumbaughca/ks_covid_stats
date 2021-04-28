import pandas as pd
import plotly.express as px

def create_choropleth(df: pd.DataFrame, color_data, title):
    fig = px.choropleth(data_frame=df, locations=df.index,
                        geojson=df.geometry,
                        color=color_data,
                        labels={'new_cases': 'Cases',
                                'new_deaths': 'Deaths',
                                'cases': 'Cases',
                                'deaths': 'Deaths',
                                'cases_avg_per_100k': 'Daily cases per 100k',
                                'deaths_avg_per_100k': 'Daily deaths per 100k'})
    fig.update_geos(fitbounds='locations')
    fig.update_layout(dragmode=False,
                      title={
                          'text': title,
                          'x': 0.5
                      },
                      font=dict(
                          size=18
                      ))
    if color_data == 'cases_avg_per_100k':
        fig.update_layout(coloraxis_colorbar=dict(
            title='Cases'
        ))
    elif color_data == 'deaths_avg_per_100k':
        fig.update_layout(coloraxis_colorbar=dict(
            title='Deaths'
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
        title = "Total " + value
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