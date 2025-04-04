import random
import string

def make_password(length):
    if length < 4:
        return "The password length has to be 4 or more"
    
    lowerbox = string.ascii_lowercase
    upperbox = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = lowerbox + upperbox + digits + symbols

    password = [
        random.choice(lowerbox),
        random.choice(upperbox),
        random.choice(digits),
        random.choice(symbols),
    ]

    password += random.choices(all_chars,k=length-4)
    random.shuffle(password)
    stirng_password="".join(password)
    return stirng_password


password_number =int(input("생성할 비밀번호 자리수를 입력하시오:"))
print("무작위로 생성된 패스워드:", make_password(password_number))
    