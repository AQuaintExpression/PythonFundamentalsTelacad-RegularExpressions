import re

urls = '''
https://www.google.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

#putem captura anumite informatii din string punandu-le intr-un grup
#asta ne lasa sa apelam functia grup pe match si ne da access direct la 
#informatia dorita


#group 0 este intreg patternul
#group 1 este patternul din primul set de paranteze -- "www."
#group 2 este patternul din al 2-lea set de paranteze "cel putin un caracter"
#group 3 este patternul din al 3-lea set de paranteze ". urmat de cel putin un caracter"

matches = pattern.finditer(urls)
for match in matches:
    print(match.group(0), match.group(1), match.group(2), match.group(3))


#mai jos o sa inlocuim informatia din urls cu informatia din grupurile 2 si 3 --> adica scapam de https://www.
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)