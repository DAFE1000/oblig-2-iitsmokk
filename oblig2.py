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


plt.plot(x1, f(x1), label="f(x)", color="green")
plt.plot(x1, df(x1), label="f´(x)", color="red")
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
    y = x - (f(x)/df(x))
    return y

#xn+1
xn = 0

"""
siden jeg skal finne punktet med 4 desimalers tilnærming så stopper jeg
funksjonen når forskjellen mellom xn+1 - xn er mindre enn 4 desimalers tilnærming

(xn+1-xn)<10^-4

siden jeg velger å gjøre det slik så må jeg finne lengden av forskjellen
mellom xn+1 og xn slik at programmet ikke stopper med en gang
"""
def lengde(x, y)
    lengde = np.sqrt(x**2+y**2)
    return lengde
#finner nullpunktet, oppdaterer x0 til xn

while ((xn-x0) < 10**-4):
    xn = newton_metode(x0)
    x0 = xn
    print(f"nullpunktet er nå tilnærmet{xn}")

print(f"f'(x)=0, når x = {xn}")