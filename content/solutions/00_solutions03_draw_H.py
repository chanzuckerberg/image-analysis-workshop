def draw_H(image, coords, color=(0, 255, 0)):
    out = image.copy()
    arm_width = 5
    height = 36
    width = 30

    # Make the left arm
    out[coords[0]:coords[0]+height, coords[1]:coords[1]+arm_width] = color

    # Make the right arm
    out[coords[0]:coords[0]+height, coords[1]+width-arm_width:coords[1]+width] = color

    # Make the strut
    out[coords[0]+height//2-arm_width//2:coords[0]+height//2+arm_width//2+1, coords[1]:coords[1]+width] = color

    return out
