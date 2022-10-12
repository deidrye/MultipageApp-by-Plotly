import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import home, table, dataDescription,scatter,diagrams,hist,boxplot

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink('Диаграмма рассеивания',
                                active=True,
                                href='scatter',
                                style={'text-decoration': 'none',
                                       'color': 'black'})),
        dbc.NavItem(dbc.NavLink('Столбчатые диаграммы',
                                active=True,
                                href='diagrams',
                                style={'text-decoration': 'none',
                                       'color': 'black'})),
        
        dbc.NavItem(dbc.NavLink('Бокса-Вискера',
                                active=True,
                                href='boxplot',
                                style={'text-decoration': 'none',
                                       'color': 'black'})),
        dbc.NavItem(dbc.NavLink('Гистограмма',
                                active=True,
                                href='hist',
                                style={'text-decoration': 'none',
                                       'color': 'black'})),
        
        dbc.NavItem(dbc.NavLink('Табличные данные',
                                href='table',
                                style={'text-decoration': 'none',
                                       'color': 'black'})),
        dbc.NavItem(dbc.NavLink('Описание данных',
                                href='dataDescription',
                                style={'text-decoration': 'none',
                                       'color': 'black'})),
    ],
    brand=" Цены на аренду жилплощади в мегаполисах Индии ",
    brand_href='home',
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(navbar, style={'margin-bottom': '30px'}),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return home.layout
    if pathname == '/hist':
        return hist.layout    
    elif pathname == '/table':
        return table.layout
    elif pathname == '/dataDescription':
        return dataDescription.layout
    elif pathname == '/diagrams':
        return diagrams.app.layout
    elif pathname == '/scatter':
        return scatter.layout
    elif pathname == '/boxplot':
        return boxplot.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)