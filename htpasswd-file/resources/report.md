# htpasswd file exposed via robots.txt

## How do we find the breach ?

A `/whatever` directory was disclosed via the robots.txt file.
Inside this directory, we found an .htpasswd file containing the following credentials:
`root:437394baff5aa33daa618be47b75cb49.`

We then discovered an admin login page at http://192.168.56.102/admin/.
By cracking the hash from the `.htpasswd` file, we were able to authenticate as the root user and retrieve the flag.

**.htpasswd** : It is a file and a mechanism used to protect a resource, requiring HTTP Basic Authentication.

## How to exploit the breach ?

On a real website, this file should never be exposed, as an attacker could use the information inside it to access a protected resource.

## How to avoid the breach ?

It's better to store this file outside the web root, or configure the server to deny access to sensitives files. 