import os
from .template import TEMPLATE_1     # choose the template you want
from .style import color
from .prompts import prompt_directory, prompt_details

# Creates the files and returns its contents
def create_file(movie_title, media_link, output_directory):
    output_file_path = os.path.join(output_directory, f'{movie_title}.txt')
    file_content = TEMPLATE_1.format(LINK=media_link, TITLE=movie_title)

    with open(output_file_path, 'w') as f:
        f.write(file_content)
    
    return output_file_path, file_content 

# Loop for file and content generation
def create_content():
    new_contents = []
    new_files = []

    output_directory = prompt_directory()

    while True:
        movie_title, media_link = prompt_details()
        new_file, new_content = create_file(movie_title, media_link, output_directory)  

        new_files.append(new_file)
        new_contents.append(new_content)  

        continue_prompt = input(color('\nContinue? (Y/N): ', 'white'))
        if continue_prompt.lower() != 'y':
            break
    
    return new_files, new_contents