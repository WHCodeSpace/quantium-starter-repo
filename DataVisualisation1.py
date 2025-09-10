import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the processed data
DATA_PATH = "./formatted_data.csv"
df = pd.read_csv(DATA_PATH)
print(df.head())
print(df.columns)

# Convert date column to datetime for proper sorting (day first)
df["date"] = pd.to_datetime(df["date"], dayfirst=True)
df = df.sort_values("date")


# Create the line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",   # optional, shows different lines per region
    title="Sales Over Time",
    labels={"date": "Transaction Date", "sales": "Sales ($)"}
)

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)

