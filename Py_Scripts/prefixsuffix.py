# Remove prefix/suffix from string.

links = [                                       # Define a list of website URLs
    "www.duckduckgo.com",                   # First URL
    "www.youtube.com",                      # Second URL
    "www.google.com",                       # Third URL
    "www.wikipedia.org"                     # Fourth URL
]

print('-Remove "www." Prefix-')             # Print intent
for link in links:                          # Loop through each URL in the list
    print(link.removeprefix("www."))        # Print the URL without the 'www.' prefix

print('\n-Remove ".com" Suffix-')           # Print new line and intent
for link in links:                          # Loop through each URL in the list
    print(link.removesuffix(".com"))        # Print the URL without the '.com' suffix