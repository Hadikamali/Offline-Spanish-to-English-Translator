import tkinter as tk
from tkinter import messagebox
# وارد کردن کلاس جدید از فایل اول (نام فایل اول خود را به جای translator_core قرار دهید)
from translator_core_fa import EnglishPersianTranslator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("مترجم انگلیسی به فارسی")
        self.root.geometry("600x450")
        self.root.configure(padx=20, pady=20)

        self.translator = None

        if not self.load_translator():
            return

        self.setup_ui()

    def load_translator(self):
        try:
            # استفاده از کلاس جدید
            self.translator = EnglishPersianTranslator()
            return True
        except Exception as e:
            messagebox.showerror("خطا", f"بارگذاری مدل با مشکل مواجه شد:\n\n{e}")
            self.root.destroy()
            return False

    def setup_ui(self):
        # بخش ورودی (انگلیسی)
        tk.Label(self.root, text="متن انگلیسی (English):", font=("Arial", 11, "bold")).pack(anchor="w")
        self.text_input = tk.Text(self.root, height=7, font=("Arial", 11))
        self.text_input.pack(fill="x", pady=(5, 15))

        # دکمه ترجمه
        self.btn_translate = tk.Button(self.root, text="ترجمه به فارسی", font=("Arial", 11, "bold"),
                                       bg="#2196F3", fg="white", command=self.perform_translation)
        self.btn_translate.pack(pady=5)

        # بخش خروجی (فارسی)
        tk.Label(self.root, text="ترجمه فارسی (Persian):", font=("Arial", 11, "bold")).pack(anchor="w", pady=(10, 0))
        self.text_output = tk.Text(self.root, height=7, font=("Arial", 11), bg="#f5f5f5")
        self.text_output.pack(fill="x", pady=(5, 5))

    def perform_translation(self):
        # دریافت متن انگلیسی
        english_text = self.text_input.get("1.0", tk.END).strip()

        if not english_text:
            messagebox.showwarning("هشدار", "لطفاً ابتدا متنی را برای ترجمه وارد کنید.")
            return

        self.btn_translate.config(text="در حال ترجمه...", state=tk.DISABLED)
        self.root.update()

        try:
            # ترجمه متن
            persian_text = self.translator.translate(english_text)

            # نمایش خروجی
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, persian_text)
        except Exception as e:
            messagebox.showerror("خطای ترجمه", f"مشکلی رخ داد:\n{e}")
        finally:
            self.btn_translate.config(text="ترجمه به فارسی", state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()