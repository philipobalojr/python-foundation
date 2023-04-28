# Defining a car wash function, this will execute with no error
# def wash_car():
#     print("Wash with tri-color foam")
#     print("Rinse twice")
#     print("Dry with large blow dryer")

#     print("Wash with white foam")
#     print("Rinse once")
#     print("Air dry") 

# wash_car()


# Let us modify this function to allow for payments of two categories
# def wash_car():    # an error will occur (name 'amount_paid' is not defined)

#     if (amount_paid == 12):
#         print("Wash with tri-color foam")
#         print("Rinse twice")
#         print("Dry with large blow dryer")

#     if (amount_paid == 6):
#         print("Wash with white foam")
#         print("Rinse once")
#         print("Air dry")    

# wash_car()


# more modification  and this step will give us error (TypeError: wash_car() missing 1 required positional argument: 'amount_paid')
# def wash_car(amount_paid):
#     if (amount_paid == 12):
#         print("Wash with tri-color foam")
#         print("Rinse twice")
#         print("Dry with large blow dryer")

#     if (amount_paid == 6):
#         print("Wash with white foam")
#         print("Rinse once")
#         print("Air dry") 

# wash_car()


# More improvement by subtituting 6 as the parameter (argument)
def wash_car(amount_paid):
    if (amount_paid == 12):
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    if (amount_paid == 6):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 

wash_car(6)