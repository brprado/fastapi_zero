from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    # Arrange (Arranjo das coisas necessarias p rodar o teste)
    client = TestClient(app)

    # Act (Executa a coisa)
    response = client.get('/')

    # Assert (Garanta que X é X, valor esperado = valor atual)
    assert response.json() == {'message': 'Olá, mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_endpoint_hello_world():
    # Arrange
    client = TestClient(app)

    # Act / Setup
    response = client.get('/hello-world')

    # Assert
    assert '<h1>Olá, mundo!</h1>' in response.text
    assert response.headers['content-type'] == 'text/html; charset=utf-8'
    assert response.status_code == HTTPStatus.OK
