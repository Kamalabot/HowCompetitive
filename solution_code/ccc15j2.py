#How are feeling today, ccc15j2

sent = input("")

happy = ":-)"
sad = ":-("
h = sent.count(happy)
s = sent.count(sad)

if h == 0 and s == 0:
    print('none')

elif h == s:
    print('unsure')

elif h > s:
    print('happy')

else:
    print('sad')




def count_emo(sent: str, h_t, s_t) -> int:
    list_sent = sent.split('')
    h = 0
    s = 0
    for token in list_sent:
        if token == h_t:
            h += 1
        if token == s_t:
            s += 1
    return h, s
