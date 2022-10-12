
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib 
from app import app


df = pd.read_csv('data\All_Cities_Cleaned.csv')


df1 = df['area']
fig=px.histogram(df1,x='area', log_y = True)

df2 = df['price']
fig1=px.histogram(df2,x='price', log_y = True)

layout = html.Div([
    html.H2('Гистограмма количества жилплощадей по площади'),
    dcc.Graph(figure=fig,style={'width': '1000px',
                                'margin-bottom': '80px',
                                'margin': 'auto'}),
    html.H2('Гистограмма количества жилплощадей по стоимости аренды'),
    dcc.Graph(figure=fig1,style={'width': '1000px',
                                'margin-bottom': '80px',
                                'margin': 'auto'}),
])
