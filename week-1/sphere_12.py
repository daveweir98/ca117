import sys
from math import pi

h1 = "Radius (m)"
h2 = "-" * 10
h3 = "Area (m^2)"
h4 = "Volume (m^3)"
h5 = "-" * 12

print ("{0:>s} {1:>15s} {2:>15s}".format(h1, h3, h4) )
print ("{0:>s} {0:>15s} {1:>15s}".format(h2, h5))

n = float(sys.argv[1])
step = float(sys.argv[2])
end = float(sys.argv[3])

while n <= end:
    area = 4 * pi *(n ** 2)
    volume = (4/3) * pi * (n ** 3)
    print ("{0:>10.1f} {1:>15.2f} {2:>15.2f}".format(n, area, volume))
    n += step
