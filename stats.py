def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    dictionary = {}
    for char in text:
        lower = char.lower()
        if lower not in dictionary: 
            dictionary[lower] = 1
            continue
        dictionary[lower] += 1
    return dictionary

def format_count(text):
    count = count_chars(text)
    arr = []
    for item in count:
        arr.append({"char": item, "num": count[item]})
    arr.sort(key=lambda item: item["num"], reverse=True)
    return arr

