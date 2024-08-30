my_shopping_list = ["Milk", "Bread", "Butter", "Eggs"]


#  Accessing first item/element
# print(my_shopping_list[0])
#
# #  Accessing all the items/elements
# for items in my_shopping_list:
#     if items[0] == "Milk":
#         print(items[0].upper())
#
# # Length of list
# print("Length:", len(my_shopping_list))
#
#
# # Adding more items to a list
# def bring_more_food(my_list):
#     my_list.append("Cheese")
#     return my_list


# Removing Items from the list
def bring_more_food1(my_list1):
    my_list1.remove("Eggs")
    return my_list1
    # return my_list1


# list_add = bring_more_food(my_shopping_list)
# print(list_add)
list_add1 = bring_more_food1(my_shopping_list)
print(list_add1)


# insert element/item at certain position

def bring_more_food2(my_list1):
    my_list1.insert(2, "Eggs")
    my_list1.insert(2, "Eggs")
    my_list1.insert(2, "Bun")
    return my_list1


insert_at_index = bring_more_food2(my_shopping_list)
print(insert_at_index)
