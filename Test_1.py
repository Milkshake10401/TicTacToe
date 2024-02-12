def test():
    print("Hello User!")
    return


def main():
    while True:
        choice = input("Welcome to the my test file. \n"
                       "To begin the test type the word 'ENTER': ")
        if choice == "ENTER":
            test()
            print("This test has been successfully completed")
            break

        else:
            print('The test has completed but the user did not follow instructions :(')
            break
    return 0


if __name__ == '__main__':
    main()
