import time
os.system('pip install colorama')
from colorama import init, Fore, Back

# Initialize colorama
init(autoreset=True)

# Define the updating message frames
frames = [
    f"{Fore.YELLOW}{Back.BLUE}  Tool Under Update  {Back.RESET}{Fore.RESET}",
    f"{Fore.YELLOW}{Back.BLUE}  Tool Under Update. {Back.RESET}{Fore.RESET}",
    f"{Fore.YELLOW}{Back.BLUE}  Tool Under Update..{Back.RESET}{Fore.RESET}",
    f"{Fore.YELLOW}{Back.BLUE}  Tool Under Update..{Back.RESET}{Fore.RESET}",
    f"{Fore.YELLOW}{Back.BLUE}  Tool Under Update.{Back.RESET}{Fore.RESET}",
    f"{Fore.YELLOW}{Back.BLUE}  Tool Under Update {Back.RESET}{Fore.RESET}",
]

def display_animated_message(frames, duration=0.5):
    for frame in frames:
        print("\033[F" + frame)
        time.sleep(duration)

print("Updating the Tool...")
display_animated_message(frames)
print("Update complete! Tool will be available soon.")
