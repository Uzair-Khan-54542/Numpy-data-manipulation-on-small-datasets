import numpy as np 

# 6. Simple image as array.
'''
# ========================================================================
# ========================== S T A R T ============================================
# ========================================================================


# 5 × 5 grayscale image (values 0–255)
pixels = np.array([
    [  0,  50, 100, 150, 200],
    [ 30,  80, 130, 180, 230],
    [ 60, 110, 160, 210, 255],
    [ 20,  70, 120, 170, 220],
    [ 10,  90, 140, 190, 240]
])



# ========================================================================
# Increasing brighteness of image by 40 piexls.
pixels[:, :] += 40


# ========================================================================
# Ensuring pixels don't exceed range of 255 after increasing brightness.
indexes = np.where(pixels > 255)
pixels[indexes] = 255


# ========================================================================
# Flipping the image horizontally.
flipped_pixels_horizontal = np.fliplr(pixels)


# ========================================================================
# Flipping the image horizontally.
flipped_pixels_vertical = np.flipud(pixels)


# ========================================================================
# Croppping the center of the image.
center_cropped = pixels[1:4, 1:4]



# ========================================================================
# Printing statements.
print(f'{pixels}\n')
# print(f'{flipped_pixels_horizontal}\n')
# print(f'{flipped_pixels_vertical}\n')
print(f'{center_cropped}\n')



# ========================================================================
# ========================== E N D ============================================
# ========================================================================

'''


