import re

class EmailAddressParser:
    
    email_regex = re.compile(r"([A-z0-9]+[.-_])*[A-z0-9]+@[A-z0-9-]+(\.[A-z]{2,})+") #email format
    
    def __init__(self, email):
        self.email= email
        

    def parse(self):
        email_addresses= re.split(r',|\s', self.email) #splits email addresses by whitespace separation
        email_list= set() #creates list of unique parsed emails
        for email in email_addresses:
            if self.email_regex.fullmatch(email): 
                email_list.add(email) #add() : adds an element to the set only if it doesn't already exist

        return sorted(list(email_list))
            