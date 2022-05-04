from tkinter import *
class Ventana:
    __titulo=str
    __xiz=0
    __yiz=0
    __xder=500
    __yder=500
    def __init__(self,ti,xi=0,yi=0,xd=500,yd=500):
        self.__titulo=ti
        self.__xiz=xi
        self.__yiz=yi
        self.__xder=xd
        self.__yder=yd
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return (self.__yder-self.__yiz)
    def ancho(self):
        return (self.__xder-self.__xiz)

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
        ven=Tk()
        ven.title(self.__titulo)
        y=self.__yder-self.__yiz
        x=self.__xder-self.__xiz
        ven.geometry("{}x{}".format(x,y))
        mainloop()

    def bajar (self,b=0):
        for d in range (b):
            self.__yder=self.__yder-d
            if self.__yiz !=0:
                self.__yiz=self.__yiz-d
    def subir (self,s=0):
        for l in range (s):
            self.__yiz=self.__yiz+l
            if (self.__yder<500):
                self.__yder=self.__yder+l

