# Insecure third party redirection

## How do we find the breach ?

When looking at third party link's source code at the bottom of the site, a query parameter "site" was used. We tried to enter something else than the original resource link, the flag appeared.

## How to exploit the breach ?

The redirection was controlled by user input, there were no validation and verifications of redirection data, user can be redirected to an evil website.

## How to avoid the breach ?

- Validate the redirection URL at the server side.