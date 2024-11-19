# hello.py

from termcolor import colored
import emoji

def hello():
    print(colored(emoji.emojize("🌎 Hello, World! :sparkles:"), "cyan"))

if __name__ == "__main__":
    hello()
