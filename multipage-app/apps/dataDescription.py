from dash import dcc, html
import dash_bootstrap_components as dbc

table_header = [
    html.Thead(html.Tr([html.Th("Показатель"), html.Th("Описание")]))
]

expl = {'seller_type': 'Тип продавца(Владелец/агент)',
        'bedroom': 'Количество спален',
        'layout_type': 'Тип помещения',
        'property_type': 'Вид собственности',
        'locality': 'Район',
        'price': 'Стоимость аренды',
        'area': 'Общая площадь жилья(или участка)',
        'furnish_type': 'Наличие мебели',
        'bathroom': 'Количество спален',
        'city': 'Город'
        }

tbl_rows = []
for i in expl:
    tbl_rows.append(html.Tr([html.Td(i), html.Td(expl[i])]))

table_body = [html.Tbody(tbl_rows)]

table = dbc.Table(table_header + table_body, bordered=True)

''' LAYOUT '''
layout = dbc.Container([
    # HEADER
    dbc.Row([
        html.H4('Описание датасета')
    ],
        style={'margin-bottom': '20px'}),

    # Description
    dbc.Row([
        dbc.Col([
            html.A('Данные заимствованы с сайта Kaggle.com', href="https://www.kaggle.com/datasets/saisaathvik/house-rent-prices-of-metropolitan-cities-in-india?select=_All_Cities_Cleaned.csv"),
            html.P(
                'Датасет представляет информацию об арендных жилплощадях в Индии. '
                'Собрана статистика о следующих параметрах '
                , style={'width': '800px'})
        ])
    ],
        style={'margin-bottom': '40px'}),

    # CONTENT
    dbc.Row(html.Div(children=table))
], style={'margin-left': '80px',
          'margin-right': '80px',
          'margin-bottom': '80px'})
