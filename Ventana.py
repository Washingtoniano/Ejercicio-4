class Ventana():
    __titulo:str
    __xiz=0
    __yiz=0
    __xder=500
    __yder=500
    def __int__(self,titulo):
        self.__titulo=titulo
        self.__xiz=0
        self.__yiz=0
        self.__xder=500
        self.__yder= 500
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return (self.__yder-self.__yiz)
    def ancho(self):
        return (self.__xder-self.__xiz)
    def Cargar(self,x,y):
        self.__xiz=x
        self.__xder=x
        self.__yder=y
        self.__yiz=y
    def mostrar (self):
        print ()
    def moverDerecha(self,d):
        for i in range (d):
            self.__xiz=self.__xiz+i
            self.__xder=self.__xder+i
    def moverIzquierda(self,i):
        for j in range(i):
            if (self.__xiz!=0):
                self.__xiz=self.__xiz-i
            self.__xder=self.__xder-i
    def mostrar(self):
        print (self.__titulo,self.__xiz,self.__xder,self.__yiz,self.__yder)
    def bajar (self,b):
        for d in range (b):
            self.__yder=self.__yder-d
            if self.__yiz !=0:
                self.__yiz=self.__yiz-d
    def subir (self,s):
        for l in range (s):
            self.__yiz=self.__yiz+l
            if (self.__yder<500):
                self.__yder=self.__yder+l

