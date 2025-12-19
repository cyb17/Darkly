# Recover mail default value

## How do we find the breach ?

When submitting an empty password recover form with an empty input, we observed in the request payload that this form had a default email value : `webmaster@borntosec.com`. By modifying this value and resending the request, we got the flag.

## How to exploit the breach ?

This sensitive information can be used by an attacker to explore other vulnerabilities (e.g., brute‑force login attacks). It can become critical if the backend does not verify email ownership before performing an important action.

## How to avoid the breach ?

- Never trust user input, always verify and validate it before any action. 
- Do NOT pre-fill sensitive data as default values.