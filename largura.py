import time

labi_0 = [[2,1,0,0,1,0,0,0,1,3],
               [0,1,0,1,1,0,1,0,1,0],
               [0,1,0,1,1,0,1,0,1,0],
               [0,1,0,1,1,0,1,1,1,0],
               [0,1,0,1,1,0,1,1,1,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,1,1,0,1,1,1,0,1,0],
               [0,1,1,0,1,1,1,0,1,0],
               [0,0,0,0,1,1,1,0,1,1],
               [0,1,1,1,1,1,1,0,0,0]]

labi_1 = [[0,0,2,0,0,0,0,0,0,1],
               [0,0,1,0,1,0,0,1,1,3],
               [0,0,1,0,1,0,0,1,1,0],
               [0,0,1,0,1,0,0,0,1,0],
               [0,0,1,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,1,0,1,1],
               [0,0,0,1,1,1,0,1,1,1],
               [1,0,0,0,1,1,0,0,0,0],
               [1,1,0,0,0,0,0,1,1,0],
               [0,0,0,0,1,0,0,1,0,0]]

labi_2 = [[3,1,1,1,1,1,1,1,1,1],
               [0,1,1,1,1,1,1,1,1,1],
               [0,1,1,1,1,1,1,1,1,1],
               [0,0,0,0,0,0,0,0,1,1],
               [1,1,1,0,1,0,1,0,1,1],
               [1,1,1,0,1,0,1,0,1,1],
               [1,1,0,0,0,0,1,0,1,1],
               [1,1,0,1,1,1,1,0,0,0],
               [1,1,0,1,1,1,1,0,1,0],
               [1,1,0,0,0,0,0,0,2,0]]

labi_3 = [[2,1,1,1,1,1,1,1,1,1],
               [0,0,0,0,1,1,1,1,3,0],
               [0,1,1,0,0,0,0,1,1,0],
               [0,0,0,0,1,1,0,0,1,0],
               [1,1,1,1,0,1,1,0,1,0],
               [1,1,1,1,0,0,0,0,0,0],
               [1,1,1,1,0,1,1,1,0,1],
               [1,1,1,1,1,1,1,1,0,1],
               [1,1,1,1,1,0,0,0,0,1],
               [1,1,1,1,1,1,1,1,1,1]]

labi_4 = [[0,0,0,0,0,0,0,0,0,2],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,1,0,0,0,0],
               [0,0,0,0,0,1,0,0,0,0],
               [1,0,0,0,0,1,0,0,0,0],
               [1,0,0,0,0,1,3,0,0,0],
               [1,0,1,0,0,0,0,0,0,0],
               [1,0,1,0,0,0,0,0,0,0],
               [1,1,1,1,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0]]

class Node:
    def __init__(Node, e=None, d=None, c=None, b=None, cam_certo = None, seguinte = None, caminho = False):
        Node.e = e
        Node.d = d
        Node.c = c
        Node.b = b
        
        Node.caminho = caminho
        Node.cam_certo = cam_certo
        Node.seguinte = seguinte 
    def __repr__(self):
        return '      %s \n %s <- %s -> %s \n       %s' % (self.c and self.c.seguinte, self.e and self.e.seguinte,self.seguinte,self.d and self.d.seguinte, self.b and self.b.seguinte)

def find_start(labi):
   for i in range(len(labi)):
       for j in range(len(labi[i])):
           if(labi[i][j] == 2):
               return(i,j)
   return -1

def livre(p,labi,no):
    if(no.seguinte[1] > 0):
        if(p == 'e') and (labi[no.seguinte[0]][no.seguinte[1]-1] != 1) and (labi[no.seguinte[0]][no.seguinte[1]-1] != 4):
            return 1
    if(no.seguinte[1] < 9):
        if(p == 'd') and (labi[no.seguinte[0]][no.seguinte[1]+1] != 1) and (labi[no.seguinte[0]][no.seguinte[1]+1] != 4):
            return 1
    if(no.seguinte[0] < 9):
        if(p == 'b') and (labi[no.seguinte[0]+1][no.seguinte[1]] != 1) and (labi[no.seguinte[0]+1][no.seguinte[1]] != 4):
            return 1
    if(no.seguinte[0] > 0):
        if(p == 'c') and (labi[no.seguinte[0]-1][no.seguinte[1]] != 1) and (labi[no.seguinte[0]-1][no.seguinte[1]] != 4):
            return 1
    return 0

def fora(no,labi):
    if(labi[no.seguinte[0]][no.seguinte[1]] == 3):
        return 1
    return 0

def visto(no,labi):
    labi[no.seguinte[0]][no.seguinte[1]] = 4
    no.caminho = True

def foi_visto(no,labi):
    if(labi[no.seguinte[0]][no.seguinte[1]] == 4):
        return 1
    return 0

