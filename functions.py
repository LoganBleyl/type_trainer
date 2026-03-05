import random
import datetime
import time
from sentences import sentences

def calculate_accuracy(original, user_input):
    correct_chars = 0
    total_chars = len(original)
    for i in range(total_chars):
        if i < len(user_input) and user_input[i] == original[i]:
            correct_chars += 1
    return (correct_chars / total_chars) * 100 if total_chars > 0 else 0

def calculate_wpm(original, time_taken):
    word_count = len(original.split())
    minutes = time_taken / 60
    return word_count / minutes if minutes > 0 else 0

def display_results(time_taken, accuracy, WPM, sentence, user_input):
    print("\nResults:")

    if accuracy == 100:
        print("\nExcellent! You typed the sentence perfectly!")
    elif accuracy >= 80:
        print("\nGood job! You typed the sentence with few mistakes.")
    elif accuracy >= 50:
        print("\nNot bad! You typed the sentence with some mistakes.")
    else:
        print("\nKeep practicing! You'll get there!")
    
    print(sentence)
    print(user_input)

    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"WPM: {WPM:.2f}")

def save_score(time_taken, accuracy, WPM):
    with open("scores.txt", "a") as file:
        file.write(f"[{datetime.datetime.now()}] Time: {time_taken:.2f} seconds, Accuracy: {accuracy:.2f}%, WPM: {WPM:.2f}\n")
    print("Score saved successfully!")

def show_scores():
    print("\nPrevious Scores:")
    try:
        with open("scores.txt", "r") as file:
            scores = file.readlines()
            for score in scores:
                print(score.strip())
    except FileNotFoundError:
        print("No scores found. Start taking the test to save your scores!")

def run_typing_test():
    print("Welcome to the Typing Speed Test!")
    print("You will be given a sentence to type. Try to type it as quickly and accurately as possible.")
    print("Press Enter when you're ready to start...")
    input()

    sentence = random.choice(sentences)
    print("\nType the following sentence:")
    print(sentence)

    start_time = input("Press Enter to start typing...")
    start_time = time.time()

    user_input = input()
    end_time = time.time()

    time_taken = end_time - start_time
    accuracy = calculate_accuracy(sentence, user_input)
    WPM = calculate_wpm(sentence, time_taken)
    
    display_results(time_taken, accuracy, WPM, sentence, user_input)
    save_score(time_taken, accuracy, WPM)
