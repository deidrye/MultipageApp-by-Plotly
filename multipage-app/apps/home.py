from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import numpy as np
from app import app

''' LAYOUT '''
layout = dbc.Container([
    # HEADER
    dbc.Row([
        html.H3('House Rent Prices of Metropolitan Cities in India'),
        html.P('(Стоимость аренды жилплощади в метрополисах Индии)'),
        html.P('Описание разделов:')
    ],
        style={'margin-bottom': '20px'}),

    # FILTERS
    dbc.Row([
        html.H4('Диаграмма рассеивания'),
        html.P('Описывает диаграмму рассеивания стоимости аренды по площади дома/участка.'),
        html.H4('Столбчатые диаграммы'),
        html.P('Здесь представлены диаграммы количества жилплощадей по городам, количествам спален и ванных комнат.'),
        html.H4('Диаграмма Бокса-Вискера'),
        html.P('На диаграмме Бокса-Вискера можно изучить различные влияния на арендную площадь и стоимость.'),
        html.H4('Гистограммы'),
        html.P('Логарифмические гистограммы стоимости и арендной площади.'),
        html.H4('Табличные данные'),
        html.P('Здесь можно изучить исходные данные и отфильтровать по нужным значениям.'),
        html.H4('Описание данных'),
        html.P('В последнем разделе представляется краткое описание датасета.')
    ],
        style={'margin-bottom': '40px'}),

    
], style={'margin-left': '80px',
          'margin-right': '80px'})
