# Nearest Hospital Finder

import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as sc

house = np.random.randint(0,30,size = 30*2).reshape(30,2) # 30 Houses
hospital = np.random.randint(0,30,size = 5*2).reshape(5,2) # 5 Hospitals

plt.scatter(house[:,0],house[:,1],lw=1,label ="HOUSE")
plt.scatter(hospital[:,0],hospital[:,1],color = "red",lw=5,label ="HOSPITAL")
plt.title("Nearest Hospital",fontsize=25)

indices = sc.KDTree(hospital).query([house])[1][0]
for each_house,each_hospital in enumerate(indices):
    plt.plot([house[each_house,0],hospital[each_hospital,0]],
             [house[each_house,1],hospital[each_hospital,1]],
             ls="--",color="gray",lw=0.5)

plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
