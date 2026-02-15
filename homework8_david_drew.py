def make_sandwich(prepared, *ingredients):
    print(f'\nMaking a {prepared} sandwich with the following ingredients:')
    for ingredient in ingredients:
        print(f'~ {ingredient}')

make_sandwich("toasted","white bread", "bacon", "lettuce", "tomato", "mayo")
make_sandwich("grilled","rye bread", "corned beef", "sauerkraut", "thousand island dressing", "swiss cheese")


