2. #Email Validation using Regex
import re
email = input("Enter yor email address:")
pattern = '^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z0-9]+\\.[a-zA-Z]{2,3}$'
if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")