import tkinter as tk
from googletrans import Translator

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Translator App")

        self.label_text = tk.StringVar()
        self.label_text.set("Masukkan teks untuk diterjemahkan:")
        self.label = tk.Label(master, textvariable=self.label_text)
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=40)
        self.entry.pack(pady=10)

        self.translate_button = tk.Button(master, text="Terjemahkan", command=self.translate_text)
        self.translate_button.pack(pady=10)

        self.translation_label_text = tk.StringVar()
        self.translation_label = tk.Label(master, textvariable=self.translation_label_text)
        self.translation_label.pack(pady=10)

    def translate_text(self):
        input_text = self.entry.get()

        if not input_text:
            self.translation_label_text.set("Masukkan teks terlebih dahulu.")
            return

        translator = Translator()

        try:
            translation_en = translator.translate(input_text, dest='en').text
            translation_lang1 = translator.translate(input_text, dest='fr').text  # Ganti 'fr' dengan kode bahasa yang diinginkan
            translation_lang2 = translator.translate(input_text, dest='es').text  # Ganti 'es' dengan kode bahasa yang diinginkan
            translation_lang3 = translator.translate(input_text, dest='de').text  # Ganti 'de' dengan kode bahasa yang diinginkan

            result_text = f'Inggris: {translation_en}\nPerancis: {translation_lang1}\nPortugis: {translation_lang2}\nJerman: {translation_lang3}'
            self.translation_label_text.set(result_text)

        except Exception as e:
            print(e)
            self.translation_label_text.set("Terjadi kesalahan saat menerjemahkan.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
