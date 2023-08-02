import webbrowser
import os
from .defaults import TEST_PAGE

# Tests the .txt contents on Browser
def test_html(contents):
    with open('temp.html', 'w') as f:
        for content in contents:
            f.write(content + '\n')
        
    webbrowser.open('file://' + os.path.realpath('temp.html'))


test_page_opened = False

def open_canvas_test_page():
    global test_page_opened
    if not test_page_opened:
        webbrowser.open(TEST_PAGE)
        test_page_opened = True


