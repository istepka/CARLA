# flake8: noqa
# isort:skip
import logging.config
import os
import pathlib

import yaml

lib_path = pathlib.Path(__file__).parent.resolve()
with open(os.path.join(lib_path, "logging.yaml"), "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

log = logging.getLogger(__name__)


import sys


path_root = pathlib.Path(__file__).parent.parent.resolve()
if path_root not in sys.path:
    sys.path.append(str(path_root))
    print('Appending path to carla module', str(path_root))

from ._version import __version__
from .data import Data, DataCatalog
from .evaluation import Benchmark
from .models import MLModel, MLModelCatalog
from .recourse_methods import RecourseMethod


def get_logger(logger: str):
    return logging.getLogger(logger)
