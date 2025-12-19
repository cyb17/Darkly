# Insecure I_am_admin cookie

## How do we find the breach ?

We found that there was a cookie named "I_am_admin", it was hashed using MD5 and had a value of "false", we replaced "false" with "true", then send the request, and we got the flag.

## How to exploit the breach ?

An attacker can steal the authentication cookie by capturing network traffic (due to the absence of HTTPS), by using JavaScript in the presence of an XSS vulnerability (HttpOnly=false), or by exploiting cross-site requests (SameSite=None).
Once obtained, the attacker can reuse this cookie to send requests as a legitimate user.

Additionally, because the authentication logic relies on a predictable cookie value (e.g. MD5(true)), the attacker can forge or modify the cookie without stealing it, resulting in a complete authentication bypass

Some vulnerability description :
- Broken Access Control: Users can gain elevated privileges by modifying a client-controlled cookie.
- Insecure Hash Usage: The application uses an insecure hash function (MD5) without salting or signing, which allows attackers to easily crack or guess the original value.
- Client-Side Trust: Authorization decisions rely on client-supplied data.

## How to avoid the breach ?

- Apply secure cookie attributes (HttpOnly, Secure, SameSite).
- Avoid weak hash function such as MD5.
- Use a secure authentication mechanism with server-side authorization checks, such as properly implemented sessions or signed JWTs.
