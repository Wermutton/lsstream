from .style import color
import os

# Prompt users for the output directory
def prompt_directory():
    output_directory = input(color('\nWhere do you want the files stored?: '))

    if os.path.isdir(output_directory):
        return output_directory
    else:
        print(color("Invalid directory, please enter a valid directory.", 'red'))
        return prompt_directory()

# Prompt users for movie details
def prompt_details():
    movie_title = input(color('\nEnter the Media Title: '))
    media_link = input(color('\nEnter the Media Link: '))

    return movie_title, media_link

# Prompts users if they want to test the links
def prompt_test_html(new_links):
    test_prompt = input(color('\nDo you want to test the media(s)? (Y/N): ', 'cyan'))
    if test_prompt.lower() == 'y':
        return True
