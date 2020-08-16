# import the necessary packages
from imagesearch.colordescriptor import ColorDescriptor
from imagesearch.searcher import Searcher
import argparse
import cv2
from matplotlib import pyplot as plt

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result_path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)

# display the query
fig = plt.figure()
ax = fig.add_subplot(4, 3, 1)
query = cv2.cvtColor(query, cv2.COLOR_BGR2RGB)
imgplot = plt.imshow(query)

i = 3 

# loop over the results
for (score, resultID) in results:

	i = i+1

	print(resultID)
	# load the result image and display it
	result = cv2.imread(resultID)
	result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
	ax = fig.add_subplot(4, 3, i)
	imgplot = plt.imshow(result)

	
plt.show()
cv2.waitKey(0)