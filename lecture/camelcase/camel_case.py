""" Camelcase converter program! """


def main():
    display_banner()
    instructions()
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)


def camelcase(sentence):
    """ Convert sentence to camelCase, for example, "Display all books"
    is converted to "displayAllBooks" """
    title_case = sentence.title()  # Uppercase first letter of each word
    upper_camel_cased = title_case.replace(' ', '')  # remove spaces
    # Lowercase first letter, join with rest of string
    # Slices don't produce index out of bounds errors.
    # So this still works on empty strings, strings of length 1
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]


def display_banner():
    """ Display program name in banner, using stars """
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print(f'\n {stars} \n {msg} \n {stars}\n')


def instructions():
    """ Display instructions for how to use program """
    print("Enter a sentence and this program will convert it to camelcase.")


if __name__ == '__main__':
    main()
