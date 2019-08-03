# Secure Coding with Python.

## Chapter 2: SQL Injection
### Fix part 2
In order to fix the SQL injetion once and for all, we should rely on prepared statements, and let the DB engine do the param sanitization, like this:
```python
        sql = "INSERT INTO listings (title, description) VALUES (%s, %s)"
        cur.execute(sql, (title, description))
```

Now both our unit test and bandit are happy!

### Fix part 3
An even better approach is to use an ORM, in this case we set up SQLAlchemy, by using the standard methods the ORM will do the sanitization so we don't need to worry about it. 

**Note**: Most ORMs in some special use cases can still allow SQL Injections to happen, if you are using non-standard methods, review the ORMs security guidelines and test your application.

## Description
Welcome to the Secure coding with python course. In this repository you will find a series of branches for each step of the development of a sample marketplace application. In such a development, we will be making security mistakes and introducing vulnerabilities, we will add tests for them and finally fixing them.

The branches will have the following naming scheme for easier navigation: {Chapter number}-{Chapter Name}/{code|test|fix}. I encourage you to follow the chapters in order, but you can also skip to the specific one you wish to review. 

For this course we will be using Python3, Flask and PostgreSQL.

<<<<<<< HEAD
**Proceed to [next section](https://github.com/nxvl/secure-coding-with-python/tree/3.1-weak-password-storage/code)**
=======
**Proceed to [next section](https://github.com/nxvl/secure-coding-with-python/tree/2.3-sql-injection/fix)**
>>>>>>> 63a94db15f2a764a554613dfe42e6423fbe40bb3

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

### 7. Cross-Site Scripting (xss)
* [7-xss/code](https://github.com/nxvl/secure-coding-with-python/tree/7-xss/code) 
* [7-xss/test](https://github.com/nxvl/secure-coding-with-python/tree/7-xss/test)
* [7-xss/fix](https://github.com/nxvl/secure-coding-with-python/tree/7-xss/fix)

### 8. Broken Access Control
* [8-broken-access-control/code](https://github.com/nxvl/secure-coding-with-python/tree/8-broken-access-control/code) 
* [8-broken-access-control/test](https://github.com/nxvl/secure-coding-with-python/tree/8-broken-access-control/test)
* [8-broken-access-control/fix](https://github.com/nxvl/secure-coding-with-python/tree/8-broken-access-control/fix)

### 9. XML External Entities (XXE)
* [9-xxe/code](https://github.com/nxvl/secure-coding-with-python/tree/9-xxe/code) 
* [9-xxe/test](https://github.com/nxvl/secure-coding-with-python/tree/9-xxe/test)
* [9-xxe/fix](https://github.com/nxvl/secure-coding-with-python/tree/9-xxe/fix)

### 10. Sensitive Data Exposure
* [10-sensitive-data-exposure/code](https://github.com/nxvl/secure-coding-with-python/tree/10-sensitive-data-exposure/code) 
* [10-sensitive-data-exposure/test](https://github.com/nxvl/secure-coding-with-python/tree/10-sensitive-data-exposure/test)
* [10-sensitive-data-exposure/fix](https://github.com/nxvl/secure-coding-with-python/tree/10-sensitive-data-exposure/fix)
