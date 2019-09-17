# Secure Coding with Python.

## Chapter 6: Cross-Site Request Factory
### Test
To easily test for CSRF and proof of concept generation, we are going to use 
[OWASP Zed Attack Proxy](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project), or ZAP for short, again.

If you followed the steps on 
[5.2-broken-deauthentication/test](https://github.com/nxvl/secure-coding-with-python/tree/5.2-broken-deauthentication/test)
you should already have ZAP installed, if not please install it.

1. Run ZAP. It will ask if you want to persist the ZAP Session.
2. Select `No, i do not want to persist this session at this mement in time` and uncheck `Remember my choice and do not ask me again`.
3. Click `Start`.
4. On the top right, find the icon `Open the browser you've chosen in the Quick Start tab pre-configured to proxy trough ZAP`. In my case it had the firefox icon.
5. Navigate to [http://localhost:5000/user/login](http://localhost:5000/user/login)
6. Login with the credentials of the user you created.
7. Go to [http://localhost:5000/listings/create](http://localhost:5000/listings/create)
8. Create a new listing.
9. On the left panel navigate to `Sites` -> `http://localhost:5000` -> `listings`
10. Select `POST:create(description,title)`.
11. On the bottom panel go to the `Alerts` tab.
12. On the left panel under `Alerts` expand `Absence of Anti-CSRF Tokens`
13. Click on `GET: http://localhost:5000/listings/create`. The right side panel has a lot of information about the vulnerability, solutions and references.
14. Now on the top left panel right click on `POST:create(description,title)`, the same from step 10.
15. Click `Generate Anti-CSRF Test FORM`.
16. A page on `http://localhost:8080` with a form very similar to the `listings/create` one.
17. On another tab, make sure you are authenticated by going to [http://localhost:5000/user/welcome](http://localhost:5000/user/welcome). Login if you aren't.
18. Back on the ZAP generated form insert a description and title. Mind that the fields might be inverted. 
19. Go to [http://localhost:5000/listings](http://localhost:5000/listings) and refresh the page.

As you can see, we have been able to generate a new entry as an authenticated user into our site from another site, 
that the user could've been tricked into navigating to.


**Proceed to [next section](https://github.com/nxvl/secure-coding-with-python/tree/6-csrf/fix)**

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
