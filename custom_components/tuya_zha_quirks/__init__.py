"""Ship Zigbee quirks for Tuya devices upstream does not cover yet."""

from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .quirks import register

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Register the quirks. Importing them is what registers them with zigpy."""
    registered = await hass.async_add_executor_job(register)
    _LOGGER.debug("Registered %s Zigbee quirks", registered)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """A quirk cannot be taken out of zigpy's registry; a restart does that."""
    return True
