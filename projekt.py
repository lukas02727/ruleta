import random as r
money = int(input("Zadej počet peněz k vsázení: "))

while True:
    
    play = input("Chceš pokračovat ve hře? ")
    if play == "ne":
        print("Ukončil jsi hru")
        break
    while True: 
        c = money
        
        bet = int(input("Kolik chceš vsadit peněz: "))
       
            
        color = input("Zadej barvu na kterou si chceš vsadit: ")
        if color == "černá" or color == "červená":
            break
        else:
            print("Zadal jsi špatnou barvu")
           


    number = r.randint(0, 37)
    if number <= 17:
        result = "černá"
    elif number <=36:
        result = "červená"
    else:
        result = "zelená"
        
    
        
    if color == result:
        c=money+bet
        print(c)
        print("Vyhrál jsi")
       
        
    else:
       c=money-bet 
       print(c)
       print("Prohrál jsi, protože padla ", result)
       
      
    
    





