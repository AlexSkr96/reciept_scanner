import cv2
from pytesseract import pytesseract


def parse_image_from_path(image_path, lang="eng"):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return parse_image(gray_image, lang)

def parse_image(image, lang="eng"):
    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = "/usr/bin/tesseract"

    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    try:
        text = pytesseract.image_to_string(image, lang="eng")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    # Displaying the extracted text
    return text
