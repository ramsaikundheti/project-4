import random

def flip_coin():
    return random.choice(["Heads", "Tails"])

def main():
    while True:
        try:
            num_flips = int(input("Enter the number of times you want to flip the coin: "))
            if num_flips <= 0:
                print("Please enter a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        heads_count = 0
        tails_count = 0
        
        for _ in range(num_flips):
            result = flip_coin()
            print(result)
            if result == "Heads":
                heads_count += 1
            else:
                tails_count += 1
        
        print("\nResults:")
        print(f"Heads: {heads_count} ({(heads_count / num_flips) * 100:.2f}%)")
        print(f"Tails: {tails_count} ({(tails_count / num_flips) * 100:.2f}%)")
        
        again = input("Do you want to flip again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
