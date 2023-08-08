from style import color
import os
import configparser

CONFIG_FILE = 'config.ini'
SECTION_NAME = 'Settings'
KEY_NAME = 'PreferredDirectory'

# Prompt users for the output directory
def prompt_directory():
    config = configparser.ConfigParser()

    # If the config file exists, try to read the preferred directory
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
        if SECTION_NAME in config and KEY_NAME in config[SECTION_NAME]:
            return config[SECTION_NAME][KEY_NAME]

    # If we didn't return above, we need to ask the user for the directory
    output_directory = input(color('\nWhere do you want the files stored?: '))
    if not os.path.isdir(output_directory):
        print(color("Invalid directory, please enter a valid directory.", 'red'))
        return prompt_directory()

    # Save the preferred directory in the config file
    if SECTION_NAME not in config:
        config.add_section(SECTION_NAME)
    config[SECTION_NAME][KEY_NAME] = output_directory
    with open(CONFIG_FILE, 'w') as config_file:
        config.write(config_file)

    return output_directory


# Prompt users for movie details
def prompt_details():
    movie_title = input(color('\nEnter the Media Title: '))
    media_link = input(color('\nEnter the Media Embed Code: '))

    return movie_title, media_link

# Prompts users if they want to test the links
def prompt_test_html():
    test_prompt = input(color('\nWould you like to try out the embed code(s) on the test page? (Y/N): '))
    if test_prompt.lower() == 'y':
        return True
    
def prompt_update_preferred_directory():
    config = configparser.ConfigParser()

    # Prompt the user for the new directory
    new_directory = input('\nEnter the new preferred directory: ')
    if not os.path.isdir(new_directory):
        print(color("Invalid directory, please enter a valid directory.", 'red'))
        return prompt_update_preferred_directory()

    # Update the config file with the new directory
    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
        if SECTION_NAME not in config:
            config.add_section(SECTION_NAME)
        config[SECTION_NAME][KEY_NAME] = new_directory
        with open(CONFIG_FILE, 'w') as config_file:
            config.write(config_file)

    print(color("Preferred directory updated successfully!", 'white'))

    return new_directory

