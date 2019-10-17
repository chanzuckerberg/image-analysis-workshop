# Your solution goes here!

# First, let's create a version using histogram equalization.
plane_equalized = exposure.equalize_hist(plane)

# Now, a version using CLAHE.
plane_clahe = exposure.equalize_adapthist(plane)

# Let's check the results.
_, ((win_top_left, win_top_center, win_top_right),
    (win_bottom_left, win_bottom_center, win_bottom_right)) = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))

# On the top, the 2D plots...
sc.show_plane(win_top_left, plane, title='Original')
sc.show_plane(win_top_center, plane_equalized, title='Histogram equalization')
sc.show_plane(win_top_right, plane_clahe, title='CLAHE')

# ... on the bottom, the histograms.
sc.plot_hist(win_bottom_left, plane)
sc.plot_hist(win_bottom_center, plane_equalized)
sc.plot_hist(win_bottom_right, plane_clahe)
