# AUTO GENERATED FILE - DO NOT EDIT

export worddash

"""
    worddash(;kwargs...)

A WordDash component.
WordDash is a component that displays a cloud of words.
The size of each word is determined by its frequency.
Clicking on a word selects it, dimming all other words
and outlining the selected word in black.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `clickData` (optional): Data about the clicked word.
Format: { word: string, count: number }. clickData has the following type: lists containing elements 'word', 'count'.
Those elements have the following types:
  - `word` (String; optional)
  - `count` (Real; optional)
- `colorScheme` (String | Array of Strings; optional): Color scheme to use for the words.
Can be either a string (Plotly/d3 color scheme name) or an array of colors.
When an array is provided, colors are interpolated across the frequency range
(lowest count gets first color, highest count gets last color).
- `customColors` (String; optional): Custom colors for specific words.
JSON string with word as key and color as value.
- `fontFamily` (String; optional): Font family to use for the words.
- `fontSizeRange` (Array of Reals; optional): Range of font sizes to use for the words.
Format: [minSize, maxSize]
- `height` (Real; optional): Height of the worddash container in pixels.
- `padding` (Real; optional): Padding between words in pixels.
- `rotate` (Bool; optional): Whether to rotate some words.
- `rotationAngles` (Array of Reals; optional): Array of possible rotation angles in degrees.
Words will be randomly rotated to one of these angles.
- `selectedWord` (String; optional): Currently selected word.
- `width` (Real; optional): Width of the worddash container in pixels.
- `words` (Dict with Strings as keys and values of type Real; optional): Dictionary of words and their counts.
Format: { word1: count1, word2: count2, ... }
"""
function worddash(; kwargs...)
        available_props = Symbol[:id, :clickData, :colorScheme, :customColors, :fontFamily, :fontSizeRange, :height, :padding, :rotate, :rotationAngles, :selectedWord, :width, :words]
        wild_props = Symbol[]
        return Component("worddash", "WordDash", "worddash", available_props, wild_props; kwargs...)
end

