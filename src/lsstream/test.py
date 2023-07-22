import webbrowser
import os

# Tests the .txt contents on Browser
def test_html(contents):
    with open('temp.html', 'w') as f:
        for content in contents:
            f.write(content + '\n')
        
    webbrowser.open('file://' + os.path.realpath('temp.html'))