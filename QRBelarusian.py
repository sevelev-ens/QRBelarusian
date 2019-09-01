import sys


import numpy as np

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    border=0,
)
qr.add_data(sys.argv[1])
qr.make(fit=True)
array=np.array(qr.get_matrix()).astype(int)

# Generating image


coarse=10
span=1.2
internal_span=35
linem1="""
</svg>"""

xs=[]
ys=[]
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        x=i-j
        y=i+j
        xs+=[x]*array[i][j]
        ys+=[y]*array[i][j]
xsm=min(xs)
ysm=min(ys)
xrange=max(xs)-xsm
yrange=max(ys)-ysm
print(yrange)

line0="""<?xml version="1.0" standalone="no"?>
<svg width="{:.1f}" height="{:.1f}" version="1.1" xmlns="http://www.w3.org/2000/svg">
""".format(47/internal_span*(xrange+span)*coarse,47/internal_span*(yrange+span)*coarse)
xs=list(map((lambda x:x-xsm),xs))
ys=list(map((lambda x:x-ysm),ys))
internallines=[]
shift=(47-internal_span)/internal_span*(yrange+span)/2
for (x,y) in zip(xs,ys):
    internallines+=['<rect x="{:.1f}" y="{:.1f}" width="{:.1f}" height="{:.1f}" fill="black" stroke-width="0"/>'.format((x+shift)*coarse,(y+shift)*coarse,span*coarse,span*coarse)]
############################################# outer ornments
addy=[0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 21, 21, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 25, 25, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 41, 41, 42, 43, 43, 43, 44, 44, 44, 44, 45, 45, 45, 46]
addx=[23, 22, 23, 24, 21, 22, 24, 25, 22, 23, 24, 23, 11, 36, 8, 11, 12, 35, 36, 39, 7, 8, 9, 11, 12, 13, 34, 35, 36, 38, 39, 40, 8, 9, 11, 12, 13, 14, 33, 34, 35, 36, 38, 39, 11, 12, 13, 14, 33, 34, 35, 36, 6, 7, 8, 9, 10, 12, 13, 14, 33, 34, 35, 37, 38, 39, 40, 41, 7, 8, 9, 10, 11, 13, 14, 33, 34, 36, 37, 38, 39, 40, 8, 9, 10, 11, 12, 14, 33, 35, 36, 37, 38, 39, 9, 10, 11, 12, 13, 34, 35, 36, 37, 38, 2, 44, 1, 2, 3, 43, 44, 45, 0, 1, 3, 4, 42, 43, 45, 46, 1, 2, 3, 43, 44, 45, 2, 44, 9, 10, 11, 12, 13, 34, 35, 36, 37, 38, 8, 9, 10, 11, 12, 14, 33, 35, 36, 37, 38, 39, 7, 8, 9, 10, 11, 13, 14, 33, 34, 36, 37, 38, 39, 40, 6, 7, 8, 9, 10, 12, 13, 14, 33, 34, 35, 37, 38, 39, 40, 41, 11, 12, 13, 14, 33, 34, 35, 36, 8, 9, 11, 12, 13, 14, 33, 34, 35, 36, 38, 39, 7, 8, 9, 11, 12, 13, 34, 35, 36, 38, 39, 40, 8, 11, 12, 35, 36, 39, 11, 36, 23, 22, 23, 24, 21, 22, 24, 25, 22, 23, 24, 23]
coarse_out=(xrange+span)*coarse/internal_span
for (x,y) in zip(addx,addy):
    internallines+=['<rect x="{:.1f}" y="{:.1f}" width="{:.1f}" height="{:.1f}" fill="black" stroke-width="0"/>'.format(x*coarse_out,y*coarse_out,coarse_out,coarse_out)]
#############################################


# In[122]:


filename="/home/maxwell/Desktop/web app/svg/"+"temp.svg"
with open(sys.argv[1].replace("/","")+".svg", "w") as fout:
    fout.write(line0+"\n".join(internallines)+linem1)

