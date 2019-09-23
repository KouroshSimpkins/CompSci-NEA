from PIL import Image
import PIL.Image
from pytesseract import image_to_string
import pytesseract
import cv2
import wand

imS = cv2.resize(warped, (1350, 1150))
cv2.imshow("output", imS)
cv2.imwrite('Output Image.PNG', imS)
cv2.waitKey(0)

pytesseract.pytesseract.tesseract_cmd = 'image'
TESSDATA_PREFIX = 'image'
output = pytesseract.image_to_string(PIL.Image.open(
                                    'OutputImage.PNG').convert(
                                    "RGB"), lang='eng')
print(output)
