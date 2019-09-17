# Secure Coding with Python.

## Chapter 2: SQL Injection
### Fix
Given that we have seen that the way this injection works is by breaking out of the `'`'s, we can use PostgreSQL 
escaping `E'\''`. For that we change our SQL query and replace every occurrence of `'` with `\'`:

```python
        sql = "INSERT INTO listings (title, description) VALUES (E'%s', E'%s')" % (
            title.replace("'", "\\'"), description.replace("'", "\\'")
        )
```

With that our test now pass:

```text
(venv) > $ pytest --tb=short
================================================================================================== test session starts ===================================================================================================
platform linux -- Python 3.5.3, pytest-5.0.0, py-1.8.0, pluggy-0.12.0
rootdir: {...}
collected 1 item
tests/test_listings.py .                                                                                                                                                                                           [100%]
================================================================================================ 1 passed in 0.95 seconds ================================================================================================
```

But this is not sufficient, if we modify our payload to be `injection\', (select version()))-- -` our query will end up being:

```sql
INSERT INTO listings (title, description) VALUES (E'injection\\', (select version()))-- -', E'\'')
```

and attacker will still be able to exploit our app.

**Proceed to [next section](https://github.com/nxvl/secure-coding-with-python/tree/2.2-sql-injection/test)**

## Index
### 1. Vulnerable Components
* [1-vulnerable-components/code](https://github.com/nxvl/secure-coding-with-python/tree/1-vulnerable-components/code) 
* [1-vulnerable-components/test](https://github.com/nxvl/secure-coding-with-python/tree/1-vulnerable-components/test)
* [1-vulnerable-components/fix](https://github.com/nxvl/secure-coding-with-python/tree/1-vulnerable-components/fix)

### 2. SQL Injection
* [2.1-sql-injection/code](https://github.com/nxvl/secure-coding-with-python/tree/2.1-sql-injection/code) 
* [2.1-sql-injection/test](https://github.com/nxvl/secure-coding-with-python/tree/2.1-sql-injection/test)
* [2.1-sql-injection/fix](https://github.com/nxvl/secure-coding-with-python/tree/2.1-sql-injection/fix)
* [2.2-sql-injection/test](https://github.com/nxvl/secure-coding-with-python/tree/2.2-sql-injection/test)
* [2.2-sql-injection/fix](https://github.com/nxvl/secure-coding-with-python/tree/2.2-sql-injection/fix)
* [2.3-sql-injection/fix](https://github.com/nxvl/secure-coding-with-python/tree/2.3-sql-injection/fix)

### 3. Weak password storage
* [3.1-weak-password-storage/code](https://github.com/nxvl/secure-coding-with-python/tree/3.1-weak-password-storage/code) 
* [3.1-weak-password-storage/fix](https://github.com/nxvl/secure-coding-with-python/tree/3.1-weak-password-storage/fix)
* [3.2-weak-password-storage/test](https://github.com/nxvl/secure-coding-with-python/tree/3.2-weak-password-storage/test)
* [3.2-weak-password-storage/fix](https://github.com/nxvl/secure-coding-with-python/tree/3.2-weak-password-storage/fix)

### 4. Broken Authentication
* [4-broken-authentication/code](https://github.com/nxvl/secure-coding-with-python/tree/4-broken-authentication/code) 
* [4-broken-authentication/fix](https://github.com/nxvl/secure-coding-with-python/tree/4-broken-authentication/fix)

### 5. Broken Deauthentication
* [5.1-broken-deauthentication/code](https://github.com/nxvl/secure-coding-with-python/tree/5.1-broken-deauthentication/code) 
* [5.1-broken-deauthentication/test](https://github.com/nxvl/secure-coding-with-python/tree/5.1-broken-deauthentication/test)
* [5.1-broken-deauthentication/fix](https://github.com/nxvl/secure-coding-with-python/tree/5.1-broken-deauthentication/fix)
* [5.2-broken-deauthentication/code](https://github.com/nxvl/secure-coding-with-python/tree/5.2-broken-deauthentication/code) 
* [5.2-broken-deauthentication/test](https://github.com/nxvl/secure-coding-with-python/tree/5.2-broken-deauthentication/test)
* [5.2-broken-deauthentication/fix](https://github.com/nxvl/secure-coding-with-python/tree/5.2-broken-deauthentication/fix)

### 6. Cross-Site Request Forgery (csrf)
* [6-csrf/code](https://github.com/nxvl/secure-coding-with-python/tree/6-csrf/code) 
* [6-csrf/test](https://github.com/nxvl/secure-coding-with-python/tree/6-csrf/test)
* [6-csrf/fix](https://github.com/nxvl/secure-coding-with-python/tree/6-csrf/fix)

### 7. Cross-Site Scripting (xss)
* [7-xss/code](https://github.com/nxvl/secure-coding-with-python/tree/7-xss/code) 
* [7-xss/test](https://github.com/nxvl/secure-coding-with-python/tree/7-xss/test)
* [7-xss/fix](https://github.com/nxvl/secure-coding-with-python/tree/7-xss/fix)

### 8. Broken Access Control
* [8-broken-access-control/code](https://github.com/nxvl/secure-coding-with-python/tree/8-broken-access-control/code) 
* [8-broken-access-control/test](https://github.com/nxvl/secure-coding-with-python/tree/8-broken-access-control/test)
* [8-broken-access-control/fix](https://github.com/nxvl/secure-coding-with-python/tree/8-broken-access-control/fix)

### 9. Sensitive Data Exposure
* [9-sensitive-data-exposure/code](https://github.com/nxvl/secure-coding-with-python/tree/9-sensitive-data-exposure/code) 
* [9-sensitive-data-exposure/test](https://github.com/nxvl/secure-coding-with-python/tree/9-sensitive-data-exposure/test)
* [9-sensitive-data-exposure/fix](https://github.com/nxvl/secure-coding-with-python/tree/9-sensitive-data-exposure/fix)
