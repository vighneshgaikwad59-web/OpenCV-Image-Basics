import cv2 

img = cv2.imread("C:\\Users\\vigne\\OneDrive\\Desktop\\explor\\flower.png")      # image load
if img is not None:
    cropped=img[100:400, 100:400]  # crop the imageq
    cv2.imshow("orginal image", img)      # image show
    cv2.imshow("window display",cropped)
    grey = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("cropped_image.png", cropped)  # save the cropped image
    cv2.imwrite("grayscale_image.png", grey)  # save the grayscale image
