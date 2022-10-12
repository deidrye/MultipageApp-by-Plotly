import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import dash_table, dcc, html
import plotly.express as px
import pandas as pd
import numpy as np
import requests
from app import app


df = pd.read_csv('data\All_Cities_Cleaned.csv')

''' FILTERS '''

options = []
for k in df.columns:
    options.append({'label': k, 'value': k})
columns2show = dcc.Dropdown(
    id='columns2show',
    options=options,
    value=df.columns,
    multi=True
)


''' LAYOUT '''
layout = dbc.Container([
    # HEADER
    dbc.Row([
        html.H4('Таблица данных')
    ],
        style={'margin-bottom': '20px'}),

    # FILTERS
    dbc.Row([
        
        dbc.Col([
            html.Div('Выберите колонки'),
            html.Div(columns2show)
        ],
            width={'size': 3}),
        
    ],
        style={'margin-bottom': '40px'}),


    # CONTENT
    dbc.Row(html.Div(id='data_table'))
], style={'margin-left': '80px',
          'margin-right': '80px',
          'margin-bottom': '80px'})

''' CALLBACKS '''


@app.callback(
    Output(component_id='data_table', component_property='children'),
    Input(component_id='columns2show', component_property='value')
)
def update_table(cols):
   

    tbl = dash_table.DataTable(data=df[cols].head(90).to_dict('row'),
                               columns=[{"name": i, "id": i} for i in df[cols].columns],
                               style_cell={'textAlign': 'right'}
                               )
    table = [html.P('Данные'), tbl]

    return table
