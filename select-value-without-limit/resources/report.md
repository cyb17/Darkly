# Select value without limit

## How do we find the breach ?

On the survey page, we observed that we could modify the select option’s value to anything. The data did not seem to be verified on the server side. When we entered a large number, we got the flag.

## Vulnerability Identified

User input was not correctly verified at the server side.

## How to avoid the breach ?

- Never trust user input.
