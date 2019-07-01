def mail(s):
    if s.count('@mail.com') == 1:
        return True
    else:
        return False
print(mail('email@mail.com'))
print(mail('something@invalid'))
print(mail('wrong_email.com'))
