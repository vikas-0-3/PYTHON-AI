import os
import pyttsx3
print("Hello user")
pyttsx3.speak("Hello user")
def func1():    
    n = input("")
    #for google chrome
    if((("not" in n and "open" in n) and ("google" in n or "chrome" in n)) or ("launch" in n and ("google" in n or "chrome" in n)) or ("run" in n and ("google" in n or "chrome" in n)) ):
        pyttsx3.speak("Okayy, not opening google chrome")
        func2()
    elif(("open" in n and ("google" in n or "chrome" in n)) or ("launch" in n and ("google" in n or "chrome" in n)) or ("run" in n and ("google" in n or "chrome" in n)) ):
        pyttsx3.speak("opening google chrome")
        os.system("google-chrome")
        func2()
    
    #for mozilla firefox
    if((("not" in n and "open" in n) and ("mozilla" in n or "firefox" in n)) or ("launch" in n and ("mozilla" in n or "firefox" in n)) or ("run" in n and ("google" in n or "chrome" in n)) ):
        pyttsx3.speak("Okayy, not opening mozilla firefox")
        func2()
    elif(("open" in n and ("mozilla" in n or "firefox" in n)) or ("launch" in n and ("mozilla" in n or "firefox" in n)) or ("run" in n and ("google" in n or "chrome" in n)) ):
        pyttsx3.speak("opening mozilla firefox")
        os.system("firefox")
        func2()


        #for browser
    elif((("open" in n or "run" in n or "launch" in n) and ("not" in n)) and ("browser" in n )):
        pyttsx3.speak("Okayy, not opening browser")
        func2()
    elif(("open" in n or "run" in n or "launch" in n) and ("browser" in n )):
        pyttsx3.speak("Which browser you want to open , google chrome or firefox ?")
        abc = input("Which browser you want to open , google chrome or firefox ? ")
        if("google" in abc or "chrome" in abc):
            pyttsx3.speak("opening google chrome")
            os.system("google-chrome")
            func2()
        elif("mozilla" in abc or "firefox" in abc):
            pyttsx3.speak("opening mozilla firefox")
            os.system("firefox")
            func2()
        else:
            pyttsx3.speak("Wrong choice")
            func2()


    #for vscode
    elif((("open" in n or "run" in n or "launch" in n) and ("not" in n)) and ("vscode" in n and "visual studio code" in n)):
        pyttsx3.speak("okay, Not opening visual studio code")
        func2()
    elif(("open" in n or "run" in n or "launch" in n) and ("vscode" in n)):
        pyttsx3.speak("opening visual studio code")
        os.system("code")
        func2()
    
    #for youtube
    elif((("open" in n or "run" in n or "launch" in n) and ("not" in n)) and ("youtube" in n)):
        pyttsx3.speak("okay, Not opening youtube")
        func2()
    elif(("open" in n or "run" in n or "launch" in n) and ("youtube" in n)):
        pyttsx3.speak("opening youtube")
        os.system("google-chrome https://www.youtube.com/")
        func2()

    #for gedit
    elif((("open" in n or "run" in n or "launch" in n) and ("not" in n)) and ("code" in n or "editor" in n)):
        pyttsx3.speak("okay, Not opening code editor")
        func2()
    elif(("open" in n or "run" in n or "launch" in n) and ("editor" in n or "code" in n)):
        pyttsx3.speak("opening code editor")
        os.system("gedit")
        func2()
    
    #for office
    elif((("open" in n or "run" in n or "launch" in n) and ("not" in n)) and ("office" in n or "libreoffice" in n or "libre" in n)):
        pyttsx3.speak("okay, Not opening libre office")
        func2()
    elif(("open" in n or "run" in n or "launch" in n) and ("office" in n or "libreoffice" in n or "libre" in n)):
        pyttsx3.speak("opening libreoffice")
        os.system("libreoffice")
        func2()


    #for  celluloid
    elif((("open" in n or "run" in n or "launch" in n or "play" in n) and ("not" in n)) and ("music" in n and "celluloid" in n and "player" in n)):
        pyttsx3.speak("okay, Not opening music player")
        func2()
    elif(("open" in n or "run" in n or "launch" in n) and ("music" in n or "celluloid" in n or "player" in n)):
        pyttsx3.speak("playing music")
        os.system("celluloid")
        func2()
  
    #for play music in celluloid
    elif((("open" in n or "run" in n or "launch" in n or "play" in n) and ("not" in n)) and ("music" in n and "celluloid" in n and "player" in n)):
        pyttsx3.speak("okay, Not playing music in music player")
        func2()
    elif(("open" in n or "run" in n or "launch" in n or "play" in n or "celluloid" in n) and ("music" in n or "celluloid" in n or "player" in n)):
        pyttsx3.speak("playing music")
        os.system("celluloid /home/growth/Documents/GITTU/Music-player/idontcare.mp3")
        func2()

    #for exit
    elif("exit" in n or "close" in n or "shut" in n or "terminate" in n):
        print("Thankyou,  Good bye ..")
        pyttsx3.speak("Thankyou,  Good bye ..")
        exit()

    else:
        print("Sorry i didn't understand, Please speak again")
        pyttsx3.speak("Sorry i didn't understand, Please speak again")
        func1()



def func2():
    print("Do you want to perform another task (yes/no)?", end="")
    pyttsx3.speak("Do you want to perform another task ?")
    k=input()
    if(k == "yes" or k == "yupz" or k == "sure"):
        print("Say what can i do for you")
        pyttsx3.speak("Say what can i do for you")
        func1()
    else:
        print("Thankyou,  Good bye ..")
        pyttsx3.speak("Thankyou,  Good bye ..")
        exit()

pyttsx3.speak("Say what can i do for you")
func1()