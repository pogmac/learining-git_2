print("This is a shopping list")

shopping_list = {
    "bakery": ["bread","bun","baguette"],
    "grocery": ["tomato","orange","apple"]
}

#print(shopping_list)
#print(type(shopping_list))

for k, v in shopping_list.items():
    print(f"I'm going to the {k.capitalize()} and buying ", end ="")
    for i in range(len(v)):
        print(v[i].capitalize(), end = " ")
    print("")

        