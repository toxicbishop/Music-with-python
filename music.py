import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def play_music(folder_path, song_file):

    file_path = os.path.join(folder_path, song_file)
    
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        return
    
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print(f"Now playing: {song_file}")
    print("Commands: [P]ause, [R]esume, S[t]op, [Q]uit")
    while True:
        command = input("> ").upper()
        
        if command == 'P':
            pygame.mixer.music.pause()
            print("Music paused.")
        elif command == 'R':
            pygame.mixer.music.unpause()
            print("Music resumed.")
        elif command == 'S':
            pygame.mixer.music.stop()
            print("Music stopped.")
            return
        else:
            print("Invalid Command")

def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Could not initialize mixer: {e}")
        return

    folder_path = "music_files"  

    if not os.path.isdir(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return
    
    mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]

    if not mp3_files:
        print(f"No .mp3 files found inside '{folder_path}'!")
        return

    while True:
        print("\n--- Music Player Menu ---")
        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. Play '{song}'")
        print("0. Exit")

        choice = input("\nEnter song number to play (or press Q to quit): ").strip()

        if choice.upper() == 'Q' or choice == '0':
            print("Exiting...")
            pygame.mixer.music.stop()
            break

        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue # Loop restarts here if input is bad
        
        # --- FIX: Convert to int HERE, after passing the check ---
        choice_idx = int(choice) - 1 

        if 0 <= choice_idx < len(mp3_files):
            play_music(folder_path, mp3_files[choice_idx])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()