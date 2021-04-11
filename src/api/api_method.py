import os
import sys

from fastapi import FastAPI
import uvicorn
from image_work.manager_image_group import ImageProcessor

from api.models import ColorSpaces
from api.logger_configuration import get_logger

app = FastAPI()
manager = ImageProcessor()
log = get_logger('Main_logger')


def log_this(e: Exception) -> None:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    log.info(f'Выполнение было прервано в файле {file_name}:{exc_tb.tb_lineno} с ошибкой {str(e)}')


@app.post('/api/new_color_space')
async def new_color_space(color_spaces: ColorSpaces):
    try:
        # TODO: rename
        answer = []

        manager.load_image(color_spaces.image)
        path_to_new_image = manager.create_pictures_different_color_space(color_spaces.color_spaces)

        for path, color_space in path_to_new_image:
            answer.append({'path': path, 'color_space': color_space})

        return answer
    except Exception as ex:
        log_this(ex)


@app.get('/api/get_color_spaces')
async def get_color_spaces():
    try:
        return manager.get_color_spaces
    except Exception as ex:
        log_this(ex)


def server_run():
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == '__main__':
    server_run()
