numbers = ["one", "two", "three"]

# overwrites numbers.txt file if already exists
# to not overwrite, use "a" for append
try:
    with open("numbers.txt", "w") as number_file:
        for n in numbers:
            number_file.write(n + "\n")
except OSError:
    print("Error writing to file.")
