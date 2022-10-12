import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import numpy as np
from app import app
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px



df = pd.read_csv('data\All_Cities_Cleaned.csv')


fig = px.box(df, x='property_type', y='price')
# minplay_bins = [0, 300, 700, 1200]
# minplay_stats = ['little playing time', 'normal playing time', 'a lot of playing time']
# df['minplayStats'] = pd.cut(df['goals'], minplay_bins, labels=minplay_stats)

layout = html.Div([
   dbc.Row([html.H4("Диаграмма Бокса-Вискера", style={'margin-left':'500px'}),
    html.P("x-axis:",style={'margin-left':'500px'}),
    dcc.Checklist(
        id='x-axis',  
        options=['furnish_type','property_type','layout_type', 'city'],
        value=['property_type'], 
        inline=True,style={'margin-left':'500px'}
    ),
    html.P("y-axis:",style={'margin-left':'500px'}),
    dcc.RadioItems(
        id='y-axis', 
        options=['area', 'price'],
        value='area', 
        inline=True,style={'margin-left':'500px'}
    ),

    ],style={'margin':'auto'}),
    
    dcc.Graph(id="graph",style={'width': '1200px','margin': 'auto'}),
    dbc.Row([html.P('  ',style={'width': '1000px',
                             'margin-bottom': '80px',
                                 'margin': 'auto'}) ]),
    html.P('На диаграмме Бокса-Вискера представлено влияние наличия мебели, типа собственности, типа участка и города на арендную площадь и стоимость аренды.',style={'width': '1000px',
                                'margin-bottom': '80px',
                                'margin': 'auto'})
])


@app.callback(
    Output("graph", "figure"), 
    [Input("x-axis", "value"), 
    Input("y-axis", "value")])

def generate_chart(x, y): 
    # df = px.data.tips()
    fig = px.box(df, x=x, y=y)
    return fig