import re

# Function to check if a string is a keyword
def is_keyword(token):
    keywords = {"int", "float", "double", "char", "if", "else", "while", "for", "return"}
    return token in keywords

# Function to check if a string is an identifier
def is_identifier(token):
    return re.match(r'^[a-zA-Z_]\w*$', token) is not None

# Function to check if a string is an operator
def is_operator(token):
    operators = {'+', '-', '*', '/', '=', '<', '>', '&', '|', '!', '%', '^'}
    return token in operators

def main():
    source_code = input("Enter the source code: ")

    # Tokenize the source code
    tokens = re.findall(r'[a-zA-Z_]\w*|[-+*/=<>&|!%^]', source_code)

    print("Tokens:")
    for token in tokens:
        if is_keyword(token):
            print("Keyword:", token)
        elif is_identifier(token):
            print("Identifier:", token)
        elif is_operator(token):
            print("Operator:", token)

if __name__ == "__main__":
    main()
