from textcleaner_partha import preprocess

text = "Ths is <b>reely</b> amazzing 😄🚀!!! I can't beleive it works..."

cleaned = preprocess(
    text,
    lowercase=True,
    remove_html=True,
    remove_emoji=True,
    expand_contraction=True,
    correct_spelling=True,
    lemmatise=True,
    verbose=True  # if you added this
)

print("Original:", text)
print("Cleaned:", cleaned)
