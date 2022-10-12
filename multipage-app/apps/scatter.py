import dash
from dash import dcc, html
from dash.dependencies import Input,Output
import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
from app import app




df = pd.read_csv('data\All_Cities_Cleaned.csv')

''' FILTERS '''
fig=px.scatter(df,x='area',y='price')
area_select = dcc.RangeSlider(
        id='range-slider',
        min=min(df['area']),
        max=max(df['area']),
        value=[min(df['area']),max(df['area'])]
    )



''' LAYOUT '''
layout = html.Div([
    dbc.Row(html.H2('Распределение стоимости аренды по площади участка'),
            style={'margin-bottom': 40, 'margin-left':'50px'}),
    dbc.Row([
    
    html.H5('Диапазон площадей участков',style={'margin-left': '100px',
                                'margin-bottom': '15px'}),
html.Div(area_select,style={'margin-left': '50px','width': '400px'})
    ]),

    
    dcc.Graph(id='chart',figure=fig),
    dbc.Row([html.P('На данной диаграмме рассеивания представлен разброс соотношений стоимости аренды к площади участка',style={'width': '1000px',
                             'margin-bottom': '80px',
                                 'margin': 'auto'}) ])        
],)



@app.callback (
    Output(component_id='chart',component_property='figure'),
    Input(component_id='range-slider',component_property='value')
)

def update_chart(radius_range):
    print(radius_range[1])
    print(radius_range[0])
    chart_data=df[(df['area'] > radius_range[0])&
                  (df['area'] < radius_range[1])]
    fig = px.scatter(chart_data,x='area', y='price')

    return fig



