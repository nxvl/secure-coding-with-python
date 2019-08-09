# Secure Coding with Python.

## Chapter 2: SQL Injection
### Fix
Given that we have seen that the way this injection works is by breaking out of the `'`'s, we can use PostgreSQL escaping `E'\''`. For that we change our SQL query and replace every occurrence of `'` with `\'`:
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

## Description
Welcome to the Secure coding with python course. In this repository you will find a series of branches for each step of the development of a sample marketplace application. In such a development, we will be making security mistakes and introducing vulnerabilities, we will add tests for them and finally fixing them.

The branches will have the following naming scheme for easier navigation: {Chapter number}-{Chapter Name}/{code|test|fix}. I encourage you to follow the chapters in order, but you can also skip to the specific one you wish to review. 

For this course we will be using Python3, Flask and PostgreSQL.

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

### 4. Weak account secrets
* [4-weak-account-secrets/code](https://github.com/nxvl/secure-coding-with-python/tree/4-weak-account-secrets/code) 
* [4-weak-account-secrets/fix](https://github.com/nxvl/secure-coding-with-python/tree/4-weak-account-secrets/fix)

### 5. Broken Authentication
* [5.1-broken-authentication/code](https://github.com/nxvl/secure-coding-with-python/tree/5.1-broken-authentication/code) 
* [5.1-broken-authentication/fix](https://github.com/nxvl/secure-coding-with-python/tree/5.1-broken-authentication/fix)
* [5.2-broken-authentication/fix](https://github.com/nxvl/secure-coding-with-python/tree/5.2-broken-authentication/fix)

### 6. Broken Deauthentication
* [6.1-broken-deauthentication/code](https://github.com/nxvl/secure-coding-with-python/tree/6.1-broken-deauthentication/code) 
* [6.1-broken-deauthentication/test](https://github.com/nxvl/secure-coding-with-python/tree/6.1-broken-deauthentication/test)
* [6.1-broken-deauthentication/fix](https://github.com/nxvl/secure-coding-with-python/tree/6.1-broken-deauthentication/fix)
* [6.2-broken-deauthentication/code](https://github.com/nxvl/secure-coding-with-python/tree/6.2-broken-deauthentication/code) 
* [6.2-broken-deauthentication/test](https://github.com/nxvl/secure-coding-with-python/tree/6.2-broken-deauthentication/test)
* [6.2-broken-deauthentication/fix](https://github.com/nxvl/secure-coding-with-python/tree/6.2-broken-deauthentication/fix)
* [6.3-broken-deauthentication/code](https://github.com/nxvl/secure-coding-with-python/tree/6.3-broken-deauthentication/code) 
* [6.3-broken-deauthentication/test](https://github.com/nxvl/secure-coding-with-python/tree/6.3-broken-deauthentication/test)
* [6.3-broken-deauthentication/fix](https://github.com/nxvl/secure-coding-with-python/tree/6.3-broken-deauthentication/fix)

### 7. Cross-Site Request Forgery (csrf)
* [7-csrf/code](https://github.com/nxvl/secure-coding-with-python/tree/7-csrf/code) 
* [7-csrf/test](https://github.com/nxvl/secure-coding-with-python/tree/7-csrf/test)
* [7-csrf/fix](https://github.com/nxvl/secure-coding-with-python/tree/7-csrf/fix)

### 8. Cross-Site Scripting (xss)
* [8-xss/code](https://github.com/nxvl/secure-coding-with-python/tree/8-xss/code) 
* [8-xss/test](https://github.com/nxvl/secure-coding-with-python/tree/8-xss/test)
* [8-xss/fix](https://github.com/nxvl/secure-coding-with-python/tree/8-xss/fix)

### 9. Broken Access Control
* [9-broken-access-control/code](https://github.com/nxvl/secure-coding-with-python/tree/9-broken-access-control/code) 
* [9-broken-access-control/test](https://github.com/nxvl/secure-coding-with-python/tree/9-broken-access-control/test)
* [9-broken-access-control/fix](https://github.com/nxvl/secure-coding-with-python/tree/9-broken-access-control/fix)

### 10. XML External Entities (XXE)
* [10-xxe/code](https://github.com/nxvl/secure-coding-with-python/tree/10-xxe/code) 
* [10-xxe/test](https://github.com/nxvl/secure-coding-with-python/tree/10-xxe/test)
* [10-xxe/fix](https://github.com/nxvl/secure-coding-with-python/tree/10-xxe/fix)

### 11. Sensitive Data Exposure
* [11-sensitive-data-exposure/code](https://github.com/nxvl/secure-coding-with-python/tree/11-sensitive-data-exposure/code) 
* [11-sensitive-data-exposure/test](https://github.com/nxvl/secure-coding-with-python/tree/11-sensitive-data-exposure/test)
* [11-sensitive-data-exposure/fix](https://github.com/nxvl/secure-coding-with-python/tree/11-sensitive-data-exposure/fix)
