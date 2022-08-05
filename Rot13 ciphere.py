def rot13(message):
    encode = []
    string = ""
    others_signs =["!","@","#","$","%","^","&","*","(",")","+","=","_","-","1","2","3","4","5","6","7","8","9","0","{","}","[","]",":","\"",";","\'","<",">",",",".","|","\\","`","~"," "]
    lower_case_one = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'] 
    lower_case_two =['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_case_one = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'] 
    upper_case_two=['N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in message:
        if i in lower_case_one:
            x = lower_case_one.index(i)
            encode.append(lower_case_two[x])
        elif i in lower_case_two:
            x = lower_case_two.index(i)
            encode.append(lower_case_one[x])
        elif i in upper_case_one:
            x = upper_case_one.index(i)
            encode.append(upper_case_two[x])
        elif i in upper_case_two:
            x = upper_case_two.index(i)
            encode.append(upper_case_one[x])
        elif i in others_signs:
            encode.append(i)
    return string.join(encode)