# Import threshold and gray convertor functions
from skimage.filters import threshold_yen
from skimage.color import rgb2gray

# Turn the image grayscale
gray_tools_image = rgb2gray(tools_image)

# Obtain the optimal thresh
thresh = threshold_yen(gray_tools_image)

# Obtain the binary image by applying thresholding
binary_image = gray_tools_image > thresh

# Show the resulting binary image
show_image(binary_image, 'Binarized image')


# from skimage.filters import try_all_threshold
# fig, ax = try_all_threshold(gray_tools_image, verbose='False')
# plt.show()