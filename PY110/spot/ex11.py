# Write a function that, given a URL as a string, parses out just the domain
# name and returns it.

# Examples:

# def domain_name(string):
#     domain = ''
#     label = string[::-1].index('moc.')
#     for char in string[::-1][label + 4:]:
#         if char.isalpha():
#             domain = char + domain
#         else:
#             break
#     return domain


def domain_name(url):
    # Remove the protocol if it exists
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]
    
    # Remove "www." if it exists
    if url.startswith("www."):
        url = url[4:]
    
    # Split the URL by dots
    parts = url.split('.')
    
    # If there's more than two parts, the main domain is likely the second-to-last part
    if len(parts) > 2:
        return parts[-2]
    else:
        return parts[0]

print(domain_name("http://github.com/carbonfive/raygun")) # should return "github"
print(domain_name("https://www.cnet.com")) # should return "cnet"