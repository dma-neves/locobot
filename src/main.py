import sys
import json

from locobot import Locobot

def print_help():
    print(f"usage: python {sys.argv[0]} config_file.json")
    print("See config/example.json for reference")
    print()
    print("command prompts:")
    print("""
    help:   show this help message 
    quit:   quit the chat bot
    ls:     list files from your project found by locobot
          """)

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print_help()
        exit(0)
        
    with open(sys.argv[1]) as f:
        config = json.load(f)
        root_dir_end = config["root_directory"].split("/")[-1]
        print(f"locobot> Hi I'm locobot, a Local Coding chat Bot. I'm here to help you with your project <{root_dir_end}>. Ask me anything.")
        
        running = True
        bot = Locobot(config["root_directory"], config["include_extensions"], config["exclude_paths"])
        
        while running:
            print()
            prompt = input("you> ")
            if prompt.lower() == "quit":
                running = False
            elif prompt.lower() == "help":
                print_help()
            elif prompt.lower() == "ls":
                print(bot.get_file_list())
            else:
                response = bot.submit_prompt(prompt)
                print()
                print("locobot> ", end="")
                
                for chunk in response:
                    print(chunk['message']['content'], end="")
                print()