import random

print("Hello, welcome to Find the Stuffy! A simple game where you find a hidden stuffy in a room.")
print("A stuffy is a stuffed animal, like a teddy bear or a plushie.")
print("You will have 3 chances to find the stuffy in a room, so choose carefully!. ;)")
print("If you find it, you win! :) If not, you lose. :(")
print("Let's start the game!")

def find_stuffy():
    room_items = ["couch", "table", "shelf", "bed", "closet", "drawer", "curtain", "rug",
                   "toy box", "bookshelf"]
    stuffy_location = random.choice(room_items)
    
    print("The stuffy is hidden in one of these items:")
    for item in room_items:
        print(f"- {item}")

    attempts = 3
    while attempts > 0:
        guess = input("Where do you think the stuffy is hidden? ").strip().lower()
        
        if guess == stuffy_location:
            print("Congratulations! You found the stuffy!")
            return
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
    
    print(f"Sorry, you couldn't find the stuffy. It was hidden in the {stuffy_location}.")

if __name__ == "__main__":
    find_stuffy()
