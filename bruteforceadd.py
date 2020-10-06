for x in range(50):
    for y in range(50):
        a=[123*x,-123*x]
        b=[179*y,-179*y]
        for p in a:
            for q in b:
                if p+q == 1:
                    print(x,y,p,q)
                    
