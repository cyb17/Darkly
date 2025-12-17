# Weak password cracked by Brute force attack

## How do we find the breach ?

We tried to send an empty request in "I forget my password" page, we got a user mail in the request payload : `webmaster@borntosec.com`. We believed that "webmaster" was a user account, so we found a weak password file from the internet, and we created a brute force attack script, and then we begin the test, and it worked. Username was "webmaster" and password was "shadow".

## Vulnerability Identified :  

- Insecure default configuration : user personal mail was defined as default value in recover form.

- Weak password : A password that is short, predictable, commonly used, or found in leaked databases, making it easy to guess or crack.

- Brute force attack risk : An attack where the attacker tries all possible combinations or a list of common passwords until the correct one is found. Includes dictionary attacks and full character‑space brute force.

## How to avoid the breach ?

- Enforce strong password policies (long, random, and unique passwords).

- Never expose user data (such as email addresses or usernames) in frontend responses or error messages, as this facilitates user enumeration and brute-force attacks.

- Implement proper input validation and reject empty or malformed requests server-side.

- Add rate limiting and account lockout mechanisms to mitigate brute-force attempts.