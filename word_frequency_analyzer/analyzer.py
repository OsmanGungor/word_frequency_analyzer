import logging
from .utils import time_decorator

logger_analyzer = logging.getLogger(__name__)


@time_decorator
def read_file(file_path):
    """
    Reads a file content.

    Args:
        file_path (str): Path to read file from.

    Returns:
        str: Content of a file.
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError as e:
        error_msg = f"The file {file_path} does not exist."
        logger_analyzer.error(f"LOG: {error_msg} Exception: {e}", exc_info=True)
        raise
    except IOError as e:
        logger_analyzer.error(f"LOG: Error occurred while trying to read the file {file_path}. Exception: {e}",
                              exc_info=True)
        raise
    except Exception as e:
        logger_analyzer.error(
            f"LOG: An unexpected error occurred while trying to read the file {file_path}. Error: {e}",
            exc_info=True)
        raise
    finally:
        logger_analyzer.info("The 'read_file' function has been executed.")


@time_decorator
def count_frequency(word, text):
    """
    Counts number of times a word is found within a text.

    Args:
        word (str): Word to find within the text.
        text (str): Text to search in.

    Returns:
        int: Number of times a word is found within a text.
    """
    try:
        count_number = text.count(word)
        return count_number
    except TypeError:
        logger_analyzer.error('Must be str, cannot be None', exc_info=True)
        raise
    except Exception as e:
        logger_analyzer.error(f"An unexpected error occurred: {e}", exc_info=True)
    finally:
        logger_analyzer.info("The 'count_frequency' function has been executed.")


@time_decorator
def create_output_file(file_path, text):
    """
    Creates a file with a given content. If file exists it will be rewritten.

    Args:
        file_path (str): Path where the file should be stored.
        text (str): Content of the file.
    """
    try:
        with open(file_path, 'w') as f:
            f.write(text)
    except IOError:
        logger_analyzer.error(f"Error occurred while trying to write to the file {file_path}.", exc_info=True)
    except Exception as e:
        logger_analyzer.error(f"An unexpected error occurred: {e}", exc_info=True)
        raise
    finally:
        logger_analyzer.info("The 'create_file' function has been executed.")


@time_decorator
def process_file(word, input_file, output_file):
    content = read_file(input_file)
    frequency_number = count_frequency(word, content)
    output_text = f'The word {word} appeared {frequency_number} times in {input_file}'
    create_output_file(output_file, output_text)
