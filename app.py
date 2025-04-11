import os
import dash
from dash import dash_table, html, dcc
from dash.dependencies import Input, Output
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Malicious Email Detection Dashboard"),

    # Table to display scan results
    dash_table.DataTable(
        id='email-table',
        columns=[
            {"name": "Email File", "id": "Email File"},
            {"name": "Status", "id": "Status"}
        ],
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
    ]),

    # This makes the app update every 10 seconds
    dcc.Interval(
        id='interval-component',
        interval=10*1000,  # 10 seconds in milliseconds
        n_intervals=0
    )
])

# Callback to update the table every 10 seconds
@app.callback(
    Output('email-table', 'data'),
    Input('interval-component', 'n_intervals')
)
def update_table(n):
    # Run the email scanner script
    os.system("./scan_emails.sh")

    # Load the latest scan results
    df = pd.read_csv("results.csv", names=["Email File", "Status"])
    return df.to_dict("records")

# Start the server
if __name__ == "__main__":
    app.run(debug=True, port=8050)


