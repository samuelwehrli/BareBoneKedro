import numpy as np
from colorsys import hls_to_rgb

def xyz_to_rgb(x, y, z):
    """
    Convert (X, Y, Z) coordinates on the unit sphere into an RGB color.
    - X and Z determine the Hue (angle in X-Z plane).
    - Y determines the Lightness.
    - Saturation is fixed at 1 for full color.

    Returns: (R, G, B) tuple in range [0,1].
    """
    # Compute Hue from X, Y (atan2 maps angle from [-pi, pi])
    hue = -(np.arctan2(z, x) / (2 * np.pi)) % 1 # Normalize to [0, 1]

    # Lightness directly from Z (rescale from [-1, 1] to [0, 1])
    lightness = ((1+y)/2)

    if hasattr(hue, '__iter__') or hasattr(lightness, '__iter__'):
        return [hls_to_rgb(h, l, 1) for h, l in zip(hue, lightness)]
    else:
        return hls_to_rgb(hue, lightness, 1)  # Saturation fixed at 1