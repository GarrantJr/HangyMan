import random

def play(hangyword):
    print(hangyword)
    hangyword, wordy = [letter for letter in hangyword], [letter for letter in hangyword]
    show = ['_' for letter in hangyword]
    lives = 8
    print(show)
    while '_' in show and lives >= 0:
    	try:
	        new = input().lower()
	        while new in hangyword:
	            show[hangyword.index(new)] = new
	            hangyword[hangyword.index(new)] = '_'
	    
	        print(show)
	        print('\n{} lives remaining\n'.format(lives))

	        lives -= 1
   
    	except:
    		print('Sorry.. Incorrect Format\n{} lives remaining\n'.format(lives))

        if lives < 0:
            print('Oops Failed\nThe word is {},{}'.format(wordy,''.join(wordy)))
        elif show == wordy:
            print('{}\n!!\t!! Congratulations !!\t!!\nGot Right in {} tries'.format(''.join(wordy),8-lives))
        # print(show)
        
    return show


with open('words.txt', 'r') as f3:
    # words = list(word for word in f3)
    word = random.choice(f3.readlines()).replace('\n','')

play(word.lower()) #Hangman by @jbs