import os
import webbrowser
import configparser
from style import intro, color
from file_generation import create_content
from prompts import prompt_test_html
from test import test_html, open_canvas_test_page
from prompts import CONFIG_FILE, SECTION_NAME, KEY_NAME
 

# Delete current batch of html files
def end_session(new_files, new_contents):
    end_prompt = input(color('\nAre you done with this session? (Y/N): '))
    if end_prompt.lower() == 'y':
        if os.path.exists('temp.html'):
            os.remove('temp.html')

        print(color(f'\n✔ Done!', 'green'))

    else:
        while True:
            print(color('\nA: Start a new batch', 'white'))
            print(color('B: Bring up test page', 'white'))
            print(color('C: Remove the newly created embed code file(s) and restart'))
            print(color('D: End session', 'white'))
            continue_prompt = input(color('What would you like to do? (A/B/C/D): '))
            
            if continue_prompt.lower() == 'a':
                lsstream()
                break
            elif continue_prompt.lower() == 'b':
                webbrowser.open('file://' + os.path.realpath('temp.html'))
                end_session(new_files, new_contents)
                break
            elif continue_prompt.lower() == 'c':
                for file in new_files:
                    os.remove(file)
                if os.path.exists('temp.html'):
                    os.remove('temp.html')
                lsstream()
                break
            elif continue_prompt.lower() == 'd':
                if os.path.exists('temp.html'):
                    os.remove('temp.html')
                    
                print(color(f'\n✔ Done!', 'green'))
                break
            else:
                print(color('\nInvalid option, please choose A, B, C or D.', 'red'))

def lsstream():    
    new_files, new_contents = create_content()

    # if prompt_test_html(new_contents): test_html(new_contents)
    if prompt_test_html(): open_canvas_test_page()

    end_session(new_files, new_contents) 


def main():
    print(color(intro.renderText('LSSTREAM')))

    config = configparser.ConfigParser()

    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
        if SECTION_NAME in config and KEY_NAME in config[SECTION_NAME]:
            directory_name = config[SECTION_NAME][KEY_NAME]
            print(color(f"Your embed code files will be stored here: {directory_name}", 'white'))
        
    lsstream() 

if __name__ == "__main__":
    main()
