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

# Sample DataFrame
sample_df = pd.DataFrame(
    [
        {"word": "Python", "count": 100, "color": "#ff7f0e"},
        {"word": "JavaScript", "count": 80, "color": "#1f77b4"},
        {"word": "React", "count": 70, "color": "#2ca02c"},
        {"word": "Dash", "count": 90, "color": "#d62728"},
        {"word": "Plotly", "count": 85, "color": "#9467bd"},
        {"word": "D3", "count": 75, "color": "#8c564b"},
        {"word": "Data", "count": 95, "color": "#e377c2"},
        {"word": "Visualization", "count": 65, "color": "#7f7f7f"},
        {"word": "Component", "count": 60, "color": "#bcbd22"},
        {"word": "Cloud", "count": 55, "color": "#17becf"},
        {"word": "Web", "count": 50},
        {"word": "Development", "count": 45},
        {"word": "Analytics", "count": 40},
        {"word": "Chart", "count": 35},
        {"word": "Graph", "count": 30},
        {"word": "Interactive", "count": 25},
        {"word": "Framework", "count": 20},
        {"word": "Library", "count": 15},
        {"word": "Code", "count": 10},
        {"word": "Programming", "count": 5},
    ]
)

app.layout = html.Div(
    [
        html.H1("WordDash Component Demo"),
        # Input method selector
        html.Div(
            [
                html.H3("Select Input Method"),
                dcc.RadioItems(
                    id="input-method",
                    options=[
                        {"label": "Dictionary", "value": "dict"},
                        {"label": "DataFrame", "value": "dataframe"},
                    ],
                    value="dict",
                    labelStyle={"display": "inline-block", "marginRight": "20px"},
                ),
            ],
            style={"marginBottom": "20px"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H3("WordDash"),
                        worddash.WordDash(
                            id="worddash",
                            words=sample_words,
                            width=600,
                            height=400,
                            fontSizeRange=[15, 80],
                            rotate=True,
                            rotationAngles=[-60, -45, -30, -15, 0, 15, 30, 45, 60],
                        ),
                        # html.Div(id="worddash-container"),
                    ],
                    style={
                        "width": "60%",
                        "display": "inline-block",
                        "vertical-align": "top",
                    },
                ),
                html.Div(
                    [
                        html.H3("Selected Word Info"),
                        html.Div(id="selected-word-display"),
                        html.Hr(),
                        html.H3("Color Scheme"),
                        dcc.Dropdown(
                            id="color-scheme-dropdown",
                            options=[
                                {"label": "Viridis", "value": "Viridis"},
                                {"label": "Plasma", "value": "Plasma"},
                                {"label": "Inferno", "value": "Inferno"},
                                {"label": "Magma", "value": "Magma"},
                                {"label": "Cividis", "value": "Cividis"},
                                {"label": "Warm", "value": "Warm"},
                                {"label": "Cool", "value": "Cool"},
                                {"label": "Blues", "value": "Blues"},
                                {"label": "Greens", "value": "Greens"},
                                {"label": "Reds", "value": "Reds"},
                                {"label": "Purples", "value": "Purples"},
                                {"label": "Oranges", "value": "Oranges"},
                                {"label": "Rainbow", "value": "Rainbow"},
                                {"label": "Sinebow", "value": "Sinebow"},
                                {"label": "Turbo", "value": "Turbo"},
                                {"label": "Spectral", "value": "Spectral"},
                            ],
                            value="Viridis",
                        ),
                        html.Hr(),
                        html.H3("Add/Update Word"),
                        dcc.Input(
                            id="word-input", type="text", placeholder="Enter a word"
                        ),
                        dcc.Input(
                            id="count-input",
                            type="number",
                            placeholder="Enter count",
                            min=1,
                        ),
                        html.Button("Add/Update", id="add-word-button"),
                        html.Hr(),
                        html.H3("Remove Word"),
                        dcc.Input(
                            id="remove-word-input",
                            type="text",
                            placeholder="Enter word to remove",
                        ),
                        html.Button("Remove", id="remove-word-button"),
                    ],
                    style={
                        "width": "35%",
                        "display": "inline-block",
                        "vertical-align": "top",
                        "padding": "20px",
                    },
                ),
            ]
        ),
    ]
)


@callback(
    Output("worddash", "words", allow_duplicate=True),
    Input("input-method", "value"),
    prevent_initial_call=True,
)
def update_worddash_input_method(input_method):
    return sample_words


@callback(Output("worddash", "colorScheme"), Input("color-scheme-dropdown", "value"))
def udpate_worddash_color_scheme(color_scheme):
    return color_scheme


@callback(
    Output("selected-word-display", "children"),
    Input("worddash", "clickData"),
    prevent_initial_call=True,
)
def display_selected_word(click_data):
    if click_data:
        return [
            html.P(f"Selected Word: {click_data['word']}"),
            html.P(f"Count: {click_data['count']}"),
        ]
    return "No word selected"


@callback(
    Output("worddash", "words"),
    Input("add-word-button", "n_clicks"),
    Input("remove-word-button", "n_clicks"),
    State("worddash", "words"),
    State("word-input", "value"),
    State("count-input", "value"),
    State("remove-word-input", "value"),
    prevent_initial_call=True,
)
def update_words(add_clicks, remove_clicks, current_words, word, count, remove_word):
    ctx = callback_context

    if not ctx.triggered:
        return current_words

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "add-word-button" and word and count:
        current_words[word] = count
    elif (
        button_id == "remove-word-button"
        and remove_word
        and remove_word in current_words
    ):
        del current_words[remove_word]

    return current_words


if __name__ == "__main__":
    app.run(debug=True)
