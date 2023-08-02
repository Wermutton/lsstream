import os
import pyperclip
from .defaults import EMBED_TEMPLATE     # choose the template you want
from .style import color
from .prompts import prompt_directory, prompt_details

# Creates the files and returns its contents
def create_file(movie_title, media_link, output_directory):
    output_file_path = os.path.join(output_directory, f'{movie_title}.txt')
    file_content = EMBED_TEMPLATE.format(LINK=media_link, TITLE=movie_title)

    with open(output_file_path, 'w') as f:
        f.write(file_content)
    
    return output_file_path, file_content 

# Sets up the embed code and places it in user's clipboard
def embed_clipboard(movie_title, media_link):
    embed_content = EMBED_TEMPLATE.format(LINK=media_link, TITLE=movie_title)
    
    # Copy the file content to clipboard
    pyperclip.copy(embed_content)

    return f"✔ Embed code for \"{movie_title}\" successfully pasted to clipboard!"


# Loop for file and content generation
def create_content():
    new_contents = []
    new_files = []

    output_directory = prompt_directory()

    while True:
        movie_title, media_link = prompt_details()
        new_file, new_content = create_file(movie_title, media_link, output_directory)  
        print('\n', color(embed_clipboard(movie_title, media_link), 'green'))

        new_files.append(new_file)
        new_contents.append(new_content)  

        continue_prompt = input(color('\nContinue? (Y/N): ', 'white'))
        if continue_prompt.lower() != 'y':
            break
    
    return new_files, new_contents