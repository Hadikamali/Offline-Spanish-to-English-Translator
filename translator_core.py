from transformers import MarianMTModel, MarianTokenizer
import os
import sys


class SpanishEnglishTranslator:
    def __init__(self):
        # پیدا کردن مسیر درست پوشه مدل
        # (حالت اول برای فایل exe و حالت دوم برای اجرای عادی در پایتون)
        if hasattr(sys, '_MEIPASS'):
            self.model_path = os.path.join(sys._MEIPASS, "local_model")
        else:
            self.model_path = os.path.abspath("local_model")

        # بررسی اینکه آیا پوشه مدل واقعاً وجود دارد یا خیر
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(
                f"پوشه مدل در مسیر زیر پیدا نشد:\n{self.model_path}\nلطفاً ابتدا فایل download_model.py را اجرا کنید.")

        # بارگذاری مدل و توکنایزر به صورت کاملاً آفلاین (بدون نیاز به اینترنت)
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_path, local_files_only=True)
        self.model = MarianMTModel.from_pretrained(self.model_path, local_files_only=True)

    def translate(self, text):
        # بررسی خالی بودن متن
        if not text or not text.strip():
            return ""

        # پردازش متن و تبدیل آن به فرمت قابل فهم برای مدل
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)

        # انجام ترجمه (تولید توکن‌های خروجی)
        translated_tokens = self.model.generate(**inputs)

        # تبدیل توکن‌های خروجی به متن قابل خواندن انسان
        translated_text = self.tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

        return translated_text
