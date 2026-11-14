import cv2
from tkinter import Tk, filedialog


def get_image_path():
    """File picker kholo, user image select kare."""
    root = Tk()
    root.withdraw()                      # chhota khali window chhupao
    root.attributes("-topmost", True)    # picker sabse upar aaye
    path = filedialog.askopenfilename(title="Image select karo")
    root.destroy()
    return path


# 1. Image load (user ki di hui image)
image_path = get_image_path()
img = cv2.imread(image_path) if image_path else None

if img is not None:
    print("image is loaded successfully")
    h, w = img.shape[:2]
    print(f"Image size: {w} x {h}")
    cv2.imshow("window display", img)

    # 2. Flip (-1 = horizontal + vertical)
    flipped_img = cv2.flip(img, -1)
    cv2.imshow("flipped images", flipped_img)

    # 3. Grayscale (flipped image se)
    grey = cv2.cvtColor(flipped_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("greyscale images", grey)

    # 4. Crop (image chhoti ho to bhi error na aaye)
    crop_images = grey[50:min(200, h), 50:min(200, w)]
    cv2.imshow("cropped images", crop_images)

    # 5. Line (original ki COPY par)
    line_img = img.copy()
    cv2.line(line_img, (0, 0), (100, 500), (255, 0, 0), 5)
    cv2.imshow("line images", line_img)

    # 6. Rectangle (original ki COPY par)
    rect_img = img.copy()
    cv2.rectangle(rect_img, (200, 200), (400, 400), (255, 0, 0), 5)
    cv2.imshow("rectangle images", rect_img)

    # 7. Key press ka wait, phir windows band
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 8. Save outputs
    cv2.imwrite("flipped_image.png", flipped_img)
    cv2.imwrite("grayscale_image.png", grey)
    cv2.imwrite("cropped_image.png", crop_images)
    cv2.imwrite("line_image.png", line_img)
    cv2.imwrite("rectangle_image.png", rect_img)
    print("all images saved successfully")
else:
    print("image is failed to load (path check karo)")