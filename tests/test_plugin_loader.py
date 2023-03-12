from janisbot4.plugin_loader import load_plugin, load_plugins, register_plugins

from tests.dispatcher_stub import DispatcherStub


def test_plugins_path_is_correct():
    import janisbot4.plugins

    assert str.endswith(janisbot4.plugins.__path__[0], "janisbot4/plugins")


def test_a_plugin_can_be_loaded():
    plugin = load_plugin(".quote_command", "janisbot4.plugins")

    assert plugin.__name__ == "janisbot4.plugins.quote_command"
    assert hasattr(plugin, "index")
    assert not isinstance(plugin, str)


def test_a_plugin_can_be_loaded_with_path_names():
    plugin = load_plugin("quote_command", "janisbot4/plugins")

    assert plugin.__name__ == "janisbot4.plugins.quote_command"
    assert hasattr(plugin, "index")
    assert not isinstance(plugin, str)


def test_all_plugins_can_be_loaded():
    plugins = load_plugins("janisbot4/plugins")

    plugin_names = [plugin.__name__ for plugin in plugins]

    assert len(plugins) > 1
    assert "janisbot4.plugins.quote_command" in plugin_names
    assert hasattr(plugins[0], "index")


def test_plugins_can_be_registered():
    plugins = load_plugins("janisbot4/plugins")

    dispatcher = DispatcherStub()
    register_plugins(plugins, dispatcher, None)

    assert dispatcher.called


def test_exception_catched_when_plugin_does_not_exist():
    plugin = load_plugin("false_module", "nonexisting/folder")
    assert not plugin
