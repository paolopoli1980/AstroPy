import numpy as np

n=500
majoraxis=np.abs(np.random.normal(0.25,5,n))
ts=np.abs(np.random.normal(10,300,n))
tp=np.abs(np.random.normal(10,500,n))
rp=np.random.uniform(10**6,9*10**6,n)
albedo=np.random.uniform(0.05,0.5,n)
tilting=np.random.uniform(0,180,n)
densityp=np.random.uniform(900,6000,n)

media = 0.1
deviazione_standard =0.08
e=np.abs(np.random.normal(media,deviazione_standard,n))

nome_file='dataplanets.dat'

with open(nome_file, 'w') as file:
    for i in range(n):
        file.write(f"{ts[i]},{tp[i]},{e[i]*1},{tilting[i]},{majoraxis[i]},{rp[i]},{densityp[i]},{albedo[i]}\n")


    file.write(f" 365.0000000000000,24.00000000000000,0.01670000000000000,23.500000000000000,1.0000000000000000,6400000.000000000,5510.000000000000,0.30000000000000000")
print('fine')
