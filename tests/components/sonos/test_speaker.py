"""Tests for common SonosSpeaker behavior."""
from unittest.mock import patch

import pytest

from homeassistant.components.sonos.const import DATA_SONOS, SCAN_INTERVAL
from homeassistant.core import HomeAssistant
from homeassistant.util import dt as dt_util

from tests.common import async_fire_time_changed


async def test_fallback_to_polling(
    hass: HomeAssistant, async_autosetup_sonos, soco, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that polling fallback works."""
    speaker = list(hass.data[DATA_SONOS].discovered.values())[0]
    assert speaker.soco is soco
    assert speaker._subscriptions
    assert not speaker.subscriptions_failed

    caplog.clear()

    # Ensure subscriptions are cancelled and polling methods are called when subscriptions time out
    with patch("homeassistant.components.sonos.media.SonosMedia.poll_media"), patch(
        "homeassistant.components.sonos.speaker.SonosSpeaker.subscription_address"
    ):
        async_fire_time_changed(hass, dt_util.utcnow() + SCAN_INTERVAL)
        await hass.async_block_till_done()

    assert not speaker._subscriptions
    assert speaker.subscriptions_failed
    assert "Activity on Zone A from SonosSpeaker.update_volume" in caplog.text


async def test_subscription_creation_fails(
    hass: HomeAssistant, async_setup_sonos
) -> None:
    """Test that subscription creation failures are handled."""
    with patch(
        "homeassistant.components.sonos.speaker.SonosSpeaker._subscribe",
        side_effect=ConnectionError("Took too long"),
    ):
        await async_setup_sonos()

    speaker = list(hass.data[DATA_SONOS].discovered.values())[0]
    assert not speaker._subscriptions

    with patch.object(speaker, "_resub_cooldown_expires_at", None):
        speaker.speaker_activity("discovery")
        await hass.async_block_till_done()

    assert speaker._subscriptions


async def test_create_update_groups_coro(
    hass: HomeAssistant, async_autosetup_sonos, soco, caplog: pytest.LogCaptureFixture
) -> None:
    """Test that create_update_groups_coro."""
    speaker = list(hass.data[DATA_SONOS].discovered.values())[0]
    assert speaker.soco is soco

    with patch.object(speaker, "async_write_entity_states") as mock_write_entity_states:
        coro = speaker.create_update_groups_coro(None)
        await coro

        assert not mock_write_entity_states.called
        assert not speaker.coordinator
        assert speaker.sonos_group == [speaker]

        for member in speaker.sonos_group[1:]:
            assert not member.coordinator
            assert member.sonos_group == [speaker]

    assert "Regrouped" not in caplog.text