def procura_BFS(fila,raiz,labi,i = 0):  
    if(foi_visto(fila[0], labi)):
        fila.pop(0)
        procura_BFS(fila,raiz,labi)
    
    else:
        if(fila[0].caminho == False):  
            if(not fila[0].cam_certo):
                time.sleep(0.1)
                print("labi: (percurso em largura!)")
                print("Visitando: ",fila[0].seguinte)
                print_labi(labi)
                print("\n\n")
                if(fora(fila[0],labi) == 1):
                    fila[0].cam_certo = 3 
                    if(marca_caminho_ate_fora(fila[0], raiz) == 1):
                        raiz.cam_certo = 1
                        return fila
                else:
                    if(livre('e',labi,fila[0])):
                        fila[0].e = Node()
                        fila[0].e.seguinte = fila[0].seguinte
                        fila[0].e.seguinte = [int(i) for i in fila[0].e.seguinte]
                        fila[0].e.seguinte[1] -= 1
                        fila.append(fila[0].e)
                    if(livre('b',labi,fila[0])):
                        fila[0].b = Node()
                        fila[0].b.seguinte = fila[0].seguinte
                        fila[0].b.seguinte = [int(i) for i in fila[0].b.seguinte]
                        fila[0].b.seguinte[0] += 1
                        fila.append(fila[0].b)
                    if(livre('d',labi,fila[0])):
                        fila[0].d = Node()
                        fila[0].d.seguinte = fila[0].seguinte
                        fila[0].d.seguinte = [int(i) for i in fila[0].d.seguinte]
                        fila[0].d.seguinte[1] += 1
                        fila.append(fila[0].d)
                    if(livre('c',labi,fila[0])):
                        fila[0].c = Node()
                        fila[0].c.seguinte = fila[0].seguinte
                        fila[0].c.seguinte = [int(i) for i in fila[0].c.seguinte]
                        fila[0].c.seguinte[0] -= 1
                        fila.append(fila[0].c)                
                    visto(fila[0],labi)           
                    fila.pop(0)           
                    procura_BFS(fila,raiz,labi)          
    return fila

def marca_caminho_ate_fora(no,raiz,i = 0):   
    if(raiz.e != None):
       if(raiz.e == no):
            return 1
       else:
            if (marca_caminho_ate_fora(no,raiz.e,i+1) == 1):
                raiz.e.cam_certo = 1
                return 1

    if(raiz.d != None):

       if(raiz.d == no):
            return 1
       else:
            if (marca_caminho_ate_fora(no,raiz.d,i+1) == 1):
                raiz.d.cam_certo = 1
                return 1
  
    if(raiz.c != None):
      
       if(raiz.c == no):
            return 1
       else:
            if (marca_caminho_ate_fora(no,raiz.c,i+1) == 1):
                raiz.c.cam_certo = 1
                return 1 
    if(raiz.b != None):
    
       if(raiz.b == no):
            return 1
       else:
            if (marca_caminho_ate_fora(no,raiz.b,i+1) == 1):
                raiz.b.cam_certo = 1
                return 1       
    return 0

def listar_caminho(raiz):
    if(raiz != None):
        raiz.seguinte = [int(i) for i in raiz.seguinte]
        if(raiz.cam_certo == 1):
            print("{}".format(raiz.seguinte))
        elif(raiz.cam_certo == 3):
            print("{}".format(raiz.seguinte))
            return(raiz.seguinte)
        if(raiz.e):
            if(raiz.e.cam_certo):
                return listar_caminho(raiz.e)
        if(raiz.b):
            if(raiz.b.cam_certo):
                return listar_caminho(raiz.b)
        if(raiz.d):
            if(raiz.d.cam_certo):
                return listar_caminho(raiz.d)
        if(raiz.c):
            if(raiz.c.cam_certo):
                return listar_caminho(raiz.c)


def custo_caminho_recursiva(raiz,i=0):
    if(raiz != None):
        raiz.seguinte = [int(i) for i in raiz.seguinte]
     
        i+= custo_caminho(raiz.e,i+1) + custo_caminho(raiz.b,i+1) +  custo_caminho(raiz.d,i+1) +   custo_caminho(raiz.c,i+1)
        if(raiz.cam_certo == 3):
            print("Custo caminho: {} passos ".format(i))
        return 1
    return 0

def custo_caminho(labi):
    r = 0
    for i in range(len(labi)):
        for j in range(len(labi[0])):
            if labi[i][j] == 4:
                r+=1
    print("Total de casas visitadas: {} ".format(r))
    return r

def print_labi(lab):
    
    for linha in lab:
        for e in linha:
            switch = {
                0: ' ',
                1: '#', #Parede
                3: 'E', #Final
                4: '+', #Caminho
                5: '$', #Acabou
            }
            print(switch.get(e), end=' ')
        print('')

raiz = Node()


def menu(raiz):
    labi = labi_0
    print("Insira o mapa desefoido: \n") 
    print("0 - Mapa 0")
    print("1 - Mapa 1")
    print("2 - Mapa 2")
    print("3 - Mapa 3")
    print("4 - Mapa 4")
    i = int(input(""))
    if i == 0:
        labi = labi_0
    elif i == 1:
        labi = labi_1
    elif i == 2:
        labi = labi_2
    elif i == 3:
        labi = labi_3
    elif i == 4:
        labi = labi_4

    raiz.seguinte = find_start(labi)
    assert raiz.seguinte != -1, "Inicio desse labirinto nao foi informada!"       
    fila = [raiz]    
    fila = procura_BFS(fila,raiz,labi)
    print("\nSolução BFS: ")
    p = listar_caminho(raiz)
    print("\nInicio: ", raiz.seguinte)
    print("Final:", p)
    custo_caminho(labi)

menu(raiz)