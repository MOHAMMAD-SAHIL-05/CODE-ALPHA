import tkinter as tk
from tkinter import messagebox
from func import translate_text  # Import the translation function

# Function to handle "Enter" key event
def on_enter_key(event):
    translate_text_ui()

# Function to handle translation in UI
def translate_text_ui():
    # Get the text to be translated
    input_text = text_to_translate.get("1.0", "end-1c")
    source_language = source_lang.get()
    target_language = target_lang.get()

    # Call the translation function
    translated = translate_text(input_text, source_language, target_language)

    # Display translated text in the output box
    translated_text.delete("1.0", "end-1c")
    translated_text.insert("1.0", translated)

# Create the main window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("500x500")
root.config(bg="#F0F0F0")

# Set fonts and styles
font = ("Arial", 12)

# Frame for input and output sections
frame = tk.Frame(root, bg="#F0F0F0")
frame.pack(pady=10)

# Source Language Selection
source_lang_label = tk.Label(frame, text="From Language:", font=font, bg="#F0F0F0")
source_lang_label.grid(row=0, column=0, padx=10, pady=10)

source_lang = tk.StringVar(root)
source_lang.set('English')  # default source language is English

source_lang_menu = tk.OptionMenu(frame, source_lang, 
    'English', 'Spanish', 'French', 'German', 'Hindi', 'Japanese', 'Chinese (Simplified)', 'Arabic', 
    'Italian', 'Portuguese', 'Russian', 'Bengali', 'Tamil', 'Telugu', 'Marathi', 'Gujarati', 'Malayalam', 'Kannada', 'Punjabi', 'Odia')
source_lang_menu.config(font=font, width=20)
source_lang_menu.grid(row=0, column=1, padx=10, pady=10)

# Target Language Selection
target_lang_label = tk.Label(frame, text="To Language:", font=font, bg="#F0F0F0")
target_lang_label.grid(row=1, column=0, padx=10, pady=10)

target_lang = tk.StringVar(root)
target_lang.set('Kannada')  # default target language is Kannada

target_lang_menu = tk.OptionMenu(frame, target_lang, 
    'English', 'Spanish', 'French', 'German', 'Hindi', 'Japanese', 'Chinese (Simplified)', 'Arabic', 
    'Italian', 'Portuguese', 'Russian', 'Bengali', 'Tamil', 'Telugu', 'Marathi', 'Gujarati', 'Malayalam', 'Kannada', 'Punjabi', 'Odia')
target_lang_menu.config(font=font, width=20)
target_lang_menu.grid(row=1, column=1, padx=10, pady=10)

# Text box for user input
text_to_translate = tk.Text(root, height=6, width=40, font=font, wrap=tk.WORD)
text_to_translate.pack(pady=10)

# Translate button
translate_button = tk.Button(root, text="Translate", font=font, bg="#4CAF50", fg="white", command=translate_text_ui, relief=tk.RAISED)
translate_button.pack(pady=10)

# Text box for translated output
translated_text = tk.Text(root, height=6, width=40, font=font, wrap=tk.WORD)
translated_text.pack(pady=10)

# Bind the "Enter" key to trigger translation
root.bind('<Return>', on_enter_key)

# Run the application
root.mainloop()
