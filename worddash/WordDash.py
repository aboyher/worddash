# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal  # noqa: F401
from dash.development.base_component import Component, _explicitize_args
import pandas as pd
import json

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class WordDash(Component):
    """A WordDash component.
    WordDash is a component that displays a cloud of words.
    The size of each word is determined by its frequency.
    Clicking on a word selects it, dimming all other words
    and outlining the selected word in black.

    Keyword arguments:

    - id (string; optional):
        The ID used to identify this component in Dash callbacks.

    - clickData (dict; optional):
        Data about the clicked word. Format: { word: string, count: number
        }.

        `clickData` is a dict with keys:

        - word (string; optional)

        - count (number; optional)

    - colorScheme (string; default 'Viridis'):
        Color scheme to use for the words. Uses Plotly/d3 color scheme
        names.

    - customColors (string; optional):
        Custom colors for specific words. JSON string with word as key and
        color as value.

    - data_frame (pandas.DataFrame; optional):
        DataFrame containing word data. Must be used with word_column and
        count_column.

    - word_column (string; optional):
        Name of the column in data_frame that contains the words.

    - count_column (string; optional):
        Name of the column in data_frame that contains the counts.

    - color_column (string; optional):
        Name of the column in data_frame that contains the colors (optional).

    - fontFamily (string; default 'Arial, sans-serif'):
        Font family to use for the words.

    - fontSizeRange (list of numbers; default [10, 60]):
        Range of font sizes to use for the words. Format: [minSize,
        maxSize].

    - height (number; default 400):
        Height of the worddash container in pixels.

    - padding (number; default 5):
        Padding between words in pixels.

    - rotate (boolean; default True):
        Whether to rotate some words.

    - rotationAngles (list of numbers; default [-60, -45, -30, -15, 0, 15, 30, 45, 60]):
        Array of possible rotation angles in degrees. Words will be
        randomly rotated to one of these angles.

    - selectedWord (string; optional):
        Currently selected word.

    - width (number; default 600):
        Width of the worddash container in pixels.

    - words (dict with strings as keys and values of type number; optional):
        Dictionary of words and their counts. Format: { word1: count1,
        word2: count2, ... }."""

    _children_props = []
    _base_nodes = ["children"]
    _namespace = "worddash"
    _type = "WordDash"
    ClickData = TypedDict(
        "ClickData", {"word": NotRequired[str], "count": NotRequired[NumberType]}
    )

    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        words: typing.Optional[
            typing.Dict[typing.Union[str, float, int], NumberType]
        ] = None,
        data_frame=None,
        word_column: typing.Optional[str] = None,
        count_column: typing.Optional[str] = None,
        color_column: typing.Optional[str] = None,
        width: typing.Optional[NumberType] = None,
        height: typing.Optional[NumberType] = None,
        fontSizeRange: typing.Optional[typing.Sequence[NumberType]] = None,
        fontFamily: typing.Optional[str] = None,
        padding: typing.Optional[NumberType] = None,
        rotate: typing.Optional[bool] = None,
        rotationAngles: typing.Optional[typing.Sequence[NumberType]] = None,
        colorScheme: typing.Optional[str] = None,
        customColors: typing.Optional[str] = None,
        selectedWord: typing.Optional[str] = None,
        clickData: typing.Optional["ClickData"] = None,
        **kwargs
    ):
        self._prop_names = [
            "id",
            "clickData",
            "colorScheme",
            "customColors",
            "fontFamily",
            "fontSizeRange",
            "height",
            "padding",
            "rotate",
            "rotationAngles",
            "selectedWord",
            "width",
            "words",
        ]
        self._valid_wildcard_attributes = []
        self.available_properties = [
            "id",
            "clickData",
            "colorScheme",
            "customColors",
            "fontFamily",
            "fontSizeRange",
            "height",
            "padding",
            "rotate",
            "rotationAngles",
            "selectedWord",
            "width",
            "words",
        ]
        self.available_wildcard_properties = []
        _explicit_args = kwargs.pop("_explicit_args")
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {
            k: _locals[k]
            for k in _explicit_args
            if k != "data_frame"
            and k != "word_column"
            and k != "count_column"
            and k != "color_column"
        }

        # Process DataFrame if provided
        if (
            data_frame is not None
            and isinstance(data_frame, pd.DataFrame)
            and word_column is not None
            and count_column is not None
        ):
            if word_column in data_frame.columns and count_column in data_frame.columns:
                # Convert DataFrame to dictionary format
                words_dict = {}
                colors_dict = {}

                # Process each row in the DataFrame
                for _, row in data_frame.iterrows():
                    word = str(row[word_column])
                    count = float(row[count_column])
                    words_dict[word] = count

                    # Add color if color column is provided
                    if color_column is not None and color_column in data_frame.columns:
                        colors_dict[word] = str(row[color_column])

                # Set the words property
                args["words"] = words_dict

                # If colors are provided, pass them as a custom property
                if colors_dict:
                    args["customColors"] = json.dumps(colors_dict)

        super(WordDash, self).__init__(**args)


setattr(WordDash, "__init__", _explicitize_args(WordDash.__init__))
