def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    
    capitalized_names = fullname.upper()
    name_list = capitalized_names.split()
    
    name_init = []
    for i in name_list:
        name_init.append(i[0])
        
    return ''.join(name_init)


def main():
    fullname = input("Please enter your name:")
    initials = get_initials(fullname)
    print("The initials of", fullname, "are", initials)


if __name__ == "__main__":
    main()