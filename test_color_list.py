#!/usr/bin/env python3

import dash
from dash import html, dcc, callback, Input, Output
import sys
import os

# Add the worddash package to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "."))

from worddash import WordDash

# Sample word data
sample_words = {
    "python": 25,
    "javascript": 20,
    "react": 18,
    "dash": 15,
    "plotly": 12,
    "data": 10,
    "visualization": 8,
    "component": 6,
    "web": 5,
    "development": 4,
    "analytics": 3,
    "dashboard": 2,
}

bayer_colors = [
    "#10384f",
    "#263a50",
    "#353c51",
    "#433d52",
    "#4f3f53",
    "#5a4054",
    "#664155",
    "#714256",
    "#7c4257",
    "#874358",
    "#924359",
    "#9c435a",
    "#a7425b",
    "#b2425b",
    "#bd415c",
    "#c83f5d",
    "#d33e5e",
    "#de3b5f",
    "#e93960",
    "#f43561",
    "#ff3162",
]

# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1("WordDash Color List Demo", style={"textAlign": "center"}),
        html.Div(
            [
                html.H3("Bayer Color Gradient"),
                html.P(f"Bayer Colors: {bayer_colors}"),
                WordDash(
                    id="wordcloud-bayer",
                    words=sample_words,
                    colorScheme=bayer_colors,
                    width=600,
                    height=300,
                ),
            ],
            style={"margin": "20px", "border": "1px solid #ccc", "padding": "20px"},
        ),
        html.Div(
            [
                html.H3("Selected Word Info"),
                html.Div(
                    id="click-output", style={"padding": "10px", "fontSize": "16px"}
                ),
            ]
        ),
    ]
)


if __name__ == "__main__":
    app.run(debug=True)
