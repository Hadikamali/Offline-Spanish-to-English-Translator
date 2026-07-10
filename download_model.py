from transformers import MarianMTModel, MarianTokenizer
import os

model_name = "Helsinki-NLP/opus-mt-es-en"
save_dir = "local_model"

print("در حال دانلود و ذخیره مدل (لطفا صبر کنید)...")
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

tokenizer.save_pretrained(save_dir)
model.save_pretrained(save_dir)
print(f"مدل با موفقیت در پوشه {save_dir} ذخیره شد!")
