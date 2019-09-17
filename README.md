# Secure Coding with Python.

## Chapter 6: Cross-Site Request Factory
### Requirement
Now that we have authentication in place, we should restrict the listing create form to authenticated users.
Also, we should associate the listings with the user who created it.

### Development
We add a `user_id` column to `Listing` as foreign key to `User`. 
On the`listing.register` controller we add the `@auth` decorator and assign the user when creating the Listing.
On the listings list page we also add information about the author.

Since we are making changes to the models you also need to run:
```bash
> flask db migrate
> flask db upgrade
```

### Vulnerability
Since the only protection we have added to this form is authentication, an attacker can trick the user into navigating
to a malicious website on an authenticated browser, and submit the form in the background, without the user
knowledge using it's authentication cookies.

**Proceed to [next section](https://github.com/nxvl/secure-coding-with-python/tree/6-csrf/test)**

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
