def uppercase(text):
    list_of_text = [i for i in text]
    list_upper_case = [i.upper() for i in text]
    for letter in list_upper_case:
        if letter in list_of_text:
            list_of_text.remove(letter)
    if len(list_of_text) == 0:
        return "Yes"
    else:
        return "No"


print(uppercase(""))




