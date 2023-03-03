from thai_citizen_id.validate import calculateCheckSum
from keyring import get_keyring
import keyring
from thai_citizen_id import extract

# from thai_citizen_id import


# print(validate("5787118773411"))
# print(validate("1103702392219"))
# print(validate("110370239221"))
# print(generate())
# print(extract("5787118773411"))
# print(extract("5787118773411"))
# print(extract("5787118773411"))

# thai_citizen_id


print(calculateCheckSum("123456789012"))
print(extract("1234567890121"))

print(calculateCheckSum("2660835443125"))
print(extract("2660835443125"))

print(calculateCheckSum("627099789013"))
print(extract("6270997890131"))
