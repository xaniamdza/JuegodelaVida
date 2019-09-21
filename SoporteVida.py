"""
El juego de la vida
- Del tipo zero-player
- Creado por John H. Conway(1970)
- Ejemplifica, el ascenso, caida y alternancia de seres vivos

Reglas:
    
1.- Si una célula está viva y tiene 2 o 3 vecinos vivos, la célula sobrevive a
la siguiente generación. Los vecinos son las 8 células que la rodean
inmediatamente tanto en vertical, horizontal y diagonal.

2.- Una célula viva que no tiene vecinos vivos o que tiene un solo vecino vivo muere
por soledad para la siguiente generación.

3.- Una célula viva que tiene 4 o más vecinos muere por sobrepoblación para 
la siguiente generación.

4.- Una célula muerta con exactamente 3 vecinos vivos resulta en un nacimiento
cuya vida empezará la siguiente generación. Todas las células muertas 
restantes se mantienen muertas la siguiente generación.

"""

"""
SoporteVida

SoporteVida(rows,cols)
get_num_rows()
get_num_cols()
configure(lista,generaciones)
clear_cell(row,col) ----> matar
set_cell(row,col) ----> revivir,nacimiento
is_alive_cell(row,col) ----> esta vivo? true o false
get_alive_neighbors(row,col) ----> 

"""
from Array2D import Array2D

"""
0 -> celula muerta
1 -> celula viva

"""

class SoporteVida:
    def __init__(self,rows,cols):
        self.__rows = rows
        self.__cols = cols
        self.__gens = 0
        self.__grid = Array2D(rows,cols)
        self.__grid.clearing(0)
        
    def get_num_rows(self):
        return self.__rows
    
    def get_num_cols(self):
        return self.__cols
    
    def configure(self,inicial,generaciones):
        """inicial es una lista de la forma:
           inicial = [[1,2],[2,2],[2,3],[3,1]] 
        """
        self.__gens = generaciones
        for cell in inicial:
            self.__grid.set_item(cell[0],cell[1],1)
            
    def clear_cell(self,row,col):
        self.__grid.set_item(row,col,0)
        
    def set_cell(self,row,col):
        self.__grid.set_item(row,col,1)
        
    def is_alive_cell(self,row,col):
        if self.__grid.get_item(row,col)==1: 
            return True
        else:
            return False
    
    def get_alive_neighbors(self,row,col):
        limites=self.__calcula_vecinos(row,col)
        vivos=0
        for r in range(limites[2],limites[3]+1,1):
            for c in range(limites[0],limites[1]+1,1):
                if self.__grid.get_item(r,c)==1:
                    vivos+=1
        if self.__grid.get_item(row,col) == 1:
            vivos-=1
        return vivos
           
    def __calcula_vecinos(self,ren,col):
        x_ini=col-1
        x_fin=col+1
        y_ini=ren-1
        y_fin=ren+1
        if col == 0:
            x_ini = 0
        if col == self.__cols-1:
            x_fin = self.__cols-1
        if ren == 0:
            y_ini = 0
        if ren == self.__rows-1:
            y_fin = self.__rows-1
       
        return [x_ini,x_fin,y_ini,y_fin]

    def to_string(self):
        for x in (self.__rows):
            self.__grid[x].to_string()

    def reglas(self):
        self.__nuevo = Array2D(self.__rows,self.__cols)
        self.__nuevo.clearing(0)
        for r in range(self.__rows):
            for c in range(self.__cols):
                vivo = self.is_alive_cell(r,c)
                vecino = self.get_alive_neighbors(r,c)
                if vivo == True:
                    if vecino == 2 or vecino == 3:      
                        self.__nuevo.set_item(r,c,1)
                    if vecino < 2:                      
                        self.__nuevo.set_item(r,c,0)
                    if vecino >= 4:                     
                        self.__nuevo.set_item(r,c,0)
                else:
                    if vecino == 3:                     
                        self.__nuevo.set_item(r,c,1)
        self.__grid = self.__nuevo 
        return self.__grid   

    def inicio_juego(self):
        print("Generación inicial:")
        self.__grid.to_string()
        for x in range(1,self.__gens):
            inicio = self.reglas()
            print(f"Generación {x}:")
            inicio.to_string()        
        
def main():
    juego = SoporteVida(5,5) 
    juego.configure([[1,2],[2,1],[2,2],[2,3]],10) 
    juego.inicio_juego() 
   
main()
























