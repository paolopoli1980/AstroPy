import math
import matplotlib.pyplot as plt

# Costanti

g=9.8
R=6.4e6


# Masse degli elementi del razzo
SpaceShipMass=1e3
RocketMass=3e3
FuelMass=2800e3
Mrate=13212
Mtot=SpaceShipMass+RocketMass+FuelMass

# Caratteristiche di propulsione
vesp=2400
tstop=210.5
#Passo temporale
dt=0.01  # secondi

#limit e condizioni iniziali della simulazione
vmax=11e6   # m/s
tmax=1000*24
v=0
h=0
vx0=0
vz0=0
t=vt0=vn0=xt0=xn0=x=z=0
vgraph=[]
tgraph=[]
vagraph=[]
zgraph=[]
mgraph=[]
M=0
while vt0<vmax and t<tmax and z>=0:
    t+=dt
    # Condizione sul consumo del carburante
    
    if (t<tstop)  and (M<FuelMass):
        M=Mrate*t
    else:
        vesp=0
    if M>=FuelMass:
        Mrate=0
        M=FuelMass
        vesp=0

    #Calcolo della accelerazione
    at=Mrate/(Mtot-M)*vesp-g*(R/(R+z))**2

    #Eulero eplicito
    vt0+=at*dt
    xt0+=vt0*dt

    z=xt0
    # Fino a quando non si solleva, il razzo è fermo (Reazione vincolare terreno)
    if z<=0:
        at=0
        z=0
        xt0=0
        vt0=0
        
    #Parametri memorizzati per il grafico
    vgraph.append(vt0)
    tgraph.append(t)
    zgraph.append(xt0)
    mgraph.append(Mtot-M)
    

plt.figure(figsize=(12, 6))


plt.subplot(1, 3, 1)
plt.plot(tgraph, vgraph)
plt.title("Velocità")
plt.xlabel("Tempo (s)")
plt.ylabel("m/s")

plt.subplot(1, 3, 2)
plt.plot(tgraph, zgraph)
plt.title("Z")
plt.xlabel("Tempo (s)")
plt.ylabel("m")

plt.subplot(1, 3, 3)
plt.plot(tgraph, mgraph)
plt.title("Mtot")
plt.xlabel("Tempo (s)")
plt.ylabel("Kg")

plt.tight_layout()
plt.show()    
    
    
    
    


