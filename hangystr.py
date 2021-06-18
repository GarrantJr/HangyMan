text = 'Hello'

translate = ''

for i in range(len(text)):
    letter = input(':')
    if letter in text:
        num = text.find(letter)
        print(num)

        translate = translate + letter
        print(translate)
        if translate == text:
            print('success')
            exit()