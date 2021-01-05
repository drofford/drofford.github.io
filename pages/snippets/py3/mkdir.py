import errno
import logging
import os


def mkdir(path):
    try:
        os.makedirs(path)
        logging.debug("Created directory: {}".format(path))
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

