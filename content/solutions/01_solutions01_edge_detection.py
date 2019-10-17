# Your solution goes here!
plane_sobel_h = filters.sobel_h(plane_rescaled)  # Horizontal Sobel.
plane_sobel_v = filters.sobel_v(plane_rescaled)  # Vertical Sobel.
plane_roberts = filters.roberts(plane_rescaled)  # Roberts.
plane_prewitt = filters.prewitt(plane_rescaled)  # Prewitt.
plane_scharr = filters.scharr(plane_rescaled)  # Scharr.

# Checking the results.
_, ((win_top_left, win_top_center, win_top_right),
    (win_bottom_left, win_bottom_center, win_bottom_right)) = plt.subplots(nrows=2, ncols=3, figsize=(12, 8))

sc.show_plane(win_top_left, plane_rescaled, title='Original')
sc.show_plane(win_top_center, plane_sobel_h, title='Horizontal Sobel')
sc.show_plane(win_top_right, plane_sobel_v, title='Vertical Sobel')

sc.show_plane(win_bottom_left, plane_roberts, title='Roberts')
sc.show_plane(win_bottom_center, plane_prewitt, title='Prewitt')
sc.show_plane(win_bottom_right, plane_scharr, title='Scharr')
