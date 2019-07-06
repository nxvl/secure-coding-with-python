import pytest

from psycopg2.errors import SyntaxError

def sqli_fuzzer(client, url, params):
    fail = False
    injections = ["'", "\\'"]
    for injection in injections:
        for param in params:
            data = {k: 'foo' for k in params}
            data[param] = injection
            try:
                client.post(url, data=data)
            except SyntaxError:
                print('You seems to have an SQLi in %s for param %s' % (url, param))
                fail = True

    if fail:
        pytest.fail('Seems you are vulnerable to SQLi attacks')
