from transformers import MT5ForConditionalGeneration, MT5Tokenizer
import os

model_name = "persiannlp/mt5-small-parsinlu-translation_en_fa"
save_dir = "local_model_fa"

print("در حال دانلود مدل ParsINLU (حجم حدود 1.2 گیگابایت)...")
tokenizer = MT5Tokenizer.from_pretrained(model_name)
model = MT5ForConditionalGeneration.from_pretrained(model_name)

tokenizer.save_pretrained(save_dir)
model.save_pretrained(save_dir)
print("دانلود با موفقیت انجام شد!")