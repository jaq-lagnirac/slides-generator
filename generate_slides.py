# Justin Caringal
# Takes a directory of images and converts them into a
# .pptx presentation/slides deck

# libraries
import os
import sys
import logging
import argparse
from pptx import Presentation

# logging formatting
SCRIPT_PATH = os.path.abspath(__file__)
FORMAT = '[%(asctime)s] %(levelname)s %(message)s'
l = logging.getLogger()
lh = logging.StreamHandler()
lh.setFormatter(logging.Formatter(FORMAT))
l.addHandler(lh)
l.setLevel(logging.INFO)
debug = l.debug; info = l.info; warning = l.warning; error = l.error

# argparse constants
DESCRIPTION = '''
'''
EPILOG = '''
'''


def check_dir(dir : str) -> None:
    """checks the existence of the dir
    
    A function to ensure the directory exists before
    executing the rest of the program

    Args:
        dir (str): a relative path to the input dir
    
    Returns:
        None (exits program early if dir does not exist)

    """

    if not os.path.exists(dir):
        error(f'Directory {dir} not found.')
        sys.exit(1)

    return


def main() -> None:
    """MAIN FUNCTION"""

    # checks existence of dir
    check_dir(args.dir)
    # inits presentation
    prez = Presentation()

    for x in os.listdir(args.dir):
        img_path = os.path.join(args.dir, x)


    # for i, x in enumerate(prez.slide_layouts):
    #     print(i, x.name)
    #
    # 0 Title Slide
    # 1 Title and Content
    # 2 Section Header
    # 3 Two Content
    # 4 Comparison
    # 5 Title Only
    # 6 Blank
    # 7 Content with Caption
    # 8 Picture with Caption
    # 9 Title and Vertical Text
    # 10 Vertical Title and Text
        
    slide = prez.slides.add_slide(prez.slide_layouts[8])
    for x in slide.placeholders:
        print(x.name)
    
    print('-----')

    # for x in os.listdir(args.dir):
    #     print(os.path.join(args.dir, x))
    #
    # Title 1
    # Picture Placeholder 2
    # Text Placeholder 3

    sys.exit()
    
    placeholder = slide.placeholders[1]  # idx key, not position

    # picture = placeholder.insert_picture('my-image.png')
    # title_slide_layout = prez.slide_layouts[0]
    # slide = prez.slides.add_slide(title_slide_layout)
    # title = slide.shapes.title
    # subtitle = slide.placeholders[1]

    # title.text = 'Hello, World!'
    # subtitle.text = 'python-pptx was here!'

    prez.save('test.pptx')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)
    parser.add_argument('dir',
                        help='relpath to directory of images')
    parser.add_argument('-v', '--verbose',
                    action='store_true',
                    help='Set logging level to DEBUG')
    args = parser.parse_args()

    if args.verbose:
        l.setLevel(logging.DEBUG)

    main()