import random
import time

# Number of horses and track length definition
NUM_HORSES = 4
TRACK_LENGTH = 40

# Simulate clearing the console by printing blank lines
def clear_console():
    print("\n" * 33)

# Print the racetrack with the current positions of the horses
def print_track(horses):
    clear_console()
    print("🏇 Horse Track Dash! 🏇\n")
    for i in range(NUM_HORSES):
        track = ['-'] * TRACK_LENGTH
        position = horses[i]
        if position < TRACK_LENGTH:
            track[position] = '🐎'  # Position of the horse
        else:
            track[-1] = '🏁'  # Finish line
        print(f"Horse {i + 1}: " + ''.join(track))
    print("\n" + "🌟" * 46)

# Initialize horses' positions
horses = [0] * NUM_HORSES

# Welcome message and start prompt
print("\n🌟 Welcome to Horse Track Dash! 🌟\n")
input("Press Enter to start the race...")

# Main game loop
while max(horses) < TRACK_LENGTH:
    for i in range(NUM_HORSES):
        # Move each horse a random number of steps between 1 and 3
        horses[i] += random.randint(1, 3)

    # Print the updated track
    print_track(horses)

    # Pause briefly for animation effect
    time.sleep(0.5)

# Determine the winner (the horse with the maximum position)
winner = horses.index(max(horses)) + 1
print("\n" + "🎉" * 15)
print(f"🏆 Horse {winner} wins the race! 🏆")
print("🎉" * 15)
