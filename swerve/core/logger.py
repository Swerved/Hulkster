# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

import logging
from Hulkster.swerve.core import commandline, paths, swerveos

enabled = commandline.cli_get_value_for_argument("--debug")


def channel(name, level=logging.INFO):
    """To setup as many loggers as you want"""

    if name == "app":
        return
    log_file = paths.logs() + name + ".log"
    handler = logging.FileHandler(log_file)
    style = logging.Formatter('%(asctime)s ''[''%(levelname)s'']'' %(message)s', '%Y%m%d@%H%M%S:')
    handler.setFormatter(style)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def main(name, level=logging.INFO):
    """To setup as many loggers as you want"""

    log_file = paths.logs() + "app.log"
    handler = logging.FileHandler(log_file)
    style = logging.Formatter('%(asctime)s ''[''%(levelname)s'']'' ''{''%(name)s''}'' - %(message)s', '%Y%m%d@%H%M%S:')
    handler.setFormatter(style)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def info(module, message):
    le = enabled
    if not enabled:
        return
    logger = main(module)
    logger.debug(message)
    logger.info(message)
    logger.warning(message)
    logger.error(message)
    logger.critical(message)
    logger = channel(module)
    logger.info(message)
