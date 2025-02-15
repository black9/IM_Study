def is_hex(c):
    is_numeric = ord('0') <= ord(c) <= ord('9')
    is_lowercase = ord('a') <= ord(c) <= ord('f')
    is_uppercase = ord('A') <= ord(c) <= ord('F')

    return is_numeric or is_lowercase or is_uppercase

def hex_to_dec(c):
    is_numeric = ord('0') <= ord(c) <= ord('9')
    is_lowercase = ord('a') <= ord(c) <= ord('f')
    is_uppercase = ord('A') <= ord(c) <= ord('F')

    if is_numeric:
        return ord(c) - ord('0')
    elif is_lowercase or is_uppercase:
        return ord(c.lower()) - ord('a') + 10

string = input('숫자를 입력하세요')
if is_hex(string):
    print('16진수입니다. 10진수로 {0} 입니다.'.format(hex_to_dec(string)))
else:
    print('16진수가 아닙니다.')

'''
##또 다른 예제

num=input("16진수 한글자 입력: ")

if('0'< num and num < '9') or ('a'<= num and num <= 'f') or ('A' <= num and num <='F'):
    print("10진수 ==> ", int(num, 16))
else:
    print("16진수 아님")

''
