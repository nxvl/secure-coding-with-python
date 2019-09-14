# Secure Coding with Python.

## Chapter 3: Weak Password Storage
### Test
Every encryption algorithm can be theoretically cracked using brute-force attacks, this attack consist in trying multiple possible strings until one provides de desired hash. Said attacks are fairly expensive to perform as they take some time.

Given that we know the algorithm used for a hash we can create a very simple dictionary brute-force attack against the hash. We will be using the [RockYou](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) wordlist.

```text
> $ time python crackpass.py f75778f7425be4db0369d09af37a6c2b9a83dea0e53e7bd57412e4b060e607f7 rockyou.txt
Password is: supersecret
python crackpass.py  rockyou.txt  0.32s user 0.01s system 99% cpu 0.325 total
                                             
```

Now that's just 1 password, if we had to crack thousands of passwords, the effort starts getting significant. That's where rainbow tables kick in.
The [wikipedia definition](https://en.wikipedia.org/wiki/Rainbow_table) describes rainbow tables as: "A rainbow table is a precomputed table for reversing cryptographic hash functions, usually for cracking password hashes."

Let's try to mass crack:
#### 50 hashes
```text
> $ time python rainbow-crack.py rockyou-rainbow.txt hashes-50.txt
[...]
password for b'73d07a303cc50a5423ae72081cafe4e50a2fb1a0ef161d55e332e8533c5e25a0' is b"b'vane944218'"
password for b'2c2d908b313fb71b5592ae4a44dfad2dbedd1832915a97a547d58e4c09a8ee49' is b"b'Robert7681'"
python rainbow-crack.py rockyou-rainbow.txt   10.98s user 1.50s system 99% cpu 12.484 total
```

#### 100 hashes
```text
> $ time python rainbow-crack.py rockyou-rainbow.txt hashes-100.txt
[...]
password for b'37325783f2e3763b14f25d3a28edc90fbd08283fffa9b446d827ad60c0d19272' is b"b'raaces'"
password for b'6df380dbe975a3bb65a880360e84584fdacea1455c27aa7ffef9a4b639592259' is b"b'mattlvu'"
python crackers/rainbow-crack.py ~/Downloads/rockyou-rainbow.txt   10.83s user 1.52s system 99% cpu 12.367 total
```

#### 200 hashes
```text
> $ time python rainbow-crack.py rockyou-rainbow.txt hashes-200.txt
[...]
password for b'53ad0738f0356042ae89f837767078f39492fc9b29e60fe056be5cefa9e9b510' is b"b'shaiyshaiy'"
password for b'9459c1e60e359f9f646bfe92a3a1ff1167a3b6d816290d09a33cdf8a565b15c6' is b"b'kuizenga'"
python crackers/rainbow-crack.py ~/Downloads/rockyou-rainbow.txt   10.99s user 1.53s system 99% cpu 12.541 total
```

As can be seen with Rainbow tables the cracking time is fairly linear, it takes around 11s for almost any case, most of the time is probably spend on loading up the DB, which can be optimized, but for the sake of this example we have done on a non-ideal way.

**Proceed to [next section](https://github.com/nxvl/secure-coding-with-python/tree/3.2-weak-password-storage/fix)**

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

### 9. XML External Entities (XXE)
* [9-xxe/code](https://github.com/nxvl/secure-coding-with-python/tree/9-xxe/code) 
* [9-xxe/test](https://github.com/nxvl/secure-coding-with-python/tree/9-xxe/test)
* [9-xxe/fix](https://github.com/nxvl/secure-coding-with-python/tree/9-xxe/fix)

### 10. Sensitive Data Exposure
* [10-sensitive-data-exposure/code](https://github.com/nxvl/secure-coding-with-python/tree/10-sensitive-data-exposure/code) 
* [10-sensitive-data-exposure/test](https://github.com/nxvl/secure-coding-with-python/tree/10-sensitive-data-exposure/test)
* [10-sensitive-data-exposure/fix](https://github.com/nxvl/secure-coding-with-python/tree/10-sensitive-data-exposure/fix)
