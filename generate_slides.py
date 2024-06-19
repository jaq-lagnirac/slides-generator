# Justin Caringal
# Takes a directory of images and converts them into a
# .pptx presentation/slides deck

# libraries
import os
import sys
import logging
import argparse
from pptx import Presentation
from PIL import Image

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

# constants
ACCEPTABLE_IMG_TYPES = ['.jpg', '.png', '.jpeg']


def check_dir(dir : str) -> str:
    """checks the existence of the dir
    
    A function to ensure the directory exists before
    executing the rest of the program

    Args:
        dir (str): a relative path to the input dir
    
    Returns:
        str: Returns name of directory

    """

    if not os.path.exists(dir):
        error(f'Directory {dir} not found.')
        sys.exit(1)

    if not os.path.isdir(dir):
        error(f'Input {dir} is not a directory.')
        sys.exit(1)
    
    dirname = os.path.split(os.path.dirname(dir))[-1] # takes last value
    print(dirname)

    return dirname


def is_image(file : str) -> bool | str:
    """checks if file is an acceptable image format
    
    A function to check the validity of the image

    Args:
        file (str) : the basename of the file

    Returns:
        bool: Returns True if filetype is acceptable, false otherwise

    """

    _, ext = os.path.splitext(file)

    if ext.lower() not in ACCEPTABLE_IMG_TYPES:
        error(f'{file} is not an acceptable image type.')
        return False
    
    return True


def main() -> None:
    """MAIN FUNCTION"""

    # checks existence of dir, extracts dirname
    dirname = check_dir(args.dir)

    print(args.dir)
    print(os.path.dirname(args.dir))
    # inits presentation
    prez = Presentation()
    
    # adds title slide
    slide = prez.slides.add_slide(prez.slide_layouts[0]) # pos=0, Title Slide
    title = slide.shapes.title
    subtitle = slide.placeholders[1]

    # formats title slide
    title.text = dirname
    subtitle.text = 'Created using tools developed by Justin Caringal'

    # iterates through image directory to create slides
    for img_basename in os.listdir(args.dir):
        # creates relative path to image
        img_path = os.path.join(args.dir, img_basename)

        # creates new slide
        slide = prez.slides.add_slide(prez.slide_layouts[8]) # pos=8, Picture with Caption
        
        # creates placeholders using idx key, not position
        title_placeholder = slide.placeholders[0] # pos=1 Title
        img_placeholder = slide.placeholders[1]  # pos=2 Picture Placeholder
        caption_placeholder = slide.placeholders[2] # pos=3 Text Placeholder

        title_placeholder.text = img_basename
        picture = img_placeholder.insert_picture(img_path)
        pillow_img = Image.open(img_path)
        print(pillow_img.width, pillow_img.height, type(pillow_img.width))
        # picture.width = pillow_img.width
        # picture.height = pillow_img.height
        picture.crop_top = 0.0
        picture.crop_bottom = 0.0
        # picture.crop_left = 0.0
        # picture.crop_right = 0.0
        caption_placeholder.text = f'The image from {img_path}'


    prez.save(f'{dirname}.pptx')

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
        
    # slide = prez.slides.add_slide(prez.slide_layouts[8])
    # for x in slide.placeholders:
    #     print(x.name)
    #
    # Title 1
    # Picture Placeholder 2
    # Text Placeholder 3
    
    # for x in os.listdir(args.dir):
    #     print(os.path.join(args.dir, x))

    sys.exit()


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