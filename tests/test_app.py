from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')

    # Assert (Garanta que X é X, valor esperado = valor atual)
    assert response.json() == {'message': 'Olá, mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):
    # UserSchema - Envio
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@test.com',
            'password': 'password@',
        },
    )

    # UserPublic - Response
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testusername2',
            'email': 'test@test2.com',
            'password': 'password@',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test2.com',
        'id': 1,
    }


def test_update_user_not_found_error(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'testusername2',
            'email': 'test@test2.com',
            'password': 'password@',
            'id': 2,
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_read_single_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test2.com',
        'id': 1,
    }


def test_read_single_user_not_found_error(client):
    response = client.get('/users/5')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_user_nor_found_error(client):
    response = client.delete('/users/22')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
