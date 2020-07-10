le = open("usernames.txt", "r")
        for name in txtFile:
            print(name.rstrip("\n"))
            # print(name[:-2])
            user = api.get_user(name)
            pr