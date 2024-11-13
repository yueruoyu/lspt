def greetings(name_list, mydict):
    return (
        f"Hello, {' '.join(name_list)}! "
        f"Nice to have a {mydict['title']} " 
        f"{mydict['occupation']} around."
    )




greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.