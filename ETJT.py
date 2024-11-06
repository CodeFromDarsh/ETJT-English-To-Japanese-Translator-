from googletrans import Translator, LANGUAGES

def translate_to_japanese(text):
    try:
        # Initialize the Translator
        translator = Translator()

        # Translate the text to Japanese
        translation = translator.translate(text, src='en', dest='ja')

        # Return the translated text
        return translation.text
    except Exception as e:
        return f"Error: {e}"

def main():
    # Get input text from the user
    english_text = input("Enter text in English: ")

    # Translate to Japanese
    japanese_translation = translate_to_japanese(english_text)

    # Output the translated text
    print(f"Translated text in Japanese: {japanese_translation}")

if __name__ == "__main__":
    main()
