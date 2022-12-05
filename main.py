import cv2
import pytesseract as pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def get_text(path: str) -> str:
    img = cv2.imread(path)
    if img is not None:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return pytesseract.image_to_string(img_rgb)
    else:
        return ":("


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_text("t1.png"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
