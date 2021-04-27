from datasets import Dataset
from dash import Dash
from dash.dependencies import Input, Output
import plots
import layout

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

app.layout = layout.create_layout()


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
    return plots.create_choropleth(df=month_county, color_data=color_data, title=title)


@app.callback(
    Output('trend-graph', 'figure'),
    Input('case-death-selector', 'value'),
    Input('day-total-selector', 'value')
)
def create_scatter(value, time):
    if time == 'all':
        return plots.create_scatter(df=total_sum_data, value=value, time=time)
    else:
        return plots.create_scatter(df=month_sum_data, value=value, time=time)



if __name__ == '__main__':
    app.run_server(debug=True)

