import random

word_list = ['knee', 'knife', 'knock', 'adapt', 'know', 'affect', 'land', 'afford', 'lap', 'large', 'last', 'borrow', 'map', 'margin', 'budget', 'mark', 'market', 'campus', 'nerve', 'civil', 'oppose', 'deal', 'porch', 'port', 'pose', 'quit', 'elite', 'quote', 'recipe', 'email', 'emerge', 'refuse', 'regard', 'scope', 'score', 'fiber', 'scream', 'screen', 'field', 'script', 'tactic', 'forest', 'tail', 'forget', 'form', 'talent', 'formal', 'uncle', 'gear', 'gender', 'gene', 'video', 'view', 'viewer', 'holy', 'weapon', 'home', 'wear', 'image', 'week', 'impact', 'year', 'income', 'yell', 'yellow', 'joy', 'judge', 'equal', 'lord', 'king', 'france', 'cousin', 'will', 'move', 'speedy', 'friend', 'seem', 'make', 'denial', 'love', 'wisdom', 'answer', 'mean', 'freely', 'leave', 'stand', 'part', 'well', 'serve', 'gentry', 'sick', 'enter', 'count', 'good', 'young', 'youth', 'bear', 'father', 'face', 'frank', 'nature', 'haste', 'moral', 'paris', 'duty', 'look', 'time', 'long', 'steal', 'talk', 'return', 'hide', 'honour', 'like', 'pride', 'clock', 'true', 'minute', 'speak', 'tongue', 'obey', 'hand', 'place', 'proud', 'poor', 'praise', 'copy', 'follow', 'rich', 'royal', 'speech', 'always', 'say', 'hear', 'word', 'ear', 'grow', 'live', 'begin', 'heel', 'flame', 'lack', 'snuff', 'sense', 'expire', 'wish', 'honey', 'bring', 'home', 'hive', 'give', 'room', 'lend', 'fill', 'know', 'month', 'rest', 'debate', 'stock', 'exchange', 'note', 'sell', 'equity', 'large', 'liquid', 'attractive', 'guarantor', 'settlement', 'counter', 'dealer', 'different', 'attract', 'cover', 'interest', 'frequently', 'likely', 'trade', 'transfer', 'money', 'security', 'seller', 'buyer', 'agree', 'price', 'ownership', 'particular', 'company', 'market', 'range', 'small', 'individual', 'larger', 'world', 'include', 'insurance', 'pension', 'hedge', 'trader', 'physical', 'floor', 'method', 'known', 'open', 'offer', 'type', 'network', 'example', 'potential', 'specific', 'accept', 'match', 'sale', 'place', 'multiple', 'purpose', 'facilitate', 'provide', 'real', 'discovery', 'hybrid', 'location', 'flow', 'broker', 'order', 'post', 'maintain', 'spread', 'case', 'close', 'difference', 'tape', 'brokerage', 'firm', 'investor', 'play', 'important', 'role', 'program', 'electronic', 'computer', 'similar', 'purchase', 'drive', 'late', 'system']

def get_word():                           
    return random.choice(word_list)
    
def play(word):                           
    word_x = [i for i in '_' * len(word)] 
    guessed_letters = []                  
    tries = 6                             
    
    print("Let's play in a Hangman!")
    print('You have 5 tries and on the 6th the game ends.')
    print('Write a letter or a word:')
    while 0 < tries:
        s = input().lower()
        if not s.isalpha():
            print('You can put only letters. Try arain.')
            continue
        if s == word:
            print(f'Congrats you guessed the word {word.upper()}! You won!')
            break
        if s in guessed_letters:
            print('You already tried this letter. Try another one.')
            continue
        else:
            guessed_letters.append(s)
        for j in range(len(word)):
            if word[j] == s:
                word_x[j] = s
        print('Look what we got', ' '.join(word_x).upper())
        if word == ''.join(word_x):
            print(f'Congrats you guessed the word {word.upper()}! You won!')
            break
        if s not in word:
            tries -= 1
            print(display_hangman(tries))
        if tries == 0:
            print('You have no more tries...')
            print('We had a word: "', word.upper(), '"', sep='')
            print('Next time you will defenetrly guess it :)')
        else:
            print('Tries left:', tries)
def display_hangman(tries):
    stages = [  # final body
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, upper body, hands, one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, upper body, hands
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, upper body, hand
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head and upper body
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                #the start
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

word = get_word()
play(word)