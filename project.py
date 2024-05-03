import bottle as bot

def main():
    temp = 0
    print("Welcome to Sports Equipment Counter!")
    print("Choose an option:")
    print("1. Login")
    print("2. Sign Up")
    choice = input("--> ")

    if choice == '1':
        design=bot.desig()
        if design ==1:
            login_credentials = bot.read_login_credentials_stud()
            username = bot.login(login_credentials)
            bot.issue(username)
        elif design == 2:
            login_credentials = bot.read_login_credentials_staff()
            username = bot.login(login_credentials)
            bot.Task(username)
        elif design == 3:
            login_credentials = bot.read_login_credentials_visitor()
            username = bot.login(login_credentials)
            bot.issue(username)
        else:
            print("Invalid Choice !")
            bot.sys.exit()
    elif choice == '2':
        bot.Sign_Up()
    else:
        print("Invalid choice!")
        bot.sys.exit()
    if temp == 1:
        print("Welcome, " + username + "!")
        bot.Task(username)
        

if __name__ == "__main__":
    main()
