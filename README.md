# Secure Coding with Python.

## Chapter 3: Weak Password Storage
### Fix
In order to keep password secure and secret we need to encrypt them before saving. Since we know MD5 has been long broken, we are going to use SHA256.

### Vulnerability
Even though we are storing passwords encrypted, our choice of algorithm allows an attacker to perform rainbow table attacks, given access to the password hashes.

**Proceed to [next section](https://github.com/nxvl/secure-coding-with-python/tree/3.2-weak-password-storage/test)**

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
