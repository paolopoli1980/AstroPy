import numpy as np
import matplotlib.pyplot as plt
import math
def calculation(ts,tp,e,tilting,a,rp,dp,albedo):

    def solve_kepler(M, e, tol=1e-10):
        E = M
        for _ in range(100):
            E_new = E + (M - (E - e*np.sin(E))) / (1 - e*np.cos(E))
            if np.max(np.abs(E_new - E)) < tol:
                break
            E = E_new
        return E

    for timetot in range(2):
        latitudinecity = {
          "North Pole":89.9,
          "Longyearbyen":78.22,
          "Helsinki":60.16749,
          "Rome": 41.8933203,
          "Cairo":31.2357257,
          "Kinshasa":-4.3217055,
          "Sydney":-33.52,
          "Ushuaia":-55,
          "South Pole":-89.9  
        }

        namecity=["North Pole","Longyearbyen","Helsinki","Rome","Cairo","Kinshasa","Sydney","Ushuaia","South Pole"]
        fig, (ax1, ax2, ax3,ax4,ax5,ax6,ax7,ax8,ax9) = plt.subplots(9)
        ax1.set_title(namecity[0])
        ax2.set_title(namecity[1])
        ax3.set_title(namecity[2])
        ax4.set_title(namecity[3])
        ax5.set_title(namecity[4])
        ax6.set_title(namecity[5])
        ax7.set_title(namecity[6])
        ax8.set_title(namecity[7])
        ax9.set_title(namecity[8])

        ax9.set_ylabel('Flux')
        ax9.set_xlabel('Hours')

        Au=149597870.7*10**3
        g=6.67*10**(-11)
        k=1.3806504*10**(-23)

    #    ts=365  # periodo intorno alla stella in giorni
    #    tp=24 #periodo intorno a se stesso in ore
        ws=2*math.pi/(ts*24)
        wt=2*math.pi/(tp)
        #tilting=50.0
    #    a=1.0 # asse maggiore a=1 corrisponde a 1 Au 
    #    e=0.0167
        b=math.sqrt(1-e**2)*a
        xf=math.sqrt(a**2-b**2)
    #    rp=6370*10**3
    #    dp=5510
        mp=(4*math.pi*rp**3*dp/3)
        mearth=5.972*10**(24)
        grav=g*mp/rp**2
        ls=3.83*10**26
        ms=1.989*10**30
    #    albedo=0.3
        staresp=3.5
        qstar=0
        mstar=4*math.pi**2*(a*Au)**3/((ts*3600*24)**2*g)
        xf=math.sqrt(a**2-b**2)
        lstar=ls*(mstar/(ms*10**(qstar)))**staresp
        tf=ts*24*10**timetot
        inct=tp/100
        boltzstef=5.67*10**(-8) 
        dstar=1.41*10**3
        rstar=math.cbrt((mstar*3/(4*math.pi*dstar)))
        tstar=math.sqrt(math.sqrt((lstar/(4*math.pi*rstar**2*boltzstef))))

        mN=2.3258671*10**(-26)
        mNmol=2*mN
        mOmol=2*2.6566962*10**(-26)
        mCO2mol=7.3065427*10**(-26)
        mH2Omol=2.9915311*10**(-26)

        for i in range(len(namecity)):
           # ws=7.164*10**(-4)
           # wt=0.2616666
        #    print(ws,wt,xf)

            #xf=0
            t=0
            latitudine=latitudinecity[namecity[i]]
            alfa=-math.pi*(latitudine-90)/180
            omega=tilting*math.pi/180*1
            betazero=0
            teta=0
            philist=[]
            tlist=[]
            phimax=1
            philistnew=[]
            dmin=a
            dmax=0
            
            while t<tf:
                t+=inct
                
                beta=wt*t+betazero
                #d=math.sqrt((-a*math.cos(ws*t+teta)+xf)**2+b**2*math.sin(ws*t+teta)**2)
                M = 2*np.pi * t / (ts*24)   # anomalia media
                E = solve_kepler(M, e)      # anomalia eccentrica
                d = a * (1 - e*np.cos(E))   # distanza fisica

                if d<dmin:
                    #print(d)
                    dmin=d
                if d>dmax:
                    dmax=d
            #print(dmin)

            if i==0 and timetot==0:
                
                tmax=tstar*math.sqrt(math.sqrt(1-albedo))*math.sqrt(rstar/(2*(dmin*Au)))
                tmin=tstar*math.sqrt(math.sqrt(1-albedo))*math.sqrt(rstar/(2*(dmax*Au)))
                tempNmol=(1/54)*g*mNmol*mp/(k*rp)
                tempN=(1/54)*g*mN*mp/(k*rp)
                tempOmol=(1/54)*g*mOmol*mp/(k*rp)
                tempCO2=(1/54)*g*mCO2mol*mp/(k*rp)
                tempH2O=(1/54)*g*mH2Omol*mp/(k*rp)
                print('------------ Rapporti tra parametri stelle e sole (Star Sun ratio) -------------------------------')
                print("Massa della stella = "+str(mstar/ms))
                print("Luminosità della stella = "+str(lstar/ls))
                print('---------------------------------------------------------------------------------')
                      
                print('------ Rapporti tra parametri pianeta e quelli terrestri ( Planets earth ratio parameters)------------------')
                print("Massa della stella (Star mass ratio) = "+str(mstar/ms))
                print("Massa del pianeta (Planet mass ratio) = " + str(mp/mearth))
                print("Gravità del pianeta (Gravity planet ratio) = " + str(grav/9.81))
                print('------------------- Temperature in gradi Kelvin (Temperatures) ---------------------------')
                print("Temperaruta blackbody massima (Blackbody Temp Max) = "+str(tmax))
                print("Temperatura blackbody minima (Blackbody Temp Min) = "+str(tmin))
                print('---------------------------------------------------------------------------')

                print('----Temperature di fuga delle possibili molecole più note in atmosfera (Escape temperatures of molecules)-----')
                print("Temperatura di fuga N2  = "+str(tempNmol))
                print("Temperatura di fuga N = "+str(tempN))
                print("Temperatura di fuga O2 ="+str(tempOmol))
                print("Temperaturea di fuga CO2 ="+str(tempCO2))
                print("Temperaturea di fuga H2O ="+str(tempH2O))
                
                print('--------------------Stato solido delle molecole (Solid state temperatures) --------------------------------------')
                print('--------------H2O(s)----------- T=273.2 K ----------------------')
                print('---------------N2(s)----------- T=63.2 K -----------------------')
                print('---------------O2(s)----------- T=54.2 K -----------------------')
                print('---------------CO2(s)---------- T= 68 K ------------------------')
                  

            t=0
            while t<tf: 
                t+=inct
                beta=wt*t+betazero
                phi=(-a*math.cos(ws*t+teta)+xf)*(math.cos(beta)*math.sin(alfa)*math.cos(omega)-math.cos(alfa)*math.sin(omega))
                phi=phi-b*math.sin(ws*t+teta)*math.sin(beta)*math.sin(alfa)
                phi=phi/math.sqrt((-a*math.cos(ws*t+teta)+xf)**2+b**2*math.sin(ws*t+teta)**2)
                #angle1=math.atan(1/(Au*math.sqrt((-a*math.cos(ws*t+teta)+xf)**2+b**2*math.sin(ws*t+teta)**2)))
                #angle2=math.atan(1/(b*Au))
                phi=phi*(dmin**2/((-a*math.cos(ws*t+teta)+xf)**2+b**2*math.sin(ws*t+teta)**2))
                #print(phi)
                if phi<0:
                    phi=0
                    
                
                philist.append(phi)
                tlist.append(t)
              #  print(philist)
            
            
                
                
            if i==0:
                ax1.plot(tlist, philist, linewidth=2.0, color='blue')
            if i==1:
                ax2.plot(tlist, philist, linewidth=2.0,color='red')
            if i==2:
                ax3.plot(tlist, philist, linewidth=2.0, color='yellow')
            if i==3:
                ax4.plot(tlist, philist, linewidth=2.0,color='green')

            if i==4:
                ax5.plot(tlist, philist, linewidth=2.0,color='purple')
            if i==5:
                ax6.plot(tlist, philist, linewidth=2.0,color='cyan')

            if i==6:
                ax7.plot(tlist, philist, linewidth=2.0,color='pink')

            if i==7:
                ax8.plot(tlist, philist, linewidth=2.0,color='brown')

            if i==8:
                ax9.plot(tlist, philist, linewidth=2.0,color='gold')


        plt.show()
              
 

    
