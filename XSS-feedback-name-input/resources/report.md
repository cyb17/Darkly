# Insecure name input on the feedback page

## How do we find the breach ?

We identified that the name input don't escape correctly special characters : '<' and '>'.
When we typed '<' in the name input, a flag appeared, so we tried some XSS injections, and it worked (ex: `\<a onmouseover="alert(document.cookie)"\>xxs link\</a\>`).

## Vulnerability Identified

Cross Site Scripting (XSS): a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. 

## How to avoid the breach ?

- Escape correctly user input data.
- Sanitize HTML if needed