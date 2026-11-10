import os, setups #подключаем наш файл setups.py

def main():
    pass

''' Данный код в файле setups.py
def setup_1():
    word        = "test"
    word_secure = ["_"] * len(word)
    enabled     = True
    letter      = ""
    counter     = 6
    return [word, word_secure, enabled, letter, counter]
'''

def game():
    #список настроек присваивается переменной
    setup_list  = setups.setup_1() 
    word        = setup_list[0]
    word_secure = setup_list[1]
    enabled     = setup_list[2]
    letter      = setup_list[3]
    counter     = setup_list[4]
    
    def game_cycle():
        while enabled:
            os.system("clear")
            print(f"Осталось {counter} попыток.")
            
            print(' '.join(word_secure))
            letter = input("Введите букву: ")
            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        word_secure[i] = letter
            else:
                counter -= 1
        
            if "_" not in word_secure:
                os.system("clear")
                print(f"Победа! Загаданное слово: {word}")
                enabled = False
                
            if counter <= 0:
                os.system("clear")
                print("Вас вздёрнули на рее!")
                enabled = False
                
    game_cycle()
game()