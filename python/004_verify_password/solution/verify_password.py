mdp = input("Enter a password (min 8 characters): ")
mdp_trop_court = "your password is too short."

if len(mdp) == 0:
    print(mdp_trop_court.upper())
    exit()
elif len(mdp) < 8:
    print(mdp_trop_court.capitalize())
    exit()

if mdp.isdigit():
    print("Your password contains only numbers.")
    exit()

print("Registration completed.")