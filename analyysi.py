import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib
from matplotlib.widgets import Slider
matplotlib.use("TkCairo")

start = 0
stop = 10

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)


nsposition = plt.axes([0.25, 0.12, 0.65, 0.03])
nollaslider = Slider(nsposition, 'Raja-arvo (c)', start + 1, stop-1, valinit=1)

dsposition = plt.axes([0.25, 0.07, 0.65, 0.03])
deltaslider = Slider(dsposition, 'Delta', 0.01, 3, valinit=1)


def func(x):
    return x**2 + 2 * x + 1


axis = np.arange(start=0, stop=stop, step=0.1)
yaxis = func(axis)


teksti = "Epsilon delta-määritelmän mukaan\n" \
         "   funktiolla on raja-arvo pisteessä c, jos\n" \
         "   jokaista ε>0 kohtaan on olemassa δ>0,\n" \
         "   siten että |f(x)-f(c)|<ε, kun 0<|x-c|<δ\n\n" \
         "Käytännössä tämä siis tarkoittaa sitä että\n" \
         "   kun ollaan lähellä funktion raja-arvoa niin\n" \
         "   voidaa funktion kautta ns. heijastaa piste\n" \
         "   takaisin y-akselille. Jos x-akselilta\n" \
         "   heijastetut pisteet ovat lähellä toisiaan, \n" \
         "   niin sanotaan että funktiolla on raja-arvo\n\n" \
         "Vieressä olevan sovelluksen kanssa voi\n" \
         "   leikkimielisesti etsiä epsilonin (ε) likiarvoja\n" \
         "   vaihtamalla alla olevista slidereista\n" \
         "   deltan (δ) ja raja-arvon(c) paikkaa\n\n" \
         "Funktioksi on esimerkissä kuvattu\n" \
         "   x^2 + 2x +1, mutta ohjelmaan voi\n" \
         "   vaihtaa oman mielensä mukaan\n" \
         "   myös oman funktion ja tarkastelualueen"


def update(val):
    ax.clear()
    nollax = nollaslider.val
    delta = deltaslider.val
    yaxis = func(axis)
    nollay = func(nollax)
    deltaminus = func(nollax - delta)
    deltaplus = func(nollax + delta)
    epsilonplus = deltaplus - nollay
    epsilonminus = nollay - deltaminus
    #print(f"Epsilonplus: {epsilonplus}, Epsilonminus: {epsilonminus}")
    ax.plot(axis, yaxis)
    ax.plot(nollax - delta, deltaminus, marker='o', markersize=4, color="blue") #vasen delta
    ax.plot(nollax + delta, deltaplus, marker='o', markersize=4, color="blue") #oikea delta
    ax.plot(nollax, nollay + stop * 0.05, marker='o', markersize=4, color="red") # nollakohta

    ax.plot(0, deltaplus, marker='o', markersize=4, color="purple") # epsilon plus piste
    ax.plot(0, deltaminus, marker='o', markersize=4, color="purple") # epsilon minus piste

    ax.plot([0, nollax + delta], [deltaplus, deltaplus], 'k--')  #epsilon to deltaplus
    ax.plot([0, nollax - delta], [deltaminus, deltaminus], 'k--')  #epsilon to deltaminus
    ax.plot([0, nollax], [nollay, nollay], 'k--')  #epsilon to deltaminus
    ax.plot(0, nollay, marker='o', markersize=4, color="blue")

    ax.plot([nollax-delta, nollax-delta], [0, deltaminus], 'k--')
    ax.plot([nollax+delta, nollax+delta], [0, deltaplus], 'k--')
    ax.plot([nollax, nollax], [0, nollay], 'k--')
    ax.text(nollax - delta, nollax-delta - 20, "δ -")
    ax.text(nollax + delta, nollax + delta - 20, "δ +")
    ax.text(nollax, nollax - 20, "C")
    ##akselit
    ax.plot([0, 0], [0, np.max(yaxis)], 'k-')
    ax.plot([0, np.max(axis)], [0, 0], 'k-')
    ax.text(1, np.max(yaxis)*0.9 , f"Epsilon ε: \n{round(min(epsilonminus, epsilonplus), 3)}", fontsize=18)
    ax.text(-0.4, deltaplus, "m+ε", fontsize=10)
    ax.text(-0.4, deltaminus, "m-ε", fontsize=10)


fig.text(0.47, 0.92, "Funktion raja-arvo", fontsize= 20)
fig.text(0.01, 0.4, s=teksti, fontsize=14) #opetusteksti

nollaslider.on_changed(update)
deltaslider.on_changed(update)
plt.show()
