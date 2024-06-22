#If you don't give me credit I'll assume you're gay
import pyfiglet
from termcolor import colored
import pyshorteners


url = "LITTLE URL"
print(colored(pyfiglet.figlet_format(url), "green"))
print("-----------------------------------------")
print(colored("AURTHOR : Easin Hossain", "red"))
print(colored("GITHUB  : BCS950", "cyan"))
print(colored("FACEBOOK: EASIN HOSSAIN ", "cyan"))
print("-----------------------------------------")

user = input(">Enter the url: ")
shortener = pyshorteners.Shortener()
bd = shortener.tinyurl.short(user)
print("Hey boss!!  ur link is here👉 : ",  bd)