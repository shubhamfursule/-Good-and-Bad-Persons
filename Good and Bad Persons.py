for i in range(int(input())):
    N,K=map(int,input().split())
    a = input()
    countupp=0
    countlow=0
    
    for i in a:
        if i.isupper():
            countupp+=1
        else:
             countlow+=1
       # print("hghkk")         
    if countlow== countupp:
        if K>=countupp:
            print("both")
        elif K<countupp:
            print("none")
        
    elif countupp>countlow:
        
            
        if K>=countupp:
            print("both")
        elif K<countlow:
            print("none")
        elif countlow<=K<countupp:
            print("brother")
    elif countupp<countlow:
        
        if K>=countlow:
            print("both")
        elif K<countupp:
            print("none")       
        elif countupp<=K<countlow:
            print("chef")    
    