import os
import webbrowser
from .style import intro, color
from .file_generation import create_content
from .prompts import prompt_test_html
from .test import test_html

# Delete current batch of html files
def end_session(new_files, new_contents):
    end_prompt = input(color('\nAre you done with this session? (Y/N): ', 'white'))
    if end_prompt.lower() == 'y':
        if os.path.exists('temp.html'):
            os.remove('temp.html')

        print(color(f'\n✔ Done!', 'green'))

    else:
        while True:
            print(color('\nA: Start a new batch?', 'yellow'))
            print(color('B: Test the media(s)?', 'cyan'))
            print(color('C: Remove the newly created files and restart?', 'red'))
            print(color('D: End session?', 'green'))
            continue_prompt = input(color('What would you like to do? (', 'white') + color('A', 'yellow') + color('/', 'white') + color('B', 'cyan') + color('/', 'white') + color('C', 'red') + color('/', 'white') + color('D', 'green') + color('): ', 'white'))
            
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
                print(color('\nInvalid option, please choose A, B, or C.', 'red'))

def lsstream():    
    new_files, new_contents = create_content()

    if prompt_test_html(new_contents): test_html(new_contents)

    end_session(new_files, new_contents) 


def main():
    print(color(intro.renderText('LSSTREAM'), 'green'))
    lsstream() 

if __name__ == "__main__":
    main()
