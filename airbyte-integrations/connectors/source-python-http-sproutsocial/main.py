#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_python_http_sproutsocial import SourcePythonHttpSproutsocial

if __name__ == "__main__":
    source = SourcePythonHttpSproutsocial()
    launch(source, sys.argv[1:])
