# Insecure use of a link present in NSA image

## How do we find the breach ?

We discovered a link on the NSA image. When clicking it, the URL contained a src parameter, and an `<object data="http://192.168.56.102/images/nsa_prism.jpg"></object>` element appeared in the source code. After several tests, we observed that the `data` attribute of the `<object></object>` tag was controlled by user input. Since the browser loads the resource specified by this attribute, we were able to supply a `data: URI scheme`, causing the browser to render and execute our payload as an embedded inline resource ([Learn more about URI scheme](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes)).

With `src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnaGknKTs8L3NjcmlwdD4=`, a base64-encoded version of `<script>alert('hi');</script>`, we found the flag.


## How to exploit the breach ?

Cross Site Scripting (XSS): a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. 

## How to avoid the breach ?

- Never inject user input directly into attributes like object.data, iframe.src, img.src.
- Don't let the browser loads resource.
- Restrict allowed URI schemes
- Validate and normalize user input.

