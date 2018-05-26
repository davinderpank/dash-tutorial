import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python by Davinder Pank.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualisation',
                'titlefont': {'size': 50, 'family': 'Courier New, monospace'},
                'xaxis': {'title': 'X-Axis', 'titlefont': {'size': 25}},
                'yaxis': {'title': 'Y-Axis'}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)