## Vulnerabilitiy Description :  

- Account enumeration : doing some tests in order to collect max user informations usefull for a brute force attack. 

- Weak password : A password that is short, predictable, commonly used, or found in leaked databases, making it easy to guess or crack.

- Brute force attack : An attack where the attacker tries all possible combinations or a list of common passwords until the correct one is found. Includes dictionary attacks and full character‑space brute force.

## Exploit

-> click signin  
-> click i forgot my password  
-> click submit
-> mail information "webmaster@borntosec.com" found in the response of the submit request  
-> we created a brute force attack script to try to log in with webmaster  

## Patch

-> Implement server-side input validation and avoid returning user account information when an error occurs.   
-> make the password stronger : long + random + unique.  