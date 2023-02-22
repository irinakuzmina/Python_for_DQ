import re
import string


def normalize_case(q):
    b1 = q.lower().capitalize()

    for i1 in re.findall(r'\.\s+[A-z]+', b1, re.I):
        b1 = b1.replace(i1, i1.title(), 1)

    return b1


def add_new_sentence(t):
    c = ''
    for i2 in re.findall(r'\s+[A-z]+\.', t, re.I):
        c = c+i2.replace('.', '')

    t = t.replace('paragraph.', 'paragraph. '+c.replace(c[1], c[1].upper(), 1)+'.')
    return t


def correct_wrong_iz(p):
    for k in re.findall(r'\Wiz\W', p, re.I):
        k1 = k.replace(k[2], 's')
        p = p.replace(k, k1, 1)
    return p


def count_whitespace(f):
    whitespace_count = 0
    for j in re.findall(r'\s', f):
        whitespace_count += 1
    print('Number of whitespace characters in this text =', whitespace_count)


a = '''homEwork:
  tHis iz your homeWork, copy these Text to variable.

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

print(correct_wrong_iz(add_new_sentence(normalize_case(a))))

count_whitespace(correct_wrong_iz(add_new_sentence(normalize_case(a))))
