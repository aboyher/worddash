import worddash
import pandas as pd
from dash import (
    Dash,
    callback,
    html,
    Input,
    Output,
    State,
    dcc,
    callback_context,
    no_update,
)

app = Dash(__name__)

# Sample word dictionary
sample_words = {
    "Python": 100,
    "JavaScript": 80,
    "React": 70,
    "Dash": 90,
    "Plotly": 85,
    "D3": 75,
    "Data": 95,
    "Visualization": 65,
    "Component": 60,
    "Cloud": 55,
    "Web": 50,
    "Development": 45,
    "Analytics": 40,
    "Chart": 35,
    "Graph": 30,
    "Interactive": 25,
    "Framework": 20,
    "Library": 15,
    "Code": 10,
    "Programming": 5,
}

app.layout = html.Div(
    [
        html.H1("WordDash Responsive Component Demo"),
        
        html.H2("1. Fixed Size WordDash (600x400)"),
        html.Div(
            [
                worddash.WordDash(
                    id="worddash-fixed",
                    words=sample_words,
                    width=600,
                    height=400,
                    fontSizeRange=[15, 60],
                    rotate=True,
                    colorScheme="Viridis",
                ),
            ],
            style={
                "border": "2px solid #ccc",
                "padding": "10px",
                "margin": "20px 0",
                "backgroundColor": "#f9f9f9",
            }
        ),
        
        html.H2("2. Responsive WordDash (fills container width, 300px height)"),
        html.Div(
            [
                worddash.WordDash(
                    id="worddash-responsive-width",
                    words=sample_words,
                    height=300,  # Fixed height, responsive width
                    fontSizeRange=[12, 50],
                    rotate=True,
                    colorScheme="Plasma",
                ),
            ],
            style={
                "border": "2px solid #007bff",
                "padding": "10px",
                "margin": "20px 0",
                "backgroundColor": "#e7f3ff",
                "width": "100%",
            }
        ),
        
        html.H2("3. Fully Responsive WordDash (fills container)"),
        html.Div(
            [
                worddash.WordDash(
                    id="worddash-fully-responsive",
                    words=sample_words,
                    fontSizeRange=[10, 45],
                    rotate=True,
                    colorScheme="Inferno",
                ),
            ],
            style={
                "border": "2px solid #28a745",
                "padding": "10px",
                "margin": "20px 0",
                "backgroundColor": "#e8f5e8",
                "width": "100%",
                "height": "400px",  # Container height
            }
        ),
        
        html.H2("4. Responsive in Flexbox Layout"),
        html.Div(
            [
                html.Div(
                    [
                        html.H4("Left Panel"),
                        worddash.WordDash(
                            id="worddash-flex-left",
                            words={k: v for k, v in list(sample_words.items())[:10]},
                            fontSizeRange=[8, 30],
                            rotate=False,
                            colorScheme="Cool",
                        ),
                    ],
                    style={
                        "flex": "1",
                        "border": "2px solid #dc3545",
                        "padding": "10px",
                        "margin": "10px",
                        "backgroundColor": "#ffeaea",
                        "height": "300px",
                    }
                ),
                html.Div(
                    [
                        html.H4("Right Panel"),
                        worddash.WordDash(
                            id="worddash-flex-right",
                            words={k: v for k, v in list(sample_words.items())[10:]},
                            fontSizeRange=[8, 30],
                            rotate=False,
                            colorScheme="Warm",
                        ),
                    ],
                    style={
                        "flex": "1",
                        "border": "2px solid #ffc107",
                        "padding": "10px",
                        "margin": "10px",
                        "backgroundColor": "#fff8e1",
                        "height": "300px",
                    }
                ),
            ],
            style={
                "display": "flex",
                "margin": "20px 0",
            }
        ),
        
        html.H2("5. Responsive in Grid Layout"),
        html.Div(
            [
                html.Div(
                    [
                        html.H4("Grid Item 1"),
                        worddash.WordDash(
                            id="worddash-grid-1",
                            words={k: v for k, v in list(sample_words.items())[:5]},
                            fontSizeRange=[10, 35],
                            colorScheme="Blues",
                        ),
                    ],
                    style={
                        "border": "2px solid #6f42c1",
                        "padding": "10px",
                        "backgroundColor": "#f3f0ff",
                        "height": "250px",
                    }
                ),
                html.Div(
                    [
                        html.H4("Grid Item 2"),
                        worddash.WordDash(
                            id="worddash-grid-2",
                            words={k: v for k, v in list(sample_words.items())[5:10]},
                            fontSizeRange=[10, 35],
                            colorScheme="Greens",
                        ),
                    ],
                    style={
                        "border": "2px solid #20c997",
                        "padding": "10px",
                        "backgroundColor": "#e8f8f5",
                        "height": "250px",
                    }
                ),
                html.Div(
                    [
                        html.H4("Grid Item 3"),
                        worddash.WordDash(
                            id="worddash-grid-3",
                            words={k: v for k, v in list(sample_words.items())[10:15]},
                            fontSizeRange=[10, 35],
                            colorScheme="Oranges",
                        ),
                    ],
                    style={
                        "border": "2px solid #fd7e14",
                        "padding": "10px",
                        "backgroundColor": "#fff4e6",
                        "height": "250px",
                    }
                ),
                html.Div(
                    [
                        html.H4("Grid Item 4"),
                        worddash.WordDash(
                            id="worddash-grid-4",
                            words={k: v for k, v in list(sample_words.items())[15:]},
                            fontSizeRange=[10, 35],
                            colorScheme="Purples",
                        ),
                    ],
                    style={
                        "border": "2px solid #e83e8c",
                        "padding": "10px",
                        "backgroundColor": "#fdf2f8",
                        "height": "250px",
                    }
                ),
            ],
            style={
                "display": "grid",
                "gridTemplateColumns": "1fr 1fr",
                "gap": "10px",
                "margin": "20px 0",
            }
        ),
        
        html.Div(
            [
                html.H3("Instructions:"),
                html.Ul([
                    html.Li("The first WordDash has fixed dimensions (600x400 pixels)"),
                    html.Li("The second WordDash fills the container width but has a fixed height"),
                    html.Li("The third WordDash fills both width and height of its container"),
                    html.Li("The fourth example shows WordDash components in a flexbox layout"),
                    html.Li("The fifth example shows WordDash components in a CSS grid layout"),
                    html.Li("Try resizing your browser window to see the responsive behavior!"),
                ]),
            ],
            style={
                "backgroundColor": "#f8f9fa",
                "padding": "20px",
                "margin": "20px 0",
                "borderRadius": "5px",
            }
        ),
    ],
    style={"padding": "20px", "fontFamily": "Arial, sans-serif"}
)

if __name__ == "__main__":
    app.run(debug=True, port=8051)
