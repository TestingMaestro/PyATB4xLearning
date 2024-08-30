def make_pizza(*toppings, base):
    print(toppings, base)


# def make_pizza2(base, *toppings): # error [not possible]
#     print(toppings, base)


make_pizza("Mushroom", "tomato", "cheese", base="thin crust")
# make_pizza(base="Mushroom", "tomato", "cheese", "thin crust")

