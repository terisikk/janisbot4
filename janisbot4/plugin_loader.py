import importlib.util
import logging
import pkgutil

import janisbot4.bot


def register_plugins(plugins, dispatcher, idfilter):
    registered_plugins = []

    for plugin in plugins:
        commands = plugin.COMMANDS if hasattr(plugin, "COMMANDS") else None
        regexp = plugin.REGEXP if hasattr(plugin, "REGEXP") else None
        content_types = plugin.CONTENT_TYPES if hasattr(plugin, "CONTENT_TYPES") else None

        dispatcher.register_message_handler(
            plugin.index, idfilter, commands=commands, regexp=regexp, content_types=content_types
        )

        registered_plugins.append(plugin.__name__)

    logging.getLogger(janisbot4.bot.LOGGER_NAME).info("Registered plugins: " + str(registered_plugins))


def load_plugins(module):
    return [load_plugin(finder, name) for finder, name, _ in pkgutil.iter_modules([module])]


def load_plugin(finder, name):
    try:
        spec = finder.find_spec(name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        logging.getLogger(janisbot4.bot.LOGGER_NAME).debug(e)
        logging.getLogger(janisbot4.bot.LOGGER_NAME).error(f"Could not load plugin {name}")

    return None
