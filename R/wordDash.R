# AUTO GENERATED FILE - DO NOT EDIT

#' @export
wordDash <- function(id=NULL, clickData=NULL, colorScheme=NULL, customColors=NULL, fontFamily=NULL, fontSizeRange=NULL, height=NULL, padding=NULL, rotate=NULL, rotationAngles=NULL, selectedWord=NULL, width=NULL, words=NULL) {
    
    props <- list(id=id, clickData=clickData, colorScheme=colorScheme, customColors=customColors, fontFamily=fontFamily, fontSizeRange=fontSizeRange, height=height, padding=padding, rotate=rotate, rotationAngles=rotationAngles, selectedWord=selectedWord, width=width, words=words)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'WordDash',
        namespace = 'worddash',
        propNames = c('id', 'clickData', 'colorScheme', 'customColors', 'fontFamily', 'fontSizeRange', 'height', 'padding', 'rotate', 'rotationAngles', 'selectedWord', 'width', 'words'),
        package = 'worddash'
        )

    structure(component, class = c('dash_component', 'list'))
}
