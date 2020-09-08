import re

emails = '''
johndoe@gmail.com
john.doe@university.edu
john-321-doe@my-work.net
'''


#extragere de patternuri cu grupuri
#daca dorim doar mailurile ".com" sau ".edu"
pattern = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu)')
matches = pattern.finditer(emails)

for match in matches:
    print(match)