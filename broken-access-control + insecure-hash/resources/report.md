## Vulnerabilitiy Description :  

- Broken Access Control: Users can gain elevated privileges by modifying a client-controlled cookie.

- Insecure Hash Usage: The application uses an insecure hash function (MD5) without salting or signing, which allows attackers to easily crack or guess the original value.

- Client-Side Trust: Authorization decisions rely on client-supplied data.


## Exploit

-> open dev tools  
-> go to Application  
-> go to Cookies  
-> there is a cookie named "I_am_admin" whose value is "false", stored as MD5, replace this value with MD5 hash of "true"  
-> and then we can send request as administrator  

## Patch

-> Apply secure cookie attributes (HttpOnly, Secure, SameSite).  
-> Avoid insecure hash function such as MD5.  
-> Use a secure authentication mechanism with server-side authorization checks, such as properly implemented sessions or signed JWTs.  