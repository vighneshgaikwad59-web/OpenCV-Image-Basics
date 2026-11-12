# OpenCV Image Basics

A beginner-friendly Python script that explores core image-processing operations using **OpenCV**: loading, flipping, grayscale conversion, cropping, drawing shapes, and saving images.

## Features

| Operation | OpenCV function | Output |
|---|---|---|
| Load image | `cv2.imread()` | Original image window |
| Flip (both axes) | `cv2.flip(img, -1)` | Flipped image window + `flipped_image.png` |
| Grayscale conversion | `cv2.cvtColor(..., cv2.COLOR_BGR2GRAY)` | Grayscale window + `grayscale_image.png` |
| Crop (ROI slicing) | `grey[50:200, 50:200]` | Cropped image window |
| Draw a line | `cv2.line()` | Line image window |
| Draw a rectangle | `cv2.rectangle()` | `rectangle_image.png` |

## Requirements

- Python 3.8+
- OpenCV

```bash
pip install opencv-python
```

## Usage

1. Place your image (e.g. `flower.png`) in a folder.
2. Update the image path in the script:

   ```python
   img = cv2.imread("C:\\Users\\<your-name>\\path\\to\\flower.png")
   ```

3. Run the script:

   ```bash
   python image_operations.py
   ```

4. Press any key while an image window is focused to close all windows and save the output files.

## How it works

1. **Load**: reads the image with `cv2.imread()`. If the path is wrong, it returns `None` and the script prints `image is failed to load`.
2. **Flip**: `flipcode = -1` flips the image both horizontally and vertically (`0` = vertical, `1` = horizontal).
3. **Grayscale**: converts the flipped BGR image to a single-channel grayscale image.
4. **Crop**: NumPy slicing `[y1:y2, x1:x2]` extracts a 150×150 region from the grayscale image.
5. **Draw line**: draws a blue line (BGR `(255, 0, 0)`) with thickness 5 from `(0, 0)` to `(100, 500)`.
6. **Save**: writes results to disk with `cv2.imwrite()`.

## Output files

- `flipped_image.png`
- `grayscale_image.png`
- `rectangle_image.png`

## Notes and common fixes

- **Rectangle needs two corner points.** `cv2.rectangle()` takes `(img, pt1, pt2, color, thickness)`:

  ```python
  rectangle = cv2.rectangle(img, (200, 200), (400, 400), (255, 0, 0), 5)
  ```

- **Draw before saving or showing.** Windows and files only show what was drawn *before* `imshow` / `imwrite` is called.
- **`cv2.line()` and `cv2.rectangle()` modify the original image in place**, so later windows will also show the drawn shapes.
- **Use raw strings or forward slashes for Windows paths**, e.g. `r"C:\Users\..."`.
- On Jupyter or Colab, replace `cv2.imshow()` with `matplotlib.pyplot.imshow()` or `cv2_imshow` (Colab).

## Concepts covered

- Image as a NumPy array (`height × width × channels`)
- BGR colour order in OpenCV (not RGB)
- Region of Interest (ROI) via array slicing
- Drawing primitives on images

## Author

Vighnesh Gaikwad
GitHub: [vighneshgaikwad59-web](https://github.com/vighneshgaikwad59-web)

## License

This project is open for learning and personal use.
