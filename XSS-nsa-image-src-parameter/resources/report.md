# Insecure use of a link present in NSA image

## How do we find the breach ?

We found a link on the NSA image. When clicked, the URL contained a src parameter, and a `<object data="http://192.168.56.102/images/nsa_prism.jpg"></object>` appeared in the source code. After a few tests, we observed that the data attribute of the object was controlled by user input, and we could pass a `data:` URI to let the browser execute our script.

With `src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnaGknKTs8L3NjcmlwdD4=`, a base64-encoded version of `<script>alert('hi');</script>`, we found the flag.

## Vulnerability Identified

Cross Site Scripting (XSS): a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. 

## How to avoid the breach ?

- Never inject user input directly into attributes like object.data, iframe.src, img.src.
- Don't let the browser loads resource.
- Restrict allowed URI schemes
- Validate and normalize user input.

