import cv2 

img = cv2.imread("C:\\Users\\vigne\\OneDrive\\Desktop\\explor\\flower.png")      # image load
if img is None:
    print("image is failed to load")
else:
    print("image is loaded successfully")
    resx = cv2.resize(img, (500, 500))  # resize image

    cv2.imshow("window display", img)      # image show
    cv2.imshow("window display", resx)      # image show

    cv2.imwrite("resized_image.png", resx)  # save the resized image

    cv2.waitKey(0)                # wait for key press
    cv2.destroyAllWindows()       # close window

print("DONE!! ")

  

