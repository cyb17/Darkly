# Insecure file upload feature

## How do we find the breach ?

We tried to upload files with different extensions and identified that JPG and JPEG were accepted. Then, we modified the `Content-Type` of the request in Firefox to image/jpg while actually sending a PHP script. We found the flag in the response.

## Vulnerability Identified

The server trusts client-side data, it seems verify just Content-type header instead of file content.

## How to avoid the breach ?

- Don't trust the Content-type, verify also the file content.

