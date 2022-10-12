import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import numpy as np
from app import app



df = pd.read_csv('data\All_Cities_Cleaned.csv')

fig=px.histogram(df,x='city')

bed_bins = [1, 3, 6, 10, 15]
bed_categ = ['1-3', '4-6', '7-10', '11-15']
df['BedCategories'] = pd.cut(df['bedroom'], bed_bins, labels=bed_categ)

fig1=px.histogram(df,x='BedCategories')

bath_bins = [1, 4, 8, 12, 16, 19]
bath_categ = ['1-4', '5-8', '9-12', '13-16', '17-19']
df['BathCategories'] = pd.cut(df['bathroom'], bath_bins, labels=bath_categ)

fig2=px.histogram(df,x='BathCategories')

app = dash.Dash(__name__)


app.layout = html.Div([
    dbc.Row([
        html.H3('Столбчатая диаграмма по городам', style={'margin-left':'80px'}),
       dcc.Graph(figure=fig,style={'width': '900px',
                                'margin-bottom': '30px',
                                'margin': 'auto'}),
                        html.P('Поскольку датасет уже предобработан, можем объединить все дома с разных районов в общие города, получив представленную столбчатую диаграмму.',
                            style={'width': '900px',
                                'margin-bottom': '30px',
                                'margin': 'auto'}), 

        ]),
    dbc.Row([
        html.H3('Столбчатая диаграмма по спальным местам', style={'margin-left':'80px'}),
       dcc.Graph(figure=fig1,style={'width': '900px',
                                'margin-bottom': '30px',
                                'margin': 'auto'}),
                        html.P('Данные были поделены на категории: 1-3, 4-6, 7-10, 11-15 спальных мест.',
                            style={'width': '900px',
                                'margin-bottom': '30px',
                                'margin': 'auto'}), 
        ]),
    dbc.Row([
        html.H3('Столбчатая диаграмма по ванным комнатам', style={'margin-left':'80px'}),
       dcc.Graph(figure=fig2,style={'width': '900px',
                                'margin-bottom': '30px',
                                'margin': 'auto'}),
                        html.P('Данные были поделены на категории: 1-4, 5-8, 9-12, 13-16 и 17-19 ванных комнат.',
                            style={'width': '900px',
                                'margin-bottom': '30px',
                                'margin': 'auto'}), 
        ]),


])



if __name__ == '__main__':
    app.run_server(debug=True)

