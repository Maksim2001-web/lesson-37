def all_variants(text):

    if not text:
        yield ""
    else:

        first_char = text[0]
        rest_of_text = text[1:]

        for variant in all_variants(rest_of_text):
            yield variant

        for variant in all_variants(rest_of_text):
            yield first_char + variant

a = all_variants("abc")
for i in a:
    print(i)


