from functions import show_scores, run_typing_test

def main():
    while True:
        print("\nTyping Speed Test Menu:")
        print("1. Start Typing Test")
        print("2. View Previous Scores")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            run_typing_test()
        elif choice == '2':
            show_scores()
        elif choice == '3':
            print("Thank you for using the Typing Speed Test. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
