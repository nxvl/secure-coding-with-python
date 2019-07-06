from .helpers.sqlifuzzer import sqli_fuzzer

def test_create(client, app):
    assert client.get('/listings/create').status_code == 200

    sqli_fuzzer(client, '/listings/create', ['title', 'description'])
