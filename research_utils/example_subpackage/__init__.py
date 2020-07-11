from . import (
    subsubpackage
)

from .test import (
    hello,
    world
)

__all__ = ['hello']

"""
In this case, importing with `import research_utils`, you can run the `world`
function with `research_utils.example.world` or
`research_utils.example.test.world`

However, you cannot run the world function when importing with
`from research_utils.example import *`. This will only import the `hello`
function but not the `test` submodule or 
"""
