#Punto c)
import wfdb
import matplotlib.pyplot as plt
import numpy as np

nombrearchivo ="EDM/emg_healthy"

record = wfdb.rdrecord(nombrearchivo)
signal = record.p_signal[:,0]  
fs = record.fs  #fs = periodo (T)
numerodatos = len(signal) 
limitartiempo=int(10*fs) #muestreo

time = [i / fs for i in range(numerodatos)]  
signal = signal[:limitartiempo]
time = time[:limitartiempo]

#DIBUJAR SEÑAL
plt.figure(figsize=(12,4))
plt.plot(time, signal, color="orange")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (mv)")
plt.title("Señal Biomédica EMG bases de datos physionet")
plt.legend()
plt.grid()
plt.show()

#ESTADISTICOS A MANO
suma = 0
for i in range(len(signal)):
    suma += signal[i]
media = suma /len(signal)
print(f"la media de la señal es: {media:.3f}")

#VECTOR DE LOGITUD
vector=0
for _ in signal:
    vector += 1
print(f"la longitud del vector es: {vector}")

#DESVIACION ESTANDAR
desviacion=0
for i in range(len(signal)):
    desviacion += (signal[i] - media) ** 2
desviacion_estandar = (desviacion/len(signal))**0.5
print (f"la desviacion estandar es: {desviacion_estandar:.3f}")

#COEFICIENTE DE VARIACION
coeficiente = desviacion_estandar/media if media !=0 else float ("nan")
print (f"El coeficiente es: {coeficiente:.3f}")

#ESTADISTICOS CON FUNCIONES
media_librerias = np.mean(signal)
longitud_vector_librerias = len(signal)
desviacion_librerias = np.std(signal)
coeficiente_variacion_librerias = desviacion_librerias / media_librerias if media_librerias != 0 else np.nan

print(f"Media de la señal con librerias: {media_librerias:.4f}")
print(f"Longitud del vector con librerias: {longitud_vector_librerias}")
print(f"Desviación estándar con librerias: {desviacion_librerias:.4f}")
print(f"Coeficiente de variación con librerias: {coeficiente_variacion_librerias:.4f}")

#TRANSFORMADA DE FOURIER

t = np.linspace(0, 1, fs, endpoint=False)
N = len(t)

frecuencia = np.fft.fftfreq(N, 1/fs) #muestreo
spectrum = np.fft.fft(signal) / N
magnitud = 2 * np.abs(spectrum[:N//2]) ##cantidad de canales

plt.figure(figsize=(12,4))
plt.plot(frecuencia[:N//2], magnitud, color="red")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.title("Espectro señal normalizado")
plt.legend()
plt.grid()
plt.show()

##DENSIDAD ESPECTRAL
psd = (magnitud ** 2) / N

plt.figure(figsize=(12,4))
plt.plot(frecuencia[:N//2], psd, color="blue")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Densida Espectral")
plt.title("Espectro señal de densidad espectrall")
plt.legend()
plt.grid()
plt.show()

##FRECUENCIA MEDIA, MEDIANA

suma = 0
for i in range(len(magnitud)):
    suma += magnitud[i]
media = suma /len(magnitud)
print(f"la media de la señal es: {media:.3f}")

desviacion=0
for i in range(len(magnitud)):
    desviacion += (magnitud[i] - media) ** 2
desviacion_estandar = (desviacion/len(magnitud))**0.5
print (f"la desviacion estandar es: {desviacion_estandar:.3f}")

media_librerias = np.mean(signal)
desviacion_librerias = np.std(signal)

print(f"Media de la señal con librerias: {media_librerias:.4f}")
print(f"Desviación estándar con librerias: {desviacion_librerias:.4f}")

plt.figure(figsize=(8, 4))
plt.hist(signal, bins=50, color='violet', alpha=0.7, edgecolor='black', density=True)
plt.xlabel("Magnitud")
plt.ylabel("Frecuencia (Hz)")
plt.title("Histograma frecuencia (10s)")
plt.grid()
plt.show()


