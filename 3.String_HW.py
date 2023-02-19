import re
import string

a = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

b = a.lower().capitalize()

for i in re.findall(r'\.\s+[A-z]+', b, re.I):
    b = b.replace(i, i.title(), 1)

c = ''
for i in re.findall(r'\s+[A-z]+\.', b, re.I):
    c = c+i.replace('.', '')

b = b.replace('paragraph.', 'paragraph. '+c.replace(c[1], c[1].upper(), 1)+'.')

for a in re.findall(r'\Wiz\W', b, re.I):
    a1 = a.replace(a[2], 's')
    b = b.replace(a,a1,1)
print(b)

whitespace_count = 0
for i in re.findall(r'\s', b):
    whitespace_count += 1

print('Number of whitespace characters in this text =', whitespace_count)


