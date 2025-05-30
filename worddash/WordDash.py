# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

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

- colorScheme (string | list of strings; default 'Viridis'):
    Color scheme to use for the words. Can be either a string
    (Plotly/d3 color scheme name) or an array of colors. When an array
    is provided, colors are interpolated across the frequency range
    (lowest count gets first color, highest count gets last color).

- customColors (string; optional):
    Custom colors for specific words. JSON string with word as key and
    color as value.

- fontFamily (string; default 'Arial, sans-serif'):
    Font family to use for the words.

- fontSizeRange (list of numbers; default [10, 60]):
    Range of font sizes to use for the words. Format: [minSize,
    maxSize].

- height (number; optional):
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

- width (number; optional):
    Width of the worddash container in pixels.

- words (dict with strings as keys and values of type number; optional):
    Dictionary of words and their counts. Format: { word1: count1,
    word2: count2, ... }."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'worddash'
    _type = 'WordDash'
    ClickData = TypedDict(
        "ClickData",
            {
            "word": NotRequired[str],
            "count": NotRequired[NumberType]
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        words: typing.Optional[typing.Dict[typing.Union[str, float, int], NumberType]] = None,
        width: typing.Optional[NumberType] = None,
        height: typing.Optional[NumberType] = None,
        fontSizeRange: typing.Optional[typing.Sequence[NumberType]] = None,
        fontFamily: typing.Optional[str] = None,
        padding: typing.Optional[NumberType] = None,
        rotate: typing.Optional[bool] = None,
        rotationAngles: typing.Optional[typing.Sequence[NumberType]] = None,
        colorScheme: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        customColors: typing.Optional[str] = None,
        selectedWord: typing.Optional[str] = None,
        clickData: typing.Optional["ClickData"] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'clickData', 'colorScheme', 'customColors', 'fontFamily', 'fontSizeRange', 'height', 'padding', 'rotate', 'rotationAngles', 'selectedWord', 'width', 'words']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'clickData', 'colorScheme', 'customColors', 'fontFamily', 'fontSizeRange', 'height', 'padding', 'rotate', 'rotationAngles', 'selectedWord', 'width', 'words']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(WordDash, self).__init__(**args)

setattr(WordDash, "__init__", _explicitize_args(WordDash.__init__))
