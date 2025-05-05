from googletrans import Translator

# Function to perform translation
def translate_text(input_text, source_language, target_language):
    translator = Translator()
    try:
        # Perform translation
        translated = translator.translate(input_text, src=source_language, dest=target_language)
        return translated.text
    except Exception as e:
        return "Error: " + str(e)
