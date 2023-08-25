# Set up your default stuff in here, like the embed_template, test page, etc
import configparser
import os
from .prompts import CONFIG_FILE, SECTION_NAME, KEY_NAME
from .style import color

EMBED_TEMPLATE = '<iframe src="{LINK}" width="640" height="360" allow="fullscreen"></iframe>'

TEST_PAGE = 'https://canvas.asu.edu/courses/26086/pages/test-page/edit'


def default_directory():
    config = configparser.ConfigParser()

    if os.path.exists(CONFIG_FILE):
        config.read(CONFIG_FILE)
        if SECTION_NAME in config and KEY_NAME in config[SECTION_NAME]:
            directory_name = config[SECTION_NAME][KEY_NAME]
            directory_name = color(directory_name, None, attrs=["underline"])
    
        return directory_name
