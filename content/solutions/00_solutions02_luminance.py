from skimage import color, img_as_float

image = img_as_float(io.imread('../data/balloon.jpg'))

gray = color.rgb2gray(image)
my_gray = image @ [0.2126, 0.7152, 0.0722]

# --- display the results ---

f, (ax0, ax1) = plt.subplots(1, 2, figsize=(10, 6))

ax0.imshow(gray, cmap='gray')
ax0.set_title('skimage.color.rgb2gray')

ax1.imshow(my_gray, cmap='gray')
ax1.set_title('my rgb2gray')
