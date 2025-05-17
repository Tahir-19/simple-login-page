import re
import getpass
from datetime import datetime
from colorama import init, Fore, Back, Style
import time

# Initialize colorama
init()

class SocialMediaLogin:
    def __init__(self):
        self.users = {}  # Dictionary to store user credentials
        self.current_user = None
        self.logo = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  {Fore.YELLOW}██╗    ██╗███████╗██╗      ██████╗ ██████╗██╗  ██╗{Fore.CYAN}  ║
║  {Fore.YELLOW}██║    ██║██╔════╝██║     ██╔═══██╗██╔════╝██║ ██╔╝{Fore.CYAN}  ║
║  {Fore.YELLOW}██║ █╗ ██║█████╗  ██║     ██║   ██║██║     █████╔╝ {Fore.CYAN}  ║
║  {Fore.YELLOW}██║███╗██║██╔══╝  ██║     ██║   ██║██║     ██╔═██╗ {Fore.CYAN}  ║
║  {Fore.YELLOW}╚███╔███╔╝███████╗███████╗╚██████╔╝╚██████╗██║  ██╗{Fore.CYAN}  ║
║  {Fore.YELLOW} ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝{Fore.CYAN}  ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""

    def print_success(self, message):
        print(f"\n{Fore.GREEN}✓ {message}{Style.RESET_ALL}")

    def print_error(self, message):
        print(f"\n{Fore.RED}✗ {message}{Style.RESET_ALL}")

    def print_info(self, message):
        print(f"\n{Fore.BLUE}ℹ {message}{Style.RESET_ALL}")

    def loading_animation(self, message, duration=2):
        print(f"\n{Fore.YELLOW}{message}", end="")
        for _ in range(duration * 10):
            print(".", end="", flush=True)
            time.sleep(0.1)
        print(f"{Style.RESET_ALL}")

    def validate_email(self, email):
        # Basic email validation using regex
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def validate_password(self, password):
        # Password must be at least 8 characters long and contain at least one number
        return len(password) >= 8 and any(char.isdigit() for char in password)

    def register(self):
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"║{Fore.WHITE}                     REGISTRATION                      {Fore.CYAN}║")
        print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        while True:
            email = input(f"\n{Fore.CYAN}Enter your email: {Style.RESET_ALL}")
            if not self.validate_email(email):
                self.print_error("Invalid email format! Please try again.")
                continue
            if email in self.users:
                self.print_error("Email already registered! Please login or use a different email.")
                return
            
            password = getpass.getpass(f"{Fore.CYAN}Enter your password (min 8 chars, at least 1 number): {Style.RESET_ALL}")
            if not self.validate_password(password):
                self.print_error("Password must be at least 8 characters long and contain at least one number!")
                continue
            
            confirm_password = getpass.getpass(f"{Fore.CYAN}Confirm your password: {Style.RESET_ALL}")
            if password != confirm_password:
                self.print_error("Passwords do not match!")
                continue
            
            # Store user data
            self.users[email] = {
                'password': password,
                'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.loading_animation("Creating your account")
            self.print_success("Registration successful! You can now login.")
            break

    def login(self):
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
        print(f"║{Fore.WHITE}                         LOGIN                          {Fore.CYAN}║")
        print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
        email = input(f"\n{Fore.CYAN}Enter your email: {Style.RESET_ALL}")
        password = getpass.getpass(f"{Fore.CYAN}Enter your password: {Style.RESET_ALL}")
        
        self.loading_animation("Verifying credentials")
        
        if email in self.users and self.users[email]['password'] == password:
            self.current_user = email
            self.print_success(f"Welcome back, {email}!")
            self.print_info(f"Last login: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return True
        else:
            self.print_error("Invalid email or password!")
            return False

    def logout(self):
        if self.current_user:
            self.loading_animation("Logging out")
            self.print_success(f"Goodbye, {self.current_user}!")
            self.current_user = None
        else:
            self.print_error("You are not logged in!")

    def show_menu(self):
        while True:
            print(self.logo)
            print(f"{Fore.CYAN}╔══════════════════════════════════════════════════════════╗")
            if not self.current_user:
                print(f"║{Fore.WHITE}                     MAIN MENU                        {Fore.CYAN}║")
                print(f"║{Fore.WHITE}  1. Register                                        {Fore.CYAN}║")
                print(f"║{Fore.WHITE}  2. Login                                           {Fore.CYAN}║")
                print(f"║{Fore.WHITE}  3. Exit                                            {Fore.CYAN}║")
            else:
                print(f"║{Fore.WHITE}                     MAIN MENU                        {Fore.CYAN}║")
                print(f"║{Fore.WHITE}  Logged in as: {Fore.GREEN}{self.current_user}{Fore.WHITE}{' ' * (35 - len(self.current_user))}{Fore.CYAN}║")
                print(f"║{Fore.WHITE}  1. Logout                                          {Fore.CYAN}║")
                print(f"║{Fore.WHITE}  2. Exit                                            {Fore.CYAN}║")
            print(f"╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
            
            choice = input(f"\n{Fore.CYAN}Enter your choice: {Style.RESET_ALL}")
            
            if not self.current_user:
                if choice == '1':
                    self.register()
                elif choice == '2':
                    self.login()
                elif choice == '3':
                    self.print_info("Thank you for using our platform!")
                    break
                else:
                    self.print_error("Invalid choice! Please try again.")
            else:
                if choice == '1':
                    self.logout()
                elif choice == '2':
                    self.print_info("Thank you for using our platform!")
                    break
                else:
                    self.print_error("Invalid choice! Please try again.")

if __name__ == "__main__":
    social_media = SocialMediaLogin()
    social_media.show_menu() 