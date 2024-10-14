
import cv2
import pytesseract
import re

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Change this path if needed

def extract_amount_from_bill(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Preprocess the image if needed (e.g., convert to grayscale)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to do OCR on the image
    extracted_text = pytesseract.image_to_string(gray_image)

    print("Extracted Text:")
    print(extracted_text)

    # Use regex to find the amount in the text (this pattern may need adjustments)
    # This example looks for patterns like $100.00 or 100.00
    amount_pattern = r'(?<=\s)(\$?\d+(?:\.\d{1,2})?)(?=\s|$)'
    amounts = re.findall(amount_pattern, extracted_text)

    if amounts:
        print("Extracted Amounts:")
        for amount in amounts:
            print(amount)
    else:
        print("No amounts found.....")

# Example usage
extract_amount_from_bill("bill2.png")  # Change the path to your bill image
