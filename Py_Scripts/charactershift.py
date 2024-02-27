# Create characters on any side of string up to defined (total) count.

text = `Flaming Dumpster`    # Define variable

print(f'{text}')             # Print variable
print(f'{text:#<20}')        # Print variable with four "#" characters to the right
print(f'{text:.>20}')        # Print variable with four "." characters to the left
print(f'{text:_^20}')        # Print variable with four "_" characters, two on the left, two on the right