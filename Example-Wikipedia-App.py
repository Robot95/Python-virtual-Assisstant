
import wikipedia

# Takes the input and prints the summary of the entered keyword
while True:
        input = raw_input("Q: ")
        print wikipedia.summary(input)
