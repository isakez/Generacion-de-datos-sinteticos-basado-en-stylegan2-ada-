import cv2
from skimage.restoration import denoise_nl_means, estimate_sigma
import numpy as np

def resize_image(image, target_size):
    resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_LINEAR)
    return resized_image



def denoise_image(image):
    sigma_est = np.mean(estimate_sigma(image, multichannel=False))
    denoised_image = denoise_nl_means(image, h=1.15 * sigma_est, fast_mode=True, patch_size=5, patch_distance=3, multichannel=False)
    return denoised_image

def normalize_image(image):
    normalized_image = image / 255.0
    return normalized_image

# O utilizando CLAHE
def apply_clahe(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    normalized_image = clahe.apply(image)
    return normalized_image