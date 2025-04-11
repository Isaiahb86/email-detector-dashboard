import os
import dash
from dash import dash_table, html, dcc
import pandas as pd

app = dash.Dash(__name__)

# Scan the emails
os.system("./scan_emails.sh")

# Load scan results
df = pd.read_csv("results.csv", names=["Email File", "Status"])

app.layout = html.Div([
    html.H1("Malicious Email Detection Dashboard"),
    dash_table.DataTable(
        columns=[
            {"name": i, "id": i} for i in df.columns
        ],
        data=df.to_dict("records"),
        style_cell={'textAlign': 'left'},
        style_data_conditional=[
            {
                'if': {'filter_query': '{Status} eq "Malicious"'},
                'backgroundColor': '#FFCCCC',
                'color': 'red'
            }
        ]
    ),
    html.Div([
        html.P("Red rows = detected as malicious", style={"color": "red", "marginTop": 20})
    ])
])

if __name__ == "__main__":
    app.run(debug=True, port=8050)
