def censor(data):
    words = ['Java', 'C#', 'Rubby', 'PHP']
    j = 0
    check_list = data.split()
    for i in check_list:
        if i in words:
            check_list[j] = '****'
        j += 1
    print(' '.join(check_list))
censor("Java jest super, ale PHP Java jest najlepszy!")

def censor_1(tekst):
    sentence = tekst.split()
    not_allowed_1 = ['Java', 'C#', 'Ruby', 'PHP']
    replaced_1 = '****'
    if 'Java' in sentence:
        index_1 = sentence.index('Java')
        sentence[index_1] = replaced_1
    if 'C#' in sentence:
        index_2 = sentence.index('C#')
        sentence[index_2] = replaced_1
    if 'Ruby' in sentence:
        index_3 = sentence.index('Ruby')
        sentence[index_3] = replaced_1
    if 'PHP' in sentence:
        index_4 = sentence.index('PHP')
        sentence[index_4] = replaced_1
    return " ".join(sentence)

print(censor_1("Java PHP Ruby C# to Java fajny język programowania"))