# Task 1

days = {
    1:'Monday',
    2:'Tuesday',
    3:'Wednesday',
    4:'Thursday',
    5:'Friday',
    6:'Saturday',
    7:'Sunday'
}
i= int(input('Enter the number from 1 to 7: '))
if 0 < i <= 7:
    print(days[i])
else:
    print('Error')

# Task 2

my_cat ={
    'name':'Rudolf',
    'age':2,
    'breed':'Persian',
    'weight':'3kg'
}

# Task 3

a = input('Enter the text: ')
dict = {}
for i in a:
    if i == ' ':
        continue
    else:
        dict[i] = a.count(i)

print(dict)

# Extra task

txt = "<h1>The Crushing Bore</h1>" \
      "<p>By Chris Mills</p>" \
      "<h2>Chapter 1: The dark night</h2>" \
      "<p>It was a dark night. Somewhere, an owl hooted. The rain lashed down on the ...</p>" \
      "<h2>Chapter 2: The eternal silence</h2>" \
      "<p>Our protagonist could not so much as a whisper out of the shadowy figure ...</p>" \
      "<h3>The specter speaks</h3>" \
      "<p>Several more hours had passed, when all of a sudden the specter sat bolt upright and exclaimed, 'Please have mercy on my soul!'</p>"

tags = ['<p>','</p>','<h1>','</h1>','<h2>','</h2>','<h3>','</h3>']
print(txt)
for item in tags:
    while item in txt:
        for i in txt:
            start = txt.find('<')
            stop = txt.find('>')
            txt = txt.replace(txt[start:stop + 1], '')
print(txt)
