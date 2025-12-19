# Select value without limit

## How do we find the breach ?

On the survey page, we observed that we could modify the select option’s value to anything. The data did not seem to be verified on the server side. When we entered a large number, we got the flag.

## How to exploit the breach ?

When a select input is not strictly validated server‑side, attackers can tamper with its value to bypass business logic or access controls by submitting values not intended by the application.

## How to avoid the breach ?

- Validate user input.
- Reject any unknown and unexpected values. 