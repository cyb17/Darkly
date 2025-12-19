# Request referer and user-agent headers

## How do we find the breach ?

The URL of the copyright page seemed very suspicious : `http://192.168.56.102/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f`, there must be something here, so we looked at the source code. There were some comments looked like a hint :

```html
<!--You must come from : "https://www.nsa.gov/".-->
<!--Let's use this browser : "ft_bornToSec". It will help you a lot.-->
```

So we tried to send a request with curl using custom header : `curl -v --silent --header "Referer: https://www.nsa.gov/" --header "User-Agent: ft_bornToSec" "http://192.168.56.102/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f"`, then we found the flag in the response.

## How to exploit the breach ?

The critical issue is that the server trusts client‑side headers and uses them to make security decisions. Since an attacker can modify request headers, this trust can be abused to exploit the application.

## How to avoid the breach ?

Any data sent by the client can be modified by the client (headers, cookies, body, URL, method), so we must treat client-side data as informational, not authoritative.

