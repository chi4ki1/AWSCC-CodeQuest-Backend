shopping_list = []

while True:
        print("\n")
        print("───────── ⋆⋅ ♰ ⋅⋆ ─────────")
        print("Options: \n1. Add item to the shopping list\n2. View shopping list\n3. Remove item from the shopping list\n4. Quit")
        print("───────── ⋆⋅ ♰ ⋅⋆ ─────────")
        
        user_choice= int(input("Enter the number of your choice: "))
        
        if user_choice == 1:
                item = input("Enter the item you want to add:")
                shopping_list.append(item)
                print("\n")
                print(item, "has been added to your shopping list.")
                
        elif user_choice == 2:
                print("\n")
                print("───────── ⋆⋅ ♰ ⋅⋆ ─────────")
                print("Your shopping list: \n")
                for item in shopping_list:
                        print(item)
                print("───────── ⋆⋅ ♰ ⋅⋆ ─────────")
        elif user_choice == 3:
                item_to_remove = input("Enter the item you want to remove: ")

                if item_to_remove in shopping_list:
                        shopping_list.remove(item_to_remove)
                        print("\n")
                        print(item_to_remove, "has been removed from your shopping list.")
                else:
                        print(item_to_remove, "is not in your shopping list.")
        elif user_choice == 4:
                print("\n")
                print("───────── ⋆⋅ ♰ ⋅⋆ ─────────")
                print("         Goodbye!         ")
                print("───────── ⋆⋅ ♰ ⋅⋆ ─────────")
                exit()
else:
        print("Input a valid option from the choices given!")
