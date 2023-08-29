# Import necessary libraries
from glob import glob
from sunpy.map import Map
import numpy as np
import multiprocessing
import sunpy.io
import sunpy.map
from sunkit_image.coalignment import mapsequence_coalign_by_match_template as mc_coalign
from astropy.coordinates import SkyCoord
import astropy.units as u
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import matplotlib.animation as anim

# Define the paths for Continuum and Dopplergram data
c_sun = glob("Continuum/*")
dop_sun = glob("Dopplergram/*")

# Coordinates for submap
bottom_left = SkyCoord(200*u.arcsec, 400*u.arcsec, frame=map1.coordinate_frame)
top_right = SkyCoord(-100*u.arcsec, 200*u.arcsec,  frame=map1.coordinate_frame)

# Create a Map Sequence for both Continuum and Dopplergram data
sun = [c_sun, dop_sun]
map_sequence = []
for j in range(len(sun)):
    mps = []
    for i in range(len(sun[j])):
        mapa = Map(sun[j][i])
        submap = mapa.submap(bottom_left, top_right=top_right)
        mps.append(submap)
    
    map_seq = sunpy.map.MapSequence(mps)
    map_sequence.append(map_seq)

# Perform data co-alignment using matching templates
dop_al = []
cont_al = []
for j in range(len(sun)):
    algn = mc_coalign(map_sequence[j])
    for i in range(len(algn)):
        data = algn[i].data
    
        if j == 0:
            cont_al.append(data)

        if j == 1:
            dop_al.append(data)
        
aligned_data = [cont_al, dop_al]

# Create animations for the aligned data
for i in range(len(sun)):
    if i == 0:
        fig = plt.figure()
        im = plt.imshow(cont_al[0], interpolation="lanczos", cmap="gray", origin="lower")
        title = plt.title("")
        
        def update(t):
            im.set_array(cont_al[t])
            title.set_text(str(t))        

        ani = anim.FuncAnimation(fig, func=update, frames=80, repeat=False, interval=150)
        ani.save("Continuum_aligned.mp4", dpi=100)
        plt.show()
        
    if i == 1:
        fig = plt.figure()
        im = plt.imshow(dop_al[0], interpolation="lanczos", cmap="gray", origin="lower")
        title = plt.title("")

        def update(t):
            im.set_array(dop_al[t])
            title.set_text(str(t))        

        ani = anim.FuncAnimation(fig, func=update, frames=80, repeat=False, interval=150)
        ani.save("Dopplergram_aligned.mp4", dpi=100)
        plt.show()

# Generate data cubes
arr = np.zeros((len(sun[0]), dop_al[0].shape[0], 579), float)
for i in range(len(dop_al)):
    if dop_al[i].shape[1] == (dop_al[0].shape[1]) - 1:
        zeros = [0] * dop_al[0].shape[0]
        dop_al[i] = np.resize(dop_al[i], (dop_al[0].shape[0], dop_al[0].shape[1]))
