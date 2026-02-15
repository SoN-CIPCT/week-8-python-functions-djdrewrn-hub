def sandwich_ingredients(*ingredients):
    print("The ingredients for the sandwich are:")
    for ingredient in ingredients:
        print("- " + ingredient)

sandwich_ingredients("white bread", "bacon", "lettuce", "tomato", "mayo")
sandwich_ingredients("rye bread", "corned beef", "sauerkraut", "thousand island dressing", "swiss cheese")


