import cv2
img = cv2.imread("C:\\Users\\vigne\\OneDrive\\Desktop\\explor\\flower.png")      # image load
if img is not None:
    print("image is loaded successfully")
    cv2.imshow("window display", img)
    flipped_img = cv2.flip(img, -1)     
    cv2.imshow("flipped images", flipped_img)      # flipped image show
    grey = cv2.cvtColor(flipped_img, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    cv2.imshow("greyscale images", grey)      # grayscale image show
    crop_images=cv2.crop_img = grey[50:200, 50:200]  # crop the grayscale image
    line=cv2.line(img, (0, 0), (100, 500), (255, 0, 0), 5)  # draw a line on the grayscale image
    cv2.imshow("line images", line)      # line image show
    cv2.imshow("cropped images", crop_images)      # cropped image show
    cv2.waitKey(0)                # wait for key press
    cv2.destroyAllWindows()       # close window
    cv2.imwrite("flipped_image.png", flipped_img)  # save the flipped image
    cv2.imwrite("grayscale_image.png", grey)  # save the grayscale image
    rectangle=cv2.rectangle(img,(200,200),(255,0,0),5)  # draw a rectangle on the original image
    cv2.imshow("rectangle images", rectangle)      # rectangle image show
    cv2.imwrite("rectangle_image.png", rectangle)  # save the rectangle image

else:
    print("image is failed to load")