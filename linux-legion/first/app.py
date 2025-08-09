#!/usr/bin/exec-suid -- /usr/local/bin/python

import os
import subprocess
import pwd
import grp
import stat
from datetime import datetime
from termcolor import colored
import pyfiglet

def display_art(text, font='block'):
    raw = pyfiglet.figlet_format(text, font=font)
    solid = "".join("█" if c not in (" ", "\n") else c for c in raw)
    return colored(solid, 'yellow')

def explain_ls(args):
    path = '.'
    flags = "".join(arg.replace('-', '') for arg in args)
    long_format = 'l' in flags
    all_files = 'a' in flags
    if long_format and all_files:
        print(display_art('ls -la'))
        print(colored("Perfect! You've combined flags. 'ls -la' gives a detailed listing of ALL files, including hidden ones.", 'green'))
    elif long_format:
        print(display_art('ls -l'))
        print(colored("The 'ls -l' command provides a detailed ('long') listing of visible files.", 'green'))
    elif all_files:
        print(display_art('ls -a'))
        print(colored("The 'ls -a' command lists ALL files and directories, including hidden ones (those starting with '.').", 'green'))
    else:
        print(display_art('ls'))
        print(colored("The 'ls' command lists the visible files and directories in the current location.", 'green'))

    print(colored(f"Here are the contents of '{os.path.abspath(path)}':\n", 'green'))

    try:
        items = os.listdir(path)
        if not all_files:
            items = [item for item in items if not item.startswith('.')]

        for item in sorted(items):
            try:
                full_path = os.path.join(path, item)
                stats = os.stat(full_path)
                mode = stats.st_mode
                
                if long_format:
                    perms = stat.filemode(mode)
                    nlink = stats.st_nlink
                    user = pwd.getpwuid(stats.st_uid).pw_name
                    group = grp.getgrgid(stats.st_gid).gr_name
                    size = stats.st_size
                    mtime = datetime.fromtimestamp(stats.st_mtime).strftime('%b %d %H:%M')
                    
                    color = 'blue' if stat.S_ISDIR(mode) else 'yellow'
                    print(colored(f"{perms} {nlink} {user} {group} {size:4d} {mtime} ", 'white') + colored(item, color))
                else:
                    color = 'blue' if os.path.isdir(full_path) else 'yellow'
                    icon = '📁' if os.path.isdir(full_path) else '📄'
                    print(colored(f"{icon} {item}", color))
            except Exception as e:
                print(colored(f"Could not stat item: {item}, Error: {e}", "red"))

        # Explanations and Hints
        if long_format:
            print(colored("\n---[ Explanation ]---", "cyan"))
            print(colored("d rwx r-x r-x", "yellow") + colored(" -> [d]irectory, [u]ser, [g]roup, [o]thers permissions (read, write, execute).", "white"))
            print(colored("ctf ctf", "yellow") + colored("     -> The user and group that own the file.", "white"))
            print(colored("4096", "yellow") + colored("        -> Size of the file in bytes.", "white"))
            print(colored("Jul 26 03:00", "yellow") + colored("  -> Date and time of last modification.", "white"))

        print(colored("\n---[ Hint ]---", "cyan"))
        in_secret_dir = os.path.basename(os.getcwd()) == '.secret'
        
        if in_secret_dir and 'flag' in items:
            print(colored("The flag is right there! Use the 'cat' command to read its contents.", "magenta"))
        elif long_format and all_files:
            print(colored("This detailed view shows a hidden '.secret' directory. That seems important! Investigate it with 'cd .secret'.", "magenta"))
        elif long_format:
            print(colored("This is a detailed view, but you're only seeing visible files. To see hidden files, combine flags: 'ls -la'.", "magenta"))
        elif all_files:
            print(colored("You can see the hidden '.secret' directory! To get more details about it, try 'ls -l'.", "magenta"))
        else: # Plain 'ls'
            print(colored("This is a simple list. For more details like permissions and size, try 'ls -l'.", "magenta"))

    except Exception as e:
        print(colored(f"Error executing ls: {e}", 'red'))


def explain_cd(path):
    print(display_art('cd'))
    print(colored("The 'cd' command changes your current directory.", 'green'))
    if not path:
        print(colored("Usage: cd <directory>", 'red'))
        return
    try:
        os.chdir(path)
        print(colored(f"Changed directory to '{os.getcwd()}'", 'green'))
        print(colored("\nHint: Now that you're here, use 'ls' to see what's inside.", "magenta"))
    except FileNotFoundError:
        print(colored(f"Error: Directory '{path}' not found.", 'red'))
    except Exception as e:
        print(colored(f"Error: {e}", 'red'))

def explain_cat(file):
    print(display_art('cat'))
    print(colored("The 'cat' command displays the content of a file. It's great for reading short files.", 'green'))
    if not file:
        print(colored("Usage: cat <file>", 'red'))
        return
    try:
        with open(file, 'r') as f:
            content = f.read()
            print(colored(f"--- Content of {file} ---", 'cyan'))
            print(content)
            print(colored(f"--- End of {file} ---", 'cyan'))
            if "pwn.college" in content:
                print(colored("\nCongratulations! You found the flag!", "yellow"))
    except FileNotFoundError:
        print(colored(f"Error: File '{file}' not found.", 'red'))
    except Exception as e:
        print(colored(f"Error: {e}", 'red'))

def main():
    print(colored("Welcome to the Interactive Command Line Challenge!", 'magenta'))
    print(colored("Your mission is to explore this environment and find the hidden flag.", 'magenta'))
    print(colored("Type 'help' to see a list of commands. Start by exploring with 'ls'.\n", 'magenta'))
    print(colored("Do cd /challenge to get to the challenge directory'.\n", 'magenta'))

    # Create a dummy file for the user to see
    with open("/challenge/welcome.txt", "w") as f:
        f.write("This is a test file to make the directory less empty.")

    while True:
        try:
            prompt = colored(f"ctf-user@{os.getcwd()} $ ", 'green')
            command = input(prompt).strip()
            if not command:
                continue

            parts = command.split()
            cmd = parts[0]
            args = parts[1:]

            if cmd == 'ls':
                explain_ls(args)
            elif cmd == 'cd':
                explain_cd(args[0] if args else "")
            elif cmd == 'cat':
                explain_cat(args[0] if args else "")
            elif cmd == 'help':
                print(colored("---[ Commands ]---", 'cyan'))
                print(colored("  ls [options] - List files. Try 'ls -la' for more details.", 'yellow'))
                print(colored("  cd <dir>     - Change directory.", 'yellow'))
                print(colored("  cat <file>   - Read a file's content.", 'yellow'))
                print(colored("  exit         - Exit the challenge.", 'yellow'))
            elif cmd == 'exit':
                break
            else:
                print(colored(f"'{cmd}' is not a recognized command in this tutorial. Try 'help'.", 'red'))

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
