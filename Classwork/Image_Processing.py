import matplotlib.pyplot as plt
from scipy import misc,ndimage
face = misc.face()
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=15)
#Results
plt.imshow(<image to be displayed>)
