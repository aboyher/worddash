% Auto-generated: do not edit by hand
\name{wordDash}

\alias{wordDash}

\title{WordDash component}

\description{
WordDash is a component that displays a cloud of words. The size of each word is determined by its frequency. Clicking on a word selects it, dimming all other words and outlining the selected word in black.
}

\usage{
wordDash(id=NULL, clickData=NULL, colorScheme=NULL,
customColors=NULL, fontFamily=NULL, fontSizeRange=NULL,
height=NULL, padding=NULL, rotate=NULL, rotationAngles=NULL,
selectedWord=NULL, width=NULL, words=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{clickData}{Lists containing elements 'word', 'count'.
those elements have the following types:
  - word (character; optional)
  - count (numeric; optional). Data about the clicked word.
Format: { word: string, count: number }}

\item{colorScheme}{Character | list of characters. Color scheme to use for the words.
Can be either a string (Plotly/d3 color scheme name) or an array of colors.
When an array is provided, colors are interpolated across the frequency range
(lowest count gets first color, highest count gets last color).}

\item{customColors}{Character. Custom colors for specific words.
JSON string with word as key and color as value.}

\item{fontFamily}{Character. Font family to use for the words.}

\item{fontSizeRange}{List of numerics. Range of font sizes to use for the words.
Format: [minSize, maxSize]}

\item{height}{Numeric. Height of the worddash container in pixels.}

\item{padding}{Numeric. Padding between words in pixels.}

\item{rotate}{Logical. Whether to rotate some words.}

\item{rotationAngles}{List of numerics. Array of possible rotation angles in degrees.
Words will be randomly rotated to one of these angles.}

\item{selectedWord}{Character. Currently selected word.}

\item{width}{Numeric. Width of the worddash container in pixels.}

\item{words}{List with named elements and values of type numeric. Dictionary of words and their counts.
Format: { word1: count1, word2: count2, ... }}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

