import os
import pyperclip
from .defaults import EMBED_TEMPLATE    
from .style import color
from .prompts import prompt_directory, prompt_details, CONFIG_FILE, SECTION_NAME, KEY_NAME
from .defaults import default_directory

# Creates the files and returns its contents
def create_file(movie_title, media_link, output_directory):
    output_file_path = os.path.join(output_directory, f'{movie_title}.txt')
    file_content = EMBED_TEMPLATE.format(LINK=media_link)

    with open(output_file_path, 'w') as f:
        f.write(file_content)
    
    return output_file_path, file_content 

# Loop for file and content generation
def create_content():
    movie_titles = []
    embed_contents = []
    new_contents = []
    new_files = []
    count = 0

    output_directory = prompt_directory()

    while True:
        movie_title, media_link = prompt_details()
        print('\n' + color(f'{movie_title}.txt successfully generated and stored in {default_directory()}', None))
        movie_titles.append(f'"{movie_title}"')
        new_file, new_content = create_file(movie_title, media_link, output_directory)  

        embed_content = EMBED_TEMPLATE.format(LINK = media_link)
        embed_contents.append(embed_content) 

        new_files.append(new_file)
        new_contents.append(new_content)  

        continue_prompt = input(color('\nWould you like to create another embed code file? (Y/N): '))
        if continue_prompt.lower() != 'y' or continue_prompt.lower() == '':
            print('\n' + color(f"Embed code(s) for {', '.join(movie_titles)} successfully pasted to clipboard! \nPaste them on the test page to try them out!", None))
            break
    
    pyperclip.copy('\n'.join(embed_contents))
    
    return new_files, new_contents