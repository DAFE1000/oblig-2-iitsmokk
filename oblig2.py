import matplotlib.pyplot as plt
import numpy as np

#PSEUDO 1
"""
def f(x):
    y = funksjon
    return y

def df(x):
    y = funksjon
    return y


plotter funksjonen for å se ca hvor jeg kan begynne
med newtons metode.

Newtons metode
def newton_metode(x):
    y = x - (f(x)/df(x))
    return y

    
x0 = vurderes utifra plott

y = 0

for i in range (n):
    y = newton_metode(x0)
    x0 = y

print("0 punktet til funksjonen ligger på:", y)
"""
#start mengde for funksjonene, justerer denne helt til jeg får ett tydelig toppunkt
x1 = np.linspace(-1, 2.5, 201)

def f(x):
    y = np.exp(-x/4)*np.arctan(x)
    return y

def df(x):
    y = np.exp(-x/4) * (1/(1 + x**2) - (1/4) * np.arctan(x))
    return y

#legger inn den andrederiverte som g(x) siden jeg deriverte uten e
def g(x):
    y = (1/(1+x**2))+(8*x/((1+x**2)**2))
    return y


plt.plot(x1, f(x1), label="f(x)", color="green")
plt.plot(x1, df(x1), label="f´(x)", color="red")
plt.plot(x1, g(x1), label="g(x)", color="blue")
#plotter i ett mer tydelig koordinatsystem
plt.axhline(0)   # x-aksen
plt.axvline(0)   # y-aksen
plt.grid()       # rutenett

plt.legend()
plt.show()

#ser at nullpunktet ligger i ca x0 = 1.6 og bruker dette som startverdi
x0 = 1.6

#Newtons metode
def newton_metode(x):
    y = x - (df(x)/g(x))
    return y

#xn
xn = x0


#xn + 1
xn1 = newton_metode(xn)

#finner nullpunktet
for i in range (5):
    xn = xn1
    xn1 = newton_metode(xn)
    print(f"nullpunktet er nå tilnærmet{xn1}")

print(f"f'(x)=0, når x = {round(xn1, 4)}")

#lager en ny x-verdi med større domene
x2 = np.linspace(-10, 10, 201)

#plotter alt på ny, men med den nye x verdien for å sjekke om jeg har fått riktig toppunkt
plt.plot(x2, f(x2), label="f(x)", color="green")
plt.plot(x2, df(x2), label="f´(x)", color="red")
plt.plot(x2, g(x2), label="g(x)", color="blue")
plt.scatter(xn1, f(xn1), label="toppunkt")
#plotter i ett mer tydelig koordinatsystem
plt.axhline(0)   # x-aksen
plt.axvline(0)   # y-aksen
plt.grid()       # rutenett

plt.legend()
plt.show()