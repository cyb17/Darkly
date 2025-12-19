# Insecure file upload feature

## How do we find the breach ?

We tried to upload files with different extensions and identified that JPG and JPEG were accepted. Then, we modified the `Content-Type` of the request in Firefox to image/jpg while actually sending a PHP script. We found the flag in the response.

## How to exploit the breach ?

The server trusts client-side data and seems to verify only the `Content-type` header instead of the actual file content.
By modifying headers, an attacker can upload and store malicious code on the server, and if the file is stored in a web-accessible directory, he can then execute it.

## How to avoid the breach ?

- Make a whitelist of acceptable extension.
- Do NOT trust the Content-type header, verify the real file content.
- Uploaded files should not be executable, and should serve as static files.

