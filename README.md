# slides-generator
A tool to convert various inputs into a .pptx/slides deck template for further human refinement (requested by Evelyn Schmidt, WashU).

## User Manual - generate_slides.py v1.0

`generate_slides.py` is a command-line tool to convert a directory of images (`.jpg`, `.png`, `.jpeg`) into a `.pptx` format with each image file getting its own dedicated slide. This tool is ***NOT*** meant to serve as a replacement for human creativity and does ***NOT*** use AI tools to achieve its goal. This tool is to automate the creation of a presentation which requires a massive amount of images; the final product is a rough template for a presentation and still requires human intervention and refinement to produce a finished presentation.

### Set up

It is assumed that you have a basic understanding of command-line tools and have the [Python language](https://www.python.org/) and [PIP package manager](https://pypi.org/project/pip/) installed locally. If you do not, please follow the requisite guides for installation.

1. Navigate to the root of this repository.
2. Run the `./setup.sh` script at the repository root. Alternatively, run the following commands on your preferred terminal (Development and testing was conducted on a WSL Ubuntu 22.04.3 LTS distro, please remember to make appropriate changes):

    ```
    python3 -m venv .venv # creates virtual python env
    source .venv/bin/activate # activates venv
    pip install -r requirements.txt # installs packages
    ```
    To activate the python virtual environment, run the following command:
    ```
    source .venv/bin/activate
    ```
    To deactivate, run this command:
    ```
    deactivate
    ```
    For more information, please visit the [official documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) for virtual Python environments (*cough cough* Evelyn @evelyn-schmidt).

### Usage

1. Activate the virtual environment.
2. Run the following command to generate your `.pptx` slides deck:
    ```
    py generate_slides.py [relative path to image directory]
    ```
    For more information, enter the following command to open the help prompt:
    ```
    py generate_slides.py --help
    ```