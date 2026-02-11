import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv('stores.csv', sep=',')

df_number=df.groupby('Number')['Revenue'].sum().reset_index()
fig_number = px.bar(df_number, x="Number", y="Revenue", barmode="group", title="Revenue Amounts by Store")

df_city=df.groupby('City')['Revenue'].sum().reset_index()
fig_city = px.bar(df_city, x="City", y="Revenue", barmode="group", title="Revenue Amounts by Store")

# Initialize the Dash app
app = Dash(__name__)

# Define the app layout
app.layout = html.Div(children=[
    html.H1(children='Dash Bar Chart Example'),
    html.H1(children='This is a new deploy'),
    dcc.Graph(
        id='graph_number',
        figure=fig_number
    ),
       dcc.Graph(
        id='graph_city',
        figure=fig_city
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)