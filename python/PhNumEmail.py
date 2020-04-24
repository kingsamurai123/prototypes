#for modules
import re, pyperclip


#reg expression for phone numbers
phoneRegex = re.compile(r'''
# (
# ([+91\s]*) #for +91 code
# (\d{10})+  #for ten digit phone number
# )

(\d{10})

''',re.VERBOSE)


#reg expression for email
emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+             # name part
@                           # @ sysmbol
[a-zA-Z0-9_.+]+             # domain part


''',re.VERBOSE)


# Get the text off the clipboard
text = pyperclip.paste()


#Extract email and phone number
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)


allNumbers = []
for phoneNum in extractedPhone:
    allNumbers.append(phoneNum)

# print(allNumbers)
results = '\n'.join(allNumbers) +'\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
# pyperclip.pause()