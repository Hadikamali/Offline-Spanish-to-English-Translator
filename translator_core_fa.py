import argostranslate.package
import argostranslate.translate


class EnglishPersianTranslator:
    def __init__(self):
        self.from_code = "en"  # زبان مبدأ: انگلیسی
        self.to_code = "fa"  # زبان مقصد: فارسی

        # بررسی اینکه آیا پکیج زبان قبلاً دانلود شده است یا خیر
        installed_packages = argostranslate.package.get_installed_packages()
        en_fa_installed = any(
            p.from_code == self.from_code and p.to_code == self.to_code for p in installed_packages
        )

        # اگر دانلود نشده بود، آن را دانلود کن
        if not en_fa_installed:
            print("در حال دانلود مدل مترجم آفلاین (حدود 30 مگابایت)... لطفاً کمی صبر کنید.")
            argostranslate.package.update_package_index()
            available_packages = argostranslate.package.get_available_packages()

            try:
                package_to_install = next(
                    filter(
                        lambda x: x.from_code == self.from_code and x.to_code == self.to_code, available_packages
                    )
                )
                argostranslate.package.install_from_path(package_to_install.download())
                print("دانلود مدل با موفقیت انجام شد!")
            except StopIteration:
                raise Exception("پکیج زبان مورد نظر یافت نشد.")

    def translate(self, text):
        # بررسی خالی نبودن متن
        if not text or not text.strip():
            return ""

        try:
            # ترجمه آفلاین و سریع متن
            return argostranslate.translate.translate(text, self.from_code, self.to_code)
        except Exception as e:
            return f"خطا در ترجمه: {e}"