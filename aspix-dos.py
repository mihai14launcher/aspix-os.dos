import os
import sys

# Initialize colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)

# Define the colors and backgrounds
colors = {
    '001': Fore.RED,
    '002': Fore.LIGHTBLUE_EX,
    '003': Fore.BLUE,
    '004': Fore.WHITE,  # default
    '005': Fore.LIGHTBLACK_EX
}

backgrounds = {
    '01': Back.BLACK,
    '02': Back.LIGHTBLACK_EX,
    '03': Back.RED,
    '04': Back.LIGHTBLUE_EX
}

# Variables to track system state
current_color = Fore.WHITE
current_background = Back.BLACK
current_directory = os.getcwd()

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to show support link
def show_support():
    return "Support: Discord : https://discord.gg/PXTtxEK7g8"

# Function to show about information
def show_about():
    return ("AspixOS - DOS\n"
            "Version : 1.0\n"
            "Owned by : mihai_sb_2009\n"
            "Github : mihai14launcher\n"
            "2024 &copy")

# Function to show help information
def show_help():
    return ("Available commands:\n"
            "clear - clear console\n"
            "support - show the support link\n"
            "about - show this information\n"
            "help - show all the commands\n"
            "color - set text color\n"
            "color-help - show the color list with numbers\n"
            "theme - set background color\n"
            "theme-help - show the background theme list with numbers\n"
            "mkdir <directory> - create a new directory\n"
            "cd <directory> - change the current directory\n"
            "cd .. - move up one directory\n"
            "shutdown - exit the OS")

# Function to show color options
def show_color_help():
    return "Color options:\n" + "\n".join([f"{code} - {color}Text Color" for code, color in colors.items()])

# Function to show theme options
def show_theme_help():
    return "Theme options:\n" + "\n".join([f"{code} - {background}Background Theme" for code, background in backgrounds.items()])

# Function to set text color
def set_color(color_code):
    global current_color
    current_color = colors.get(color_code, Fore.WHITE)
    return "Text color changed."

# Function to set background theme
def set_theme(theme_code):
    global current_background
    current_background = backgrounds.get(theme_code, Back.BLACK)
    return "Background theme changed."

# Function to create a new directory
def make_directory(directory_name):
    try:
        os.makedirs(directory_name, exist_ok=False)
        return f"Directory '{directory_name}' created successfully."
    except FileExistsError:
        return f"Error: Directory '{directory_name}' already exists."
    except Exception as e:
        return f"Error: {e}"

# Function to change the current directory
def change_directory(directory_name):
    global current_directory
    try:
        if directory_name == '..':
            current_directory = os.path.dirname(current_directory)
        else:
            new_directory = os.path.join(current_directory, directory_name)
            if os.path.isdir(new_directory):
                current_directory = new_directory
            else:
                return f"Error: Directory '{directory_name}' does not exist."
        os.chdir(current_directory)
        return f"Changed directory to '{current_directory}'."
    except Exception as e:
        return f"Error: {e}"

# Function to shut down the OS
def shutdown_os():
    return "AspixOS now is shutting down, please wait."

# Function to process user commands and return output as a string
def process_command(user_input):
    user_input = user_input.strip().lower()
    output = ""
    
    if user_input == 'clear':
        clear_console()
    elif user_input == 'support':
        output = show_support()
    elif user_input == 'about':
        output = show_about()
    elif user_input == 'help':
        output = show_help()
    elif user_input == 'color-help':
        output = show_color_help()
    elif user_input == 'theme-help':
        output = show_theme_help()
    elif user_input.startswith('color '):
        _, color_code = user_input.split()
        output = set_color(color_code)
    elif user_input.startswith('theme '):
        _, theme_code = user_input.split()
        output = set_theme(theme_code)
    elif user_input.startswith('mkdir '):
        _, dir_name = user_input.split(maxsplit=1)
        output = make_directory(dir_name)
    elif user_input.startswith('cd '):
        _, dir_name = user_input.split(maxsplit=1)
        output = change_directory(dir_name)
    elif user_input == 'shutdown':
        output = shutdown_os()
    else:
        output = "Unknown command. Type 'help' for a list of commands."
    
    return output

# Main function to run the command loop
def main():
    print("Welcome to AspixOS - DOS")
    print("Type 'help' for a list of commands.")
    
    while True:
        user_input = input(f"aspix@local {current_directory} > ")
        output = process_command(user_input)
        if output:
            print(output)

if __name__ == "__main__":
    main()
