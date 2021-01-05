import daiquiri
import logging as __LOG__
import os

level = os.getenv("LEVEL", None)
if not level:
    debug = os.getenv("DEBUG", None)
    if debug and debug.upper() == "Y":
        level = "DEBUG"
if   level == "DEBUG"  : log_level = __LOG__.DEBUG
elif level == "INFO"   : log_level = __LOG__.INFO
elif level == "WARNING": log_level = __LOG__.WARNING
else                   : log_level = __LOG__.INFO

daiquiri.setup(log_level)
logger = daiquiri.getLogger("program-name")
