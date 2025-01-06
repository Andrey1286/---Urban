def all_variants(text):
    counter = 1
    if counter <= len(text):
        for element in text:
            yield element
            counter += 1
    if counter > len(text):
        counter1 = 0
        for _ in range(len(text)):
            if counter1 < (len(text) - 1):
                yield text[0 + counter1] + text[1 + counter1]
                counter1 += 1
            else:
                yield text
                break


a = all_variants("abc")
for i in a:
    print(i)
