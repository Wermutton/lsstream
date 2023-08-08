import os
import pyperclip
from defaults import EMBED_TEMPLATE    
from style import color
from prompts import prompt_directory, prompt_details

# Creates the files and returns its contents
def create_file(movie_title, media_link, output_directory):
    output_file_path = os.path.join(output_directory, f'{movie_title}.txt')
    file_content = EMBED_TEMPLATE.format(LINK=media_link, TITLE=movie_title)

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
        movie_titles.append(f'"{movie_title}"')
        new_file, new_content = create_file(movie_title, media_link, output_directory)  

        embed_content = EMBED_TEMPLATE.format(LINK = media_link, TITLE = movie_title)
        embed_contents.append(embed_content) 

        new_files.append(new_file)
        new_contents.append(new_content)  

        continue_prompt = input(color('\nWould you like to create another embed code file? (Y/N): '))
        if continue_prompt.lower() != 'y':
            print('\n', color(f"✔ Embed code(s) for {', '.join(movie_titles)} successfully pasted to clipboard!", 'white'))
            break
    
    pyperclip.copy('\n'.join(embed_contents))
    
    return new_files, new_contents