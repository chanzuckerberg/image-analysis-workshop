from skimage import restoration  # skimage's restoration submodule.

plane_bilateral = restoration.denoise_bilateral(plane_rescaled)
plane_tv_chambolle = restoration.denoise_tv_chambolle(plane_rescaled)

# Checking the results.
_, (win_left, win_center, win_right) = plt.subplots(nrows=1, ncols=3, figsize=(12, 8))

sc.show_plane(win_left, plane_rescaled, title='Original')
sc.show_plane(win_center, plane_bilateral, title='Bilateral')
sc.show_plane(win_right, plane_tv_chambolle, title='TV Chambolle')
