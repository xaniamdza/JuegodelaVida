class Array2D:
    
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__data = []
        for r in range (self.__rows):
            tmp=[]
            for c in range(self.__cols):
                tmp.append(None)
            self.__data.append(tmp)
                
    def to_string(self):
        print(self.__data)   

    def get_num_rows():
        return self.__rows

    def get_num_cols():
        return self.__cols
    
    def clearing(self, value):
        for r in range(self.__rows):
            for c in range(self.__cols):
                self.__data[r][c] = value
                
    def set_item(self, r, c, value):
        self.__data[r][c] = value

    def get_item(self, r, c):
        return self.__data[r][c]                
         