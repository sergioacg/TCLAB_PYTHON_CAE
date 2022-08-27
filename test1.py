import tclab_cae.tclab_cae as tclab    
import time

lab = tclab.TCLab_CAE()

print('Turn on heaters and LED for 20 seconds')
lab.Q1(50)
lab.Q2(50)
lab.LED(50)

for i in range(21):
    print('Time:',i,'T1:',lab.T1,'T2:',lab.T2,'T3:',lab.T3
           ,'I1:',lab.I1,'I2:',lab.I2)
    time.sleep(1)
    
lab.Q1(0); lab.Q2(0); lab.LED(0)
lab.close()