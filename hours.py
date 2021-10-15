my_string = "http://www.codewars.com/kata/"

if 'https' in my_string:
    token=my_string.split('https://')[1].split('.')[0]
elif 'http'in my_string:
    token=my_string.split('http://')[1].split('.')[0]
elif 'http://www' in my_string:
    token=my_string.split('http://www.')[1].split('.')[0]
#elif 'www' in my_string:
#    token=my_string.split('www.')[1].split('.')[0]


print(token)