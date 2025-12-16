# Insecure I_am_admin cookie

## How do we find the breach ?

We found that there was a cookie named "I_am_admin", it was hashed using MD5 and had a value of "false", we tried to replace "false" with "true", then send the request, and we got the flag.

## Vulnerability Identified :

- Broken Access Control: Users can gain elevated privileges by modifying a client-controlled cookie.

- Insecure Hash Usage: The application uses an insecure hash function (MD5) without salting or signing, which allows attackers to easily crack or guess the original value.

- Client-Side Trust: Authorization decisions rely on client-supplied data.

## Recommended Fix

- Apply secure cookie attributes (HttpOnly, Secure, SameSite).
- Avoid insecure hash function such as MD5.
- Use a secure authentication mechanism with server-side authorization checks, such as properly implemented sessions or signed JWTs.
