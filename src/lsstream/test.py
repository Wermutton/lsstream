import webbrowser
import os
from .defaults import TEST_PAGE

# Tests the .txt contents on Browser
def test_html(contents):
    with open('temp.html', 'w') as f:
        f.write('<html><head><style>')
        f.write('''
        .video-container {
            position: relative;
        }
        .title {
            position: absolute;
            top: 0;
            left: 0;
            color: white;
            background-color: rgba(0,0,0,0.7);
            padding: 5px;
        }
        </style></head><body>''')
        for content in contents:
            f.write(content + '\n')
        f.write('</body></html>')
        
    webbrowser.open('file://' + os.path.realpath('temp.html'))



# test_page_opened = False

# def open_canvas_test_page():
#     if not test_page_opened:
#         webbrowser.open(TEST_PAGE)
#         test_page_opened = True


def open_canvas_test_page():
    webbrowser.open(TEST_PAGE)

# async def automate_test():
#     browser = await launch(headless=False)
#     page = await browser.newPage()
#     await page.goto('https://canvas.asu.edu/courses/26086/pages/test-page/edit')

#     selectorForViewTab = '#tinymce-parent-of-wiki_page_body > div > div:nth-child(3) > div > div.tox-editor-container > div.tox-editor-header > div.tox-menubar > button:nth-child(2)'

#     # Wait for the selector to be available
#     await page.waitForSelector(selectorForViewTab, timeout=60000) 

#     await page.click(selectorForViewTab)





