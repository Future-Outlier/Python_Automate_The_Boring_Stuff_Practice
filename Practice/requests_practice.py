# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
# the above can make you search HTTP_status_codes
import requests
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(type(res))
# if we download successful, we will get none object, else we will return error name
# and terminate the program.
print(res.raise_for_status())
print(res.status_code)
print(requests.codes.ok)
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])