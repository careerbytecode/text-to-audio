import PyPDF2
import pyttsx3

def pdf_to_speech(pdf_path):
    try:
        # Open the PDF file
        with open(pdf_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""

            # Extract text from each page
            for page in range(len(reader.pages)):
                text += reader.pages[page].extract_text() + "\n"

            # Initialize text-to-speech engine
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()

    except Exception as e:
        print(f"Error: {e}")


# Example usage
pdf_to_speech(r"C:\Users\gayat\Downloads\MLRESUME.pdf")
