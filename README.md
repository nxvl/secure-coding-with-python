# Secure Coding with Python.

## Chapter 3: Weak Password Storage
### Fix
In order to prevent rainbow table attacks, cryptographers incorporated *[salt](https://en.wikipedia.org/wiki/Salt_(cryptography)* to hashing algorithms.
One of the algorithms that incorporates *salt* is [Bcrypt](https://en.wikipedia.org/wiki/Bcrypt).
Said algorithm also uses a technique known as *[key stretching](https://en.wikipedia.org/wiki/Key_stretching)*, while salt prevents precomputation attacks, key stretching helps thwart attacks that rely on hardware that can perform hashes very quickly, such as GPUs and ASICs

To test this concept, here is a function that hashes a password and times how long it takes to do so. We increase the iteration in 4 every time.
```python
In [1]: import bcrypt                                                                                                                                                                                                                                                       

In [2]: import time                                                                                                                                                                                                                                                         

In [3]: def hash(passwd, r): 
   ...:     start = time.time() 
   ...:     salt = bcrypt.gensalt(rounds=r) 
   ...:     hashed = bcrypt.hashpw(passwd, salt) 
   ...:     end = time.time() 
   ...:     print(end - start) 
   ...:     print(salt) 
   ...:     print(hashed) 
   ...:                                                                                                                                                                                                                                                                     

In [4]: hash(b'supersecret', 4)                                                                                                                                                                                                                                             
0.0013570785522460938
b'$2b$04$wBySsg90EhLyCxFhuNC9Ze'
b'$2b$04$wBySsg90EhLyCxFhuNC9ZeDZKdauAtlEcegqM0GOyZKIgJhJ6neMW'

In [5]: hash(b'supersecret', 8)                                                                                                                                                                                                                                             
0.01915597915649414
b'$2b$08$QNWHnTrxBQu8pscr5hhveu'
b'$2b$08$QNWHnTrxBQu8pscr5hhveuyNOPwtR4VhxujWE/O.yjc60DhIduWkq'

In [6]: hash(b'supersecret', 12)                                                                                                                                                                                                                                            
0.2138371467590332
b'$2b$12$.Eql6xg1/uUoWr3yuYSOaO'
b'$2b$12$.Eql6xg1/uUoWr3yuYSOaOLkEZ.XoUiJOjuMHtjyWNZoW8JOOSHx.'

In [7]: hash(b'supersecret', 16)                                                                                                                                                                                                                                            
3.2648401260375977
b'$2b$16$A4xDXHZPHPE5tUxdqoJD0u'
b'$2b$16$A4xDXHZPHPE5tUxdqoJD0uXleSIgNGHOOv8yQ6wQIU/rLoVwqtF4C'
```
 
Now if an attacker gets our hashed passwords, since each password has it's own hash, the brute-force attack will need to be performed per-hash, since the salt chances for each one. And since we can configure the iterations, as time passes by, we can increase it to make a brute-force attack slower each time.

**Note**: Other algorithms that include the same concepts, and are arguably better, are scrypt and argon2.


**Proceed to [next section](https://github.com/nxvl/secure-coding-with-python/tree/4-weak-account-secrets/code)**

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
