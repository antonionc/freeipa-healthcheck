from ipahealthcheck.system.plugin import SystemPlugin, registry
from ipahealthcheck.core.plugin import duration, Result
from ipahealthcheck.core import constants


@registry
class MyPlugin(SystemPlugin):
    @duration
    def check(self):
        yield Result(self, constants.WARNING, "This is a bougs test", {"key": "value"})
