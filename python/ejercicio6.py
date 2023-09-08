a = ""
length = len(a)
print(length)
print('\n')
b = "it's ok"
length =len(c)
print(length)
print('\n')
c = 'it\'s ok'
length = len(c)
print(length)
print('\n')
d = """hey"""
length = len(d)
print(d)
print('\n')
e = '\n'
length = len(e)
print(length)
print('\n')
def is_valid_zip(zip_code):
    return (len(zip_code)==5 and zip_code.isdigit())
print('\n')
def word_search(doc_list, keyword):
    list=[]
    for statement,phrase in enumerate(doc_list):
        phrase=phrase.split()
        if keyword.lower() in [word.rstrip('.,').lower() for word in phrase]:
            list.append(statement)
    return list

print('\n')
def multi_word_search(doc_list, keywords):
    indices={}
    for keyword in keywords:
        indices[keyword]=word_search(doc_list,keyword)
    return indices
print('\n')

print('\n')
