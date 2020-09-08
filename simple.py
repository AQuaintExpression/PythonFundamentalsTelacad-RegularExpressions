import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

google.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''

sentence = 'Start a sentence and then bring it to an end'



# o sa lucram cu siruri raw in principal
# 1. exemplu pattern.compile -- se foloseste atunci cand folosim un patter in mai multe cautari

#functiile pe care le-am invatat deja o sa functioneze si pentru patternuri

pattern = re.compile(r'Start')
matches = pattern.search(sentence)
print(matches)

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# rezultatul este:
"""
<re.Match object; span=(1, 4), match='abc'>
"""

# 2. anumite caractere speciale trebuiesc a fi folosite cu un "\" in fata daca vrem a le folosi in patternuri
# ele sunt: . ^ $ * + ? { } [ ] \ | ( )

# a.
pattern = re.compile(r'.')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

"""
    o sa returneze absolut fiecare caracter
"""

# b.
pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

"""
    o sa returneze fiecare aparitie a caracterului "."
    similar pentru oricare dintre caracterele de pe linia 52.
"""


# 3. exemplu /b -- word boundary (caractere separate de spatii)
# o sa cautam aparitiile lui Ha unde este delimitat la inceput

pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


# 4. inceput/sfarsit de sir --> ^/$

pattern = re.compile(r'^')
matches = pattern.finditer(sentence)

for match in matches:
    print(match)

# returneaza <re.Match object; span=(0, 0), match=''> adica inceputul stringului

# 5. exemple practice:
# a. gasirea nr de telefon in text_to_search


pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# daca am fi vrut doar nr separate de "-" sau "."
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[.-]\d\d\d\d')

#doar nr care incep cu 800 sau 900:
# pattern = re.compile(r'[89]00[-.]\d\d\d[.-]\d\d\d\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# 6. character sets [] --> o sa se faca match pe orice este cuprins intre paranteze patrate:
#doar nr care incep cu 800 sau 900:
pattern = re.compile(r'[89]00[-.]\d\d\d[.-]\d\d\d\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


# 7. "^" intr-un character set
# [^ab] --> o sa faca match pe orice inafara de a sau b
# in alte cuvinte negheaza un character set
# doar nr care incep cu orice altceva in afara de 8 sau 9:
pattern = re.compile(r'[^89]\d\d[-.]\d\d\d[.-]\d\d\d\d')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match) 


# cuantificatori: 
"""
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)
"""

# vezi emails.py