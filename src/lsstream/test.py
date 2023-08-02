import webbrowser
from defaults import TEST_PAGE
import os

# Tests the .txt contents on Browser
def test_html(contents):
    with open('temp.html', 'w') as f:
        for content in contents:
            f.write(content + '\n')
        
    webbrowser.open('file://' + os.path.realpath('temp.html'))


# Opens a "Default Test page" on canvas so users can test it 
def open_canvas_test_page():
    webbrowser.open(TEST_PAGE)

