from ipahealthcheck.core.plugin import Plugin, Result
from ipahealthcheck.core import constants
from ipahealthcheck.mymodule.plugin import registry


@registry
class MyPlugin(Plugin):
    @duration
    def check(self):
        yield Result(self, constants.WARNING)
