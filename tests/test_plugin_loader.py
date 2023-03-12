import janisbot4.plugins

from importlib.machinery import FileFinder

from janisbot4.plugin_loader import load_plugin, load_plugins, register_plugins
from tests.dispatcher_stub import DispatcherStub


def test_plugins_path_is_correct():
    import janisbot4.plugins

    assert str.endswith(janisbot4.plugins.__path__[0], "janisbot4/plugins")


def test_all_plugins_can_be_loaded():
    plugins = load_plugins(janisbot4.plugins.__path__[0])
    plugin_names = [plugin.__name__ for plugin in plugins]

    assert len(plugins) > 1
    assert "quote_command" in plugin_names
    assert hasattr(plugins[0], "index")


def test_plugins_can_be_registered():
    plugins = load_plugins(janisbot4.plugins.__path__[0])

    dispatcher = DispatcherStub()
    register_plugins(plugins, dispatcher, None)

    assert dispatcher.called


def test_exception_catched_when_plugin_does_not_exist():
    plugin = load_plugin(FileFinder("nonexisting/folder"), "false_module")
    assert not plugin
