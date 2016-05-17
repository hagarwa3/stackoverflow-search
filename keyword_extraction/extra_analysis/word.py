#########################################
#	Plotting word clouds for common 	#
#	words in the queries of each		#
#	language being analysed				#
#########################################

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import wordcloud
from wordcloud import WordCloud, ImageColorGenerator

# d = path.dirname(__file__)

# Read the whole text.
text = open('fullfilePython.txt').read()

# read the mask / color image
# taken from http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
alice_coloring = np.array(Image.open( "pythonlogo.png"))

wc = WordCloud(background_color="black", max_words=200, mask=alice_coloring,
               max_font_size=80, random_state=42)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(alice_coloring)

# show
plt.imshow(wc)
plt.axis("off")
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()