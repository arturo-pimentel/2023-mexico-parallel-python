import time
import os

N_p=N_t=4
for np in range(N_p):
    for nt in range(N_t):
        print("Processing NP ["+str(np+1)+"], NT["+str(nt+1)+"].")
        start = time.time()
        cmd = "python process_multiple_images.py "+str(np+1)+" "+str(nt+1)+" images/*.png"
        os.system(cmd)
        end = time.time()
        print("Total time: "+str(end-start))

