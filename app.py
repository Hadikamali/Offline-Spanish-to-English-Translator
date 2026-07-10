# app.py
import tkinter as tk
from tkinter import messagebox
from translator_core import SpanishEnglishTranslator  # وارد کردن هسته ترجمه از فایل اول


class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("مترجم اسپانیایی به انگلیسی")
        self.root.geometry("600x450")
        self.root.configure(padx=20, pady=20)

        # بارگذاری موتور ترجمه در پس‌زمینه
        self.translator = None

        # اگر مدل بارگذاری نشد، ادامه نده
        if not self.load_translator():
            return

        self.setup_ui()

    def load_translator(self):
        try:
            self.translator = SpanishEnglishTranslator()
            return True  # بارگذاری موفق
        except Exception as e:
            messagebox.showerror("خطا", f"بارگذاری مدل با مشکل مواجه شد. لطفاً نصب بودن torch را بررسی کنید:\n\n{e}")
            self.root.destroy()
            return False  # بارگذاری ناموفق

    def setup_ui(self):
        # بخش ورودی (اسپانیایی)
        tk.Label(self.root, text="متن اسپانیایی (Spanish):", font=("Arial", 11, "bold")).pack(anchor="w")
        self.text_input = tk.Text(self.root, height=7, font=("Arial", 11))
        self.text_input.pack(fill="x", pady=(5, 15))

        # دکمه ترجمه
        self.btn_translate = tk.Button(self.root, text="ترجمه به انگلیسی", font=("Arial", 11, "bold"),
                                       bg="#2196F3", fg="white", command=self.perform_translation)
        self.btn_translate.pack(pady=5)

        # بخش خروجی (انگلیسی)
        tk.Label(self.root, text="ترجمه انگلیسی (English):", font=("Arial", 11, "bold")).pack(anchor="w", pady=(10, 0))
        self.text_output = tk.Text(self.root, height=7, font=("Arial", 11), bg="#f5f5f5")
        self.text_output.pack(fill="x", pady=(5, 5))

    def perform_translation(self):
        spanish_text = self.text_input.get("1.0", tk.END).strip()

        if not spanish_text:
            messagebox.showwarning("هشدار", "لطفاً ابتدا متنی را برای ترجمه وارد کنید.")
            return

        # تغییر وضعیت دکمه برای جلوگیری از کلیک مجدد
        self.btn_translate.config(text="در حال ترجمه...", state=tk.DISABLED)
        self.root.update()

        try:
            # فراخوانی تابع ترجمه از هسته اصلی
            english_text = self.translator.translate(spanish_text)

            # نمایش خروجی
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, english_text)
        except Exception as e:
            messagebox.showerror("خطای ترجمه", f"مشکلی رخ داد:\n{e}")
        finally:
            # بازگرداندن وضعیت دکمه
            self.btn_translate.config(text="ترجمه به انگلیسی", state=tk.NORMAL)


if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
