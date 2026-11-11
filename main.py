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

def clear_screen():
    os.system("cls")
    
def game():
    #список настроек присваивается переменной
    setup_list  = setups.setup_2() 
    word        = setup_list[0]
    word_secure = setup_list[1]
    enabled     = setup_list[2]
    letter      = ""
    counter     = setup_list[3]
    
    while enabled:
        clear_screen()
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
            clear_screen()
            print(f"Победа! Загаданное слово: {word}")
            enabled = False
            
        if counter <= 0:
            clear_screen()
            print("Вас вздёрнули на рее!")
            enabled = False
            
game()