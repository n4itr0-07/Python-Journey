# Demonstrating various escape sequences

print("Backslash: \\")
print('Single quote: \'')
print("Double quote: \"")
print("ASCII Bell: \a")  # May not produce a visible output
print("Backspace: ABC\bD")  # C replaced by D
print("Formfeed: Hello\fWorld")  # Formfeed character
print("Linefeed: Hello\nWorld")  # Newline character
print("Carriage Return: Hello\rWorld")  # World overwrites Hello
print("Horizontal Tab: Hello\tWorld")  # Horizontal tab space
print("Vertical Tab: Hello\vWorld")  # Vertical tab character
print("Octal value: \101")  # Octal representation of 'A'
print("Hexadecimal value: \x41")  # Hexadecimal representation of 'A'
print("Unicode by name: \N{GREEK SMALL LETTER ALPHA}")  # Unicode name
print("16-bit Unicode: \u03B1")  # 16-bit Unicode
print("32-bit Unicode: \U000003B1")  # 32-bit Unicode
# Escape character \e example (non-standard in Python, may require specific terminal support)
