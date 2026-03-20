import os # Interacts with the Operative System
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
    # We hide the "Hello from the pygame community. https://www.pygame.org/contribute.html" pygame library support message at the start

# Libraries that we need to install: (python -m pip install)
import pygame # Has an audio mixer
import keyboard # For special keys like spacebar

    # FUNCTIONS:
def PlaySoundtrack(folder, soundtrack_name):

    file_path = os.path.join(folder, soundtrack_name)
    paused = False

    if not os.path.exists(file_path):
        print("ERR0R! File not found")
        return
    
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print(f"Now playing: {soundtrack_name}")
    print(" Press spacebar to pause or resume")
    print(" Press escape to exit")

    while True:
        evento = keyboard.read_event()
        if evento.event_type == keyboard.KEY_UP:
            if evento.name == "space":
                if paused == False:
                    pygame.mixer.music.pause()
                    paused = True
                    #print("Paused")
                elif paused == True:
                    pygame.mixer.music.unpause()
                    paused = False
                    #print("Resumed")
                else:
                    print("ERR0R! How the fuck did you reach this error?")
            if evento.name == "esc":
                pygame.mixer.music.stop()
                return
        

def main():
    try:
        pygame.mixer.init() # We initialize the music mixer
    except pygame.error as e:
        print("ERR0R! ", e)
        return
    
    folder = "MusicExamples"

    if not os.path.isdir(folder):
        print(f"ERR0R! Folder '{folder}' not found")
        return
    
    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]
        # Only return the .mp3 files of the folder

    while True:
        if not mp3_files:
            print("ERR0R! Zero mp3 files found")
        else:
            print("My list:")
            print("0. Exit")
            for index, soundtrack in enumerate(mp3_files, start = 1): 
                print(f"{index}. {soundtrack}")
        choice_input = input("Enter the soundtrack to play or 0 to Exit:")
        if choice_input == '0':
            print("Doing this thing...")
            break
        elif not choice_input.isdigit():
            print("ERR0R! Selecet a valid soundtrack")
            continue

        choice = int(choice_input)-1

        if 0 <= choice < len(mp3_files):
            PlaySoundtrack(folder, mp3_files[choice])
        else:
            print("ERR0R! Invalid choice")

if __name__ == "__main__": #In case is import as module in other script
    main()