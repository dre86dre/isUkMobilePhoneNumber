# This function isUkMobilePhoneNumber() checks to see if an UK mobile phone number is in a string, returning either True or False.
# This code checks for both '+447' and '07' formats.

def isUkMobilePhoneNumber(text):
    # This code block checks for mobile numbers starting with the '+447' format
    # This code first checks to see if the text starts with '+447' and the lengh is 13 characters
    # It then runs a for loop to check that the last 12 characters in the text consist of only numeric characters.

    if text.startswith('+447') and len(text) == 13:
        for i in range(1, 13):
            if not text[i].isdecimal():
                return False
        return True

    # This code block checks for mobile numbers starting with the '07' format
    # This code first checks to see if the text starts with '07' and the lengh is 11 characters
    # It then runs a for loop to check that the last 9 characters in the text consist of only numeric characters.
    elif text.startswith('07') and len(text) == 11:
        for i in range(2, 11):
            if not text[i].isdecimal():
                return False
        return True
    
    else:
        return False

message = "Call me on +447377427818 tomorrow. 415-555-9999 is my office line. But +447939939049 is my alternative mobile number. Also, try 07700123456 or 07123456789."

# This for loop iterates a chunk of 11 and 13 characters starting from 0 to see whether it matches the 
# '+447' or '07' mobile phone number pattern, and if so, prints the chunk.
for i in range(len(message)):
    for lengh in (11, 13):
        chunk = message[i:i+lengh]
        if isUkMobilePhoneNumber(chunk):
            print('Phone number found: ' + chunk)
print('Done')