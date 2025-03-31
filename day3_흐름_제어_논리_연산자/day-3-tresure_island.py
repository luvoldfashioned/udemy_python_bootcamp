

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_question = input("left or right?")
first_question_lowercase = first_question.lower()
if first_question_lowercase == "left":
    second_question = input("swim or wait?")
    second_question_lowercase = second_question.lower()
    if second_question_lowercase == "wait":
        third_question = input("which door? red, blue, green")
        third_question_lowercase = third_question.lower()
        if third_question == "red":
            print('''
                            (  .      )
                    )           (              )
                            .  '   .   '  .  '  .
                    (    , )       (.   )  (   ',    )
                    .' ) ( . )    ,  ( ,     )   ( .
                ). , ( .   (  ) ( , ')  .' (  ,    )
                (_,) . ), ) _) _,')  (, ) '. )  ,. (' )  
                ''')
            print("burned by fire, GAME OVER")
        elif third_question == "blue":
            print('''
                    /^\      /^\
                    |  \    /  |
                    ||\ \../ /||
                    )'        `(
                    ,;`w,    ,w';,
                    ;,  ) __ (  ,;
                    ;  \(\/)/  ;;
                    ;|  |vwwv|    ``-...
                    ;  `lwwl'   ;      ```''-.
                    ;| ; `""' ; ;              `.
                    ;         ,   ,          , |
                    '  ;      ;   l    .     | |
                    ;    ,  ,    |,-,._|      \;
                    ;  ; `' ;   '    \ `\     \;
                    |  |    |  |     |   |    |;
                    |  ;    ;  |      \   \   (;
                    | |      | l       | | \  |
                    | |      | |  pb   | |  ) |
                    | |      | ;       | |  | |
                    ; ,      : ,      ,_.'  | |
                    :__'      | |           ,_.'
                    ''')    
            print("Eaten by beasts, GAME OVER")
        elif third_question == "green":
            print('''
                  888                                              
                888                                              
                888                                              
                88888b.  .d88b.  8888b. 888  888 .d88b. 88888b.  
                888 "88bd8P  Y8b    "88b888  888d8P  Y8b888 "88b 
                888  88888888888.d888888Y88  88P88888888888  888 
                888  888Y8b.    888  888 Y8bd8P Y8b.    888  888 
                888  888 "Y8888 "Y888888  Y88P   "Y8888 888  888 


                    ''')
            print("You WIN!")
    else:
        print('''
         
                    .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
                                       (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'     
        ''')
        print("Attacked by crocodile. GAME OVER")

else:
    print('''
        888             888         
        888             888         
        888             888         
        88888b.  .d88b. 888 .d88b.  
        888 "88bd88""88b888d8P  Y8b 
        888  888888  88888888888888 
        888  888Y88..88P888Y8b.     
        888  888 "Y88P" 888 "Y8888  
                              ''')
    print("Fall into a hole. GAME OVER")