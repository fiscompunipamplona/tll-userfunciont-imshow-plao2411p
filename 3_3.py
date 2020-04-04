from pylab import imshow, gray,show
from numpy import loadtxt
data = loadtxt("/home/plao/metnu/Virtuales/calse2/codigos/stm.txt",float)
imshow(data, origin="lower")
gray()
show() 