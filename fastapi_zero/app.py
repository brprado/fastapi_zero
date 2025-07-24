from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, mundo!'}


@app.get(
    '/hello-world', status_code=HTTPStatus.OK, response_class=HTMLResponse
)
def hello_world():
    return HTMLResponse("""
                        <!DOCTYPE html>
                        <html lang="pt-br">
                        <head>
                            <meta charset="UTF-8">
                            <title>Olá Mundo</title>
                        </head>
                        <body>
                            <h1>Olá, mundo!</h1>
                        </body>
                        </html>""")
