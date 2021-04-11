# Method API

## post

Изменение цветового пространства:

    /api/new_color_space 
        ->
        path: str - директория с файлом || урл в облаке
        color_space: List[str] - лист 
        
        <-
        [
        path: str - директория с обработанным изображением || урл в облаке 
        color_space: str - цветовое пространстов этого файла
        ]

Выделение рамок:

    /api/serch_all_rectangles_of_color
        -> 
        path: str
        color_

## get 

Получение всех доступных цветовых пространств.

    /api/get_color_spaces
        color_space: List[str] - отдет названия всех доступных цветовы пространств.
