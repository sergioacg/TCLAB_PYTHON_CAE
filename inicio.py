# install tclab
import tclab_cae.tclab_cae as tclab       
import time
lab = tclab.TCLab_CAE()
lab.LED(100)  # turn on LED
time.sleep(5) # wait 5 seconds
lab.LED(0)    # turn off LED
lab.close()