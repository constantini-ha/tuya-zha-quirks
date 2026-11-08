"""A single-instance flow: there is nothing to configure, only to install."""

from __future__ import annotations

from homeassistant.config_entries import ConfigFlow

from .const import DOMAIN


class TuyaZhaQuirksFlow(ConfigFlow, domain=DOMAIN):
    """Create the one entry that loads the quirks."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()
        return self.async_create_entry(title="Tuya ZHA Quirks", data={})
