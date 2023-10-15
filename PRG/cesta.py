graf = [[0,0,1,0,1],
        [0,0,1,1,0],
        [1,1,0,0,1],
        [0,1,0,0,1],
        [1,0,1,1,0]]



def cesta(start, finish):
    
        if graf[start][finish] != 0:
                return f"cesta v grafu z {start} do {finish} je platný"
        else:
                return f"cesta v grafu z {start} do {finish} není platný"



# cesta(start, finish) start = node, ze kterého budeme začínat (A = 0, graf[0][0]) | finish = node u kterého kontrolujeme jestli se spojen s start nodem (E = 4, graf[0][4])

lol = cesta(0, 4)
print(lol)