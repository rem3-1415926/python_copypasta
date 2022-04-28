import numpy as np
import matplotlib.pyplot as plt
import csv 
import sys 

"""
ila data contains 2 16bit values of a sine + cosine, and an angle which 
they represent (in 1024 bit/rotation). 
! file reading could be done more elegant with np.loadtxt() !
"""

FILE = "iladata_rev.csv"
if len(sys.argv) == 2:
	FILE = sys.argv[1]

lines = []
with open(FILE, "r") as file:
	reader = csv.reader(file)

	for line in reader:
		lines.append(line)

labels = lines[0]
units = lines[1]
data = np.array(lines[2:]).T

for i, l in enumerate(labels):
	if str.find(l, "xlslice_0_Dout_p1") >= 0:
		p1_idx = i 
for i, l in enumerate(labels):
	if str.find(l, "xlslice_1_Dout") >= 0:
		p2_idx = i 
for i, l in enumerate(labels):
	if str.find(l, "expected_angle") >= 0:
		exp_angle_idx = i 

p1 = data[p1_idx].astype(int)
p2 = data[p2_idx].astype(int)
exp_angle = data[exp_angle_idx].astype(int)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(p1)
ax1.plot(p2)
ax2.plot(exp_angle, color="green")

plt.show()