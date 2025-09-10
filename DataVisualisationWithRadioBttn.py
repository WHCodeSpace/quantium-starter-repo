import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# the path to the formatted data file
DATA_PATH = "./formatted_data.csv"

# load in data
data = pd.read_csv(DATA_PATH)
data["date"] = pd.to_datetime(data["date"], dayfirst=True)
data = data.sort_values(by="date")

# initialize dash
dash_app = Dash(__name__)

# radio button for region selection
region_selector = dcc.RadioItems(
    id="region-filter",
    options=[
        {"label": "All", "value": "all"},
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"},
    ],
    value="all",
    inline=True,
    style={
        "margin": "20px 0",
        "padding": "10px",
        "backgroundColor": "#f8f9fa",
        "border": "1px solid #dee2e6",
        "borderRadius": "8px",
        "fontFamily": "Arial, sans-serif",
        "fontSize": "16px"
    }
)

# initial line chart
line_chart = px.line(
    data,
    x="date",
    y="sales",
    color="region",
    title="Pink Morsel Sales",
    labels={"date": "Date", "sales": "Sales ($)"}
)

# app layout with CSS styling
dash_app.layout = html.Div(
    style={
        "backgroundColor": "#f0f2f5",
        "minHeight": "100vh",
        "padding": "30px"
    },
    children=[
        html.H1(
            "Pink Morsel Visualizer",
            id="header",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "fontFamily": "Verdana, sans-serif",
                "marginBottom": "20px"
            }
        ),
        html.Div(
            children=[region_selector],
            style={
                "display": "flex",
                "justifyContent": "center",
                "marginBottom": "30px"
            }
        ),
        html.Div(
            children=[dcc.Graph(id="visualization", figure=line_chart)],
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 8px rgba(0,0,0,0.1)"
            }
        )
    ]
)

# callback for interactive filtering
@dash_app.callback(
    Output("visualization", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"] == selected_region]

    fig = px.line(
        filtered_data,
        x="date",
        y="sales",
        color="region" if selected_region == "all" else None,
        title=f"Pink Morsel Sales ({selected_region.capitalize() if selected_region != 'all' else 'All Regions'})",
        labels={"date": "Date", "sales": "Sales ($)"}
    )
    fig.update_layout(
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        font=dict(family="Verdana, sans-serif", size=14, color="#2c3e50"),
        margin=dict(l=40, r=40, t=60, b=40)
    )
    return fig

# run app
if __name__ == "__main__":
    dash_app.run(debug=True)
