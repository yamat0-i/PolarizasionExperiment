"""Utils to display to be returned to the user on the console."""
import os
import string

from pathlib import Path

import termcolor


def get_TEMPLATE_DIR_PATH():
    """Return the path of the template's directory.

    Returns:
        str: The template dir path.
    """
    TEMPLATE_DIR_PATH = None
    # try:
    #     import settings
    #     if settings.TEMPLATE_PATH:
    #         TEMPLATE_DIR_PATH = settings.TEMPLATE_PATH
    # except ImportError:
    #     pass

    if not TEMPLATE_DIR_PATH:
        VIEWS_DIR = Path(os.path.dirname(__file__))
        BASE_DIR = Path(VIEWS_DIR.parent)
        TEMPLATE_DIR_PATH = os.path.join(BASE_DIR, 'templates')

    return TEMPLATE_DIR_PATH


class NoTemplateError(Exception):
    """No Template Error"""


def find_template(temp_file):
    """Find for template file in the given location.

    Returns:
        str: The template file path

    Raises:
        NoTemplateError: If the file does not exists.
    """
    TEMPLATE_DIR_PATH = get_TEMPLATE_DIR_PATH()
    temp_file_path = os.path.join(TEMPLATE_DIR_PATH, temp_file)
    if not os.path.exists(temp_file_path):
        raise NoTemplateError('Could not find {}'.format(temp_file))
    return temp_file_path


def get_template(template_file_path, color=None):
    """Return the path of the template.

    Args:
        template_file_path (str): The template file path
        color: (str): Color formatting for output in terminal
            See in more details: https://pypi.python.org/pypi/termcolor

    Returns:
        string.Template: Return templates with characters in templates.
    """
    template = find_template(template_file_path)
    with open(template, 'r', encoding='utf-8') as template_file:
        contents = template_file.read()
        contents = contents.rstrip(os.linesep)
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents=contents, splitter="=" * 60, sep=os.linesep)
        contents = termcolor.colored(contents, color)
        return string.Template(contents)
