morse = {'A' : '.-', 'B' : '-...','C' : '-.-.','D' : '-..',
         'E' : '.', 'F' : '..-.', 'G' : '--.','H' : '....',
         'I' : '..','J' : '.---', 'K' : '-.-','L' : '.-..',
         'M' : '--', 'N' : '-.','O' : '---','P' : '.--.',
         'Q' : '--.-', 'R' : '.-.','S' : '...','T' : '-',
         'U' : '..-', 'V' : '...-', 'W' : '.--','X' : '-..-',
         'Y' : '-.--','Z' : '--..',' ' : '/','1' : '.----',
         '2' : '..---','3' : '...--','4' : '....-',
         '5' : '.....','6' : '-....', '7' : '--...',
         '8' : '---..','9' : '----.','.' : '.-.-.-',
         ',' : '--..--','?' : '..--..','!' : '..--.',
         ':' : '---..','"' : '.-..-.',"'" : '.----.',
         '=' : '-...-'}
def morse_out(text_input,morse):
     morse_output = ''
     for i in text_input:
          x = morse.get(i.upper())
          morse_output += (x+' ')
     print(morse_output)

def text_out(morse,morse_input):
     morse_input += ' '
     alphabets = []
     morse_values = []
     text_output = ''
     morse_word = ''
     for i in morse.keys():
          alphabets.append(i)
     for i in morse.values():
          morse_values.append(i)
     for i in range(len(morse_input)):
          if morse_input[i] == ' ':
               #if morse_input[i+1] == '/':
                   # text_output += ' '
               if morse_word != '':
                    index = morse_values.index(morse_word)
                    text_output += alphabets[index]
                    morse_word = ''
          else:
               if morse_input[i] == '/':
                    text_output += ' '
               else:
                    morse_word += morse_input[i]
     print(text_output.capitalize())

    
while True:
     choice = int(input('''
Enter :-
1 - Transalate text to morse
2 - Transalate morse to text
3 - Quit
'''))
     if choice == 1:
          text_input = input('Enter text/(0011 to stop) :')
          if text_input == '0011':
               break
          morse_out(text_input,morse)
     elif choice == 2:
          morse_input = input('Enter/0011 to stop :')
          if morse_input == '0011':
               break
          text_out(morse,morse_input)
     elif choice == 3:
          break
     else:
          print('Wrong choice')
          continue
