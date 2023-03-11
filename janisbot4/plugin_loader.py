import pkgutil
import importlib


def register_plugins(plugins, dispatcher, idfilter):
    for plugin in plugins:
        commands = plugin.COMMANDS if hasattr(plugin, "COMMANDS") else None
        regexp = plugin.REGEXP if hasattr(plugin, "REGEXP") else None
        content_types = plugin.CONTENT_TYPES if hasattr(plugin, "CONTENT_TYPES") else None

        dispatcher.register_message_handler(
            plugin.index, idfilter, commands=commands, regexp=regexp, content_types=content_types
        )


def load_plugins(module):
    return [load_plugin(name, module) for _, name, _ in pkgutil.iter_modules([module])]


def load_plugin(source, path):
    try:
        return importlib.import_module(source_to_module(source), path_to_package(path))
    except Exception as e:
        print(e)
        print(f"Could not load plugin {source}")

    return None


def source_to_module(source):
    if not source.startswith("."):
        return "." + source

    return source


def path_to_package(path):
    return path.replace("/", ".")
