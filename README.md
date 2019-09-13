# Secure Coding with Python.

## Chapter 5: Broken De-Authentication
### Test
Since the vulnerability is the same as the prior chapter, the test is also very similar, this time we are going to
use [OWASP Zed Attack Proxy](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project), or ZAP for short.

1. Please download and install ZAP.
2. Run ZAP. It will ask if you want to persist the ZAP Session.
3. Select `No, i do not want to persist this session at this mement in time` and uncheck `Remember my choice and do not ask me again`.
4. Click `Start`.
5. On the top right, find the icon `Open the browser you've chosen in the Quick Start tab pre-configured to proxy trough ZAP`. In my case it had the firefox icon.
6. Navigate to [http://localhost:5000/user/login](http://localhost:5000/user/login)
7. Login with the credentials of the user you created.
8. On `ZAP` go to the `History` tab in the bottom half of the window.
9. Find the `/user/welcome` request.
10. Go to the `Request` tab in the top half of the window.
11. On the header section you can see the cookie being sent like `Cookie: session=eyJrZXkiOiJHSDFWdThPbFdKRExWbU9ZTGY2SkJJMXJ5NUZNRlIwNVhoWTUwanFwZUxRIn0.XXsIUA.nNZ8EN3ty3HfsUjzTrEKZ9mzNPQ`
12. Copy the cookie value.
13. Go ahead and change the password in [http://localhost:5000/user/change_password](http://localhost:5000/user/change_password)
14. Once again click on`Open the browser you've chosen in the Quick Start tab pre-configured to proxy trough ZAP`. In my case it had the firefox icon.
15. In the new browser confirm you are not logged in by going to [http://localhost:5000/user/welcome](http://localhost:5000/user/welcome)
16. You should get redirected to the login page.
17. On `ZAP` click on `Set break on all requests and responses`. Should be a green circle icon.
18. On your unauthenticated browser, go to [http://localhost:5000/user/welcome](http://localhost:5000/user/welcome).
19. On `ZAP` insert the cookie value copied in step 11 in the headers section of the breakpoint.
20. On the top click on `Submit and continue to next break point`. Which will look like a play icon.

As you can see even after the user changed their password, we were able to log in using the session value captured previously successfully performing a session hijacking attack.

**Proceed to [next section](https://github.com/nxvl/secure-coding-with-python/tree/5.2-broken-deauthentication/fix)**

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
* [5.3-broken-deauthentication/code](https://github.com/nxvl/secure-coding-with-python/tree/5.3-broken-deauthentication/code) 
* [5.3-broken-deauthentication/test](https://github.com/nxvl/secure-coding-with-python/tree/5.3-broken-deauthentication/test)
* [5.3-broken-deauthentication/fix](https://github.com/nxvl/secure-coding-with-python/tree/5.3-broken-deauthentication/fix)

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

### 9. XML External Entities (XXE)
* [9-xxe/code](https://github.com/nxvl/secure-coding-with-python/tree/9-xxe/code) 
* [9-xxe/test](https://github.com/nxvl/secure-coding-with-python/tree/9-xxe/test)
* [9-xxe/fix](https://github.com/nxvl/secure-coding-with-python/tree/9-xxe/fix)

### 10. Sensitive Data Exposure
* [10-sensitive-data-exposure/code](https://github.com/nxvl/secure-coding-with-python/tree/10-sensitive-data-exposure/code) 
* [10-sensitive-data-exposure/test](https://github.com/nxvl/secure-coding-with-python/tree/10-sensitive-data-exposure/test)
* [10-sensitive-data-exposure/fix](https://github.com/nxvl/secure-coding-with-python/tree/10-sensitive-data-exposure/fix)
