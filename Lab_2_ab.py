import numpy as np
import matplotlib.pyplot as plt

#Punto a)
#Datos david
#define h y x
x =np.array ([1,0,7,0,5,9,0,1,0,1])
h =np.array ([5,6,0,0,7,7,6])

#GRAFICA h[n] David
t = np.arange(len(h))
plt.figure(figsize=(8, 4))
plt.stem(t, h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('h[n] David')
plt.grid()
plt.show

#GRAFICA x[n] David
t = np.arange(len(x))
plt.figure(figsize=(8, 4))
plt.stem(t, x)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x[n] David')
plt.grid()
plt.show

y = np.convolve(x, h, mode='full')#se calcula la convolucion
print("Señal convolucion entre h[n] y x[n], David")

#graficacion convolucion o y[n] David
t = np.arange(len(y))
plt.figure(figsize=(8, 4))
plt.stem(t, y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Concolucion de h[n] y x[n] de David')
plt.grid()
plt.show


#Datos Sofia

x =np.array ([1,0,0,0,5,1,9,3,6,3])
h =np.array ([5,6,0,0,7,7,0])

#GRAFICA h[n] Sofia
t = np.arange(len(h))
plt.figure(figsize=(8, 4))
plt.stem(t, h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('h[n] Sofia')
plt.grid()
plt.show

#GRAFICA x[n] Sofia
t = np.arange(len(x))
plt.figure(figsize=(8, 4))
plt.stem(t, x)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x[n] Sofia')
plt.grid()
plt.show

y = np.convolve(x, h, mode='full')#se calcula la convolucion
print("Señal convolucion entre h[n] y x[n], Sofia")

#graficacion convolucion o y[n] sofia
t = np.arange(len(y))
plt.figure(figsize=(8, 4))
plt.stem(t, y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Concolucion de h[n] y x[n] de Sofia')
plt.grid()
plt.show


#Datos Dayana

x =np.array ([1,0,0,7,4,9,8,4,0,5])
h =np.array ([5,6,0,0,8,1,3])

#GRAFICA h[n] Dayana
t = np.arange(len(h))
plt.figure(figsize=(8, 4))
plt.stem(t, h)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('h[n] Dayana')
plt.grid()
plt.show

#GRAFICA x[n] Dayana
t = np.arange(len(x))
plt.figure(figsize=(8, 4))
plt.stem(t, x)
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x[n] Dayana')
plt.grid()
plt.show

y = np.convolve(x, h, mode='full')#se calcula la convolucion
print("Señal convolucion entre h[n] y x[n], Dayana")

#graficacion convolucion o y[n] dayana
t = np.arange(len(y))
plt.figure(figsize=(8, 4))
plt.stem(t, y)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Concolucion de h[n] y x[n] de Dayana')
plt.grid()
plt.show


#Punto b)
Ts = 1.25e-3 #Ts dado por la guía
n = np.arange(9) #para 0<=n<=9
f = 100 #100 nts
x1 = np.cos(2 * np.pi * f * n * Ts) #x1(nTs) = cos(2pi100nts)
x2 = np.sin(2 * np.pi * f * n * Ts) #x2(nTs) = sen(2pi100nts)
correlacion = np.correlate(x1, x2, mode='full')
print ("orrelación cruzado (vector o resultado", correlacion)

#Grafica de correlacion
t_corr = np.arange(-len(n) + 1, len(n))
plt.figure(figsize=(8, 4))
plt.stem(t_corr,correlacion)
plt.xlabel("Desplazamiento")
plt.ylabel("Correlacion")
plt.title("Correlacion cruzada entre x1[n] y x2[n]")
plt.grid()
plt.show()
