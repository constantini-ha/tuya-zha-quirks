"""Every module here registers itself with zigpy when imported."""

import importlib
import logging
import pkgutil

_LOGGER = logging.getLogger(__name__)

_done = False


def register() -> int:
    """Import each quirk once, returning how many registered."""
    global _done
    if _done:
        return 0
    _done = True

    try:
        import zhaquirks  # noqa: F401
    except ImportError:
        _LOGGER.warning("ZHA is not installed, so no quirk was registered")
        return 0

    count = 0
    for module in pkgutil.iter_modules(__path__):
        if module.name.startswith("_"):
            continue
        try:
            importlib.import_module(f"{__name__}.{module.name}")
        except Exception as err:  # one bad quirk must not take the rest down
            _LOGGER.warning("Quirk %s was not registered: %s", module.name, err)
        else:
            count += 1
            _LOGGER.info("Registered the %s quirk", module.name)
    return count
