'''
1. e-mail состоит из имени и доменной части, эти части разделяются символом "@";

2. доменная часть не короче 3 символов и не длиннее 256, является набором непустых строк, состоящих из символов a-z 0-9_- и разделенных точкой;

3. каждый компонент доменной части не может начинаться или заканчиваться символом "-";

4. имя (до @) не длиннее 128 символов, состоит из символов a-z0-9"._-;

5. в имени не допускаются две точки подряд;

6. если в имени есть двойные кавычки ", то они должны быть парными;

7. в имени могут встречаться символы "!,:", но только между парными двойными кавычками.
'''

def check_email(email):
    #1. e-mail состоит из имени и доменной части, эти части разделяются символом "@";
    assert isinstance(email,str)
    if email.find('@') == -1:
        return False
    if len(email.split('@')) != 2:
        return False
    username,domain = email.split('@')[0],email.split('@')[1]
    #2. доменная часть не короче 3 символов и не длиннее 256, является набором непустых строк, состоящих из символов a-z 0-9_- и разделенных точкой;

    if len(domain)<3 or len(domain)>= 256:
        return False
    if domain.find('.')==-1:
        return False
    import string
    for i in domain:
        if i not in string.digits+ '_-.'+string.ascii_letters.lower():
            return False
    #3. каждый компонент доменной части не может начинаться или заканчиваться символом "-";
    for i in domain.split('.'):
        if len(i)==0:
            return False
        if (i[0] == '-') or (i[-1] == '-'):
            return False
    #4. имя (до @) не длиннее 128 символов, состоит из символов a-z0-9"._-; (+ !,: из 7)
    if not username or len(username)>128:
        return False
    for i in username:
        if i not in string.digits+ '_-."!,:'+string.ascii_letters.lower():
            return False
    #5. в имени не допускаются две точки подряд;
    if username.find('..')!=-1:
        return False
    #6. если в имени есть двойные кавычки ", то они должны быть парными;
    if username.find('"') != -1:
        if (len(username.split('"'))%2) == 0:
            return False
    #7. в имени могут встречаться символы "!,:", но только между парными двойными кавычками.
    import re
    m = re.findall(r"\"[a-z0-9!:,._-]+\"", username)
    for i in username:
        if i in '!,:' and i not in ''.join(m):
            return False
    return True


#regex version
def check_email_regex(email):
    import re
    r = re.compile("(?!.*\.\.)(?:(?:\"(?:[a-z-0-9_!:,.])*\")|(?:[a-z-0-9_.]))+@[a-z0-9-]+\.[a-z0-9-_\.]+")
    if r.match(email):
        if len(email.split('@')) != 2:
            return False
        if len(email[:email.find('@')])<=128:
            domain_part=email[email.find('@')+1:]
            if len(domain_part)>=3 and len(domain_part)<=256:
                for i in domain_part.split('.'):
                    if len(i)==0:
                        return False
                    if (i[0] == '-') or (i[-1] == '-'):
                        return False
                return True
    else:
        return False
