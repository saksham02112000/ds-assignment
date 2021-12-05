import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.title = 'Stock Viewer'

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1("Stock Price Trend Analysis", className='title'),
            html.H2("Select a company to view stock"),
            dcc.Dropdown(
                id='stock_dropdown',
                options=[
                    {'label': 'Tata Motors', 'value': 'TATAMOTORS'},
                    {'label': 'Gail', 'value': 'GAIL'},
                    {'label': 'HCLTech', 'value': 'HCLTECH'},
                    {'label': 'Bajaj Finserv', 'value': 'BAJAJFINSV'},
                    {'label': 'Coal India', 'value': 'COALINDIA'},
                    {'label': 'Hero', 'value': 'HEROMOTOCO'},
                    {'label': 'ICICI Bank', 'value': 'ICICIBANK'},
                    {'label': 'Kotak Mahindra Bank', 'value': 'KOTAKBANK'},
                    {'label': 'Reliance', 'value': 'RELIANCE'},
                    {'label': 'Wipro', 'value': 'WIPRO'},
                ],
                value='TATAMOTORS',
                className='dropdown-list'
            )
        ],
            className='text-display'),
        html.Div([
            dcc.Graph(id="stock_price-vs-date",
                      config={
                          'scrollZoom': True,
                          'doubleClick': 'reset',
                      }
                      ),
            html.Div([
                dcc.RangeSlider(
                    id='year_chosen',
                    marks={
                        2011: '2011',
                        2012: '2012',
                        2013: '2013',
                        2014: '2014',
                        2015: '2015',
                        2016: '2016',
                        2017: '2017',
                        2018: '2018',
                        2019: '2019',
                        2020: '2020',
                        2021: '2021',
                        2022: '2022',
                    },
                    min=2011,
                    max=2022,
                    value=[2021, 2022],
                ),
            ])
        ],
            className='graph-display'),
    ],
        className='app',
    ),
    html.Div([
        html.Label("Made by Saksham Srivastava(101903570)", className='footer')
    ])
])

colors = {"background": "#E5ECF6", "text": "#636EFA"}


@app.callback(
    Output('stock_price-vs-date', 'figure'),
    [
        Input('stock_dropdown', 'value'),
        Input('year_chosen', 'value')
    ]
)
def update_figure(stock_selected, year_chosen):
    if stock_selected:
        filename = stock_selected + '.csv'
        data = pd.read_csv(filename)
    else:
        data = pd.read_csv('TATAMOTORS.csv')

    data['Date'] = pd.to_datetime(data['Date'])
    data['Year'] = data['Date'].dt.year
    data.set_index = 'Year'

    data = data[(data['Year'] >= year_chosen[0]) & (data['Year'] <= year_chosen[1])]

    fig = px.line(
        data,
        title=f'{stock_selected} Price Chart',
        x='Date',
        y='High',
        labels={
            'High': 'Price'
        }
    )
    fig.update_layout(
        paper_bgcolor=colors["background"],
        font_color=colors["text"]
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=False, host='0.0.0.0', port=8000)
