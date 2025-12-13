# Title

## Observation

Navigation to pages other than Home appears to rely on the page parameter:

index.php?page=home


User input provided via this parameter is processed without proper validation.

## Vulnerability Identified

The application directly uses the page parameter to load files.
This behavior exposes the application to both Path Traversal and Local File Inclusion (LFI) vulnerabilities.

### vulnerability 1

By manipulating the page parameter, directory traversal sequences are processed, allowing access to files located outside the intended web directory.

Impact:

Access to sensitive system files

Disclosure of server and environment information

### vulnerability 2

The application includes files based on user input without restriction.
This allows unintended local files to be included and interpreted by the server.

Impact:

Disclosure of application source files

Exposure of credentials or secrets

Increased attack surface for further exploitation

## How to exploit the breach (conceptual)

An attacker can abuse the lack of input validation on the page parameter to:

Traverse directories outside the web root

Include unauthorized local files

Access sensitive information

🛠 Security issues involved

Missing server‑side input validation

Unsafe dynamic file inclusion

Lack of access control

✅ Recommended fix

Validate user input server‑side

Replace dynamic file inclusion with a strict whitelist of allowed pages

Prevent directory traversal patterns (../ and encoded variants)

Use fixed base paths for file loading