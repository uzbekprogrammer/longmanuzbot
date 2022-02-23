from googletrans import Translator
translator = Translator()
message = "mening ismim Abdurahim"
lang = translator.detect(message).lang
print(lang)

print(translator.translate(message, "en"))
