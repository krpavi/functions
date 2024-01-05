# website login
def variable(usr_details, usr_name, password):
    # website login
    i = 0
    while i < 4:
        if usr_name.upper() in usr_details.keys() and password in usr_details.values():
            print("You have logged in")  # logged in successfully if both password and username are correct
            break

        else:  # password is incorrect
            i += 1  # control variable increased by 1 in the next iteration

    else:  # login iteration has exceeded the limit of 4
        print("You have failed to login")


variable(usr_details={"DAVID": 123, "KEVIN": 456, "RICHARD": 789, "ROBERT": 150},
         usr_name=input("Enter your username: "),
         password=int(input("Enter your password: ")))