# Secure Coding with Python.

## Chapter 2: SQL Injection
### Requirement
For our marketplace application, we first decide to allow the upload of Listings, just text. We will 
worry about users later, since we want to focus on getting the DB and Models setup without needed to worry about 
authentication and session management at this point.

### Setting up the DB
First we need to install postgresql, you can do that with your preferred package manager, for this tutorial we will be
using postgres 11.4. After installing you would probably need to init the db:
```bash
> initdb /usr/local/var/postgres
```
*Note*: on linux you might need to run the command as root or use sudo.

Then we create the `marketplace` database:
```bash
> createdb marketplace
```
*Note*: on linux you might need to run the command as postgres user by prepending `sudo -u postgres` to the command.

Then we need to install the python driver for python, which comes as the `psycopg2` package.
```bash
> pip install psycopg2 
```
or
```bash
> pip install -r requirements.txt
```
*Note*: On OSX if you installed postgres from homebrew, you might need to prepend 
`LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib"` to the command in order to install correctly.

### Development
Since the application will need some more configuration we change the `marketplace/__init__.py` to make use of the 
`create_app` factory function. We add the DB connection functions into `marketplace/db.py` and add the factory function. 
We also add the DB schema in `schema.sql` and add a flask command to init the DB, which we run with:
```bash
> python -m flask init-db
```

### Vulnerability
Since we are generating the SQL to insert the new listing in a very unsecure way, we can insert SQL commands that will 
be run in the DB. For example if we insert `'` as title or description we will get 
`psycopg2.errors.SyntaxError: INSERT has more target columns than expressions LINE 1: INSERT INTO listings (title, description) VALUES (''', ''') ^` 
instead of a success.

We can for example get the postgresql version or any other SQL function result, to check that out, insert 
`injection', (select version()))-- -` as the title. When we do so, the SQL that's going to be executed will be the 
following:

```sql
INSERT INTO listings (title, description) VALUES ('injection', (select version()))-- -', 'ignored description')
```

As it can be seen, the inserted title will be `injection` and the description will be the result of the 
`select version()` command, or any other command we wish to insert there, including dropping the DB.

**Proceed to [next section](https://github.com/nxvl/secure-coding-with-python/tree/2.1-sql-injection/test)**

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
* [4.1-broken-authentication/code](https://github.com/nxvl/secure-coding-with-python/tree/4.1-broken-authentication/code) 
* [4.1-broken-authentication/fix](https://github.com/nxvl/secure-coding-with-python/tree/4.1-broken-authentication/fix)
* [4.2-broken-authentication/fix](https://github.com/nxvl/secure-coding-with-python/tree/4.2-broken-authentication/fix)

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