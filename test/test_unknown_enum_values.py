import json
import unittest
from pathlib import Path
from typing import Any

from fingerprint_server_sdk import Event
from fingerprint_server_sdk.models.bot_info import BotInfo
from fingerprint_server_sdk.models.event_device import EventDevice
from fingerprint_server_sdk.models.event_edge import EventEdge
from fingerprint_server_sdk.models.event_source import EventSource
from fingerprint_server_sdk.models.proxy_details import ProxyDetails
from fingerprint_server_sdk.models.sdk import SDK

MOCK_DIR = Path(__file__).resolve().parent / 'mocks'


class TestUnknownEnumValues(unittest.TestCase):
    """Test that unknown/new enum values are accepted without errors."""

    def _load_event_json(self) -> dict[str, Any]:
        mock_file = MOCK_DIR / 'events' / 'get_event_200.json'
        return json.loads(mock_file.read_text(encoding='utf-8'))

    def test_event_with_unknown_proxy_type(self) -> None:
        """Unknown proxy_type value should be accepted and preserved."""
        data = self._load_event_json()
        data['proxy_details']['proxy_type'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event.actual_instance, EventDevice)
        self.assertEqual(event.actual_instance.proxy_details.proxy_type, 'unknown-value')

    def test_event_with_unknown_sdk_platform(self) -> None:
        """Unknown SDK platform value should be accepted and preserved."""
        data = self._load_event_json()
        data['sdk']['platform'] = 'new-platform'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event.actual_instance, EventDevice)
        self.assertEqual(event.actual_instance.sdk.platform, 'new-platform')

    def test_event_with_unknown_bot_result(self) -> None:
        """Unknown bot result value should be accepted and preserved."""
        data = self._load_event_json()
        data['bot'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event.actual_instance, EventDevice)
        self.assertEqual(event.actual_instance.bot, 'unknown-value')

    def test_event_with_unknown_vpn_confidence(self) -> None:
        """Unknown vpn_confidence value should be accepted and preserved."""
        data = self._load_event_json()
        data['vpn'] = True
        data['vpn_confidence'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event.actual_instance, EventDevice)
        self.assertEqual(event.actual_instance.vpn_confidence, 'unknown-value')

    def test_event_with_unknown_proxy_confidence(self) -> None:
        """Unknown proxy_confidence value should be accepted and preserved."""
        data = self._load_event_json()
        data['proxy_confidence'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event.actual_instance, EventDevice)
        self.assertEqual(event.actual_instance.proxy_confidence, 'unknown-value')

    def test_event_with_unknown_tampering_confidence(self) -> None:
        """Unknown tampering_confidence value should be accepted and preserved."""
        data = self._load_event_json()
        data['tampering_confidence'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event.actual_instance, EventDevice)
        self.assertEqual(event.actual_instance.tampering_confidence, 'unknown-value')

    def test_event_with_unknown_rare_device_percentile_bucket(self) -> None:
        """Unknown rare_device_percentile_bucket value should be accepted and preserved."""
        data = self._load_event_json()
        data['rare_device_percentile_bucket'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event.actual_instance, EventDevice)
        self.assertEqual(event.actual_instance.rare_device_percentile_bucket, 'unknown-value')

    def test_event_with_unknown_source(self) -> None:
        """Unknown non-empty source cannot pick an Event oneOf variant."""
        data = self._load_event_json()
        data['source'] = 'unknown-value'

        with self.assertRaisesRegex(ValueError, "unknown Event source"):
            Event.from_json(json.dumps(data))

    def test_event_without_source(self) -> None:
        """Omit source hydrates to EventDevice."""
        data = self._load_event_json()
        data.pop('source', None)

        event = Event.from_json(json.dumps(data))
        self.assertIsInstance(event.actual_instance, EventDevice)
        self.assertEqual(event.actual_instance.source, EventSource.DEVICE)

    def test_proxy_details_with_unknown_proxy_type(self) -> None:
        """ProxyDetails model should accept unknown proxy_type directly."""
        details = ProxyDetails.from_dict({'proxy_type': 'unknown-value', 'last_seen_at': 123})
        self.assertIsInstance(details, ProxyDetails)
        self.assertEqual(details.proxy_type, 'unknown-value')

    def test_sdk_with_unknown_platform(self) -> None:
        """SDK model should accept unknown platform directly."""
        sdk = SDK.from_dict({'platform': 'unknown-value', 'version': '1.0.0'})
        self.assertIsInstance(sdk, SDK)
        self.assertEqual(sdk.platform, 'unknown-value')

    def test_bot_info_with_unknown_identity_and_confidence(self) -> None:
        """BotInfo model should accept unknown identity and confidence values."""
        info = BotInfo.from_dict(
            {
                'category': 'crawler',
                'provider': 'TestBot',
                'name': 'test',
                'identity': 'unknown-value',
                'confidence': 'unknown-value',
            }
        )
        self.assertIsInstance(info, BotInfo)
        self.assertEqual(info.identity, 'unknown-value')
        self.assertEqual(info.confidence, 'unknown-value')

    def test_event_with_multiple_unknown_enum_values(self) -> None:
        """Event should deserialize when multiple enum fields have unknown values."""
        data = self._load_event_json()
        data['proxy_details']['proxy_type'] = 'unknown-value'
        data['sdk']['platform'] = 'unknown-value'
        data['bot'] = 'unknown-value'
        data['vpn'] = True
        data['vpn_confidence'] = 'unknown-value'
        data['proxy_confidence'] = 'unknown-value'
        data['tampering_confidence'] = 'unknown-value'
        data['rare_device_percentile_bucket'] = 'unknown-value'

        event = Event.from_json(json.dumps(data))
        actual = event.actual_instance
        self.assertIsInstance(actual, EventDevice)
        self.assertEqual(actual.proxy_details.proxy_type, 'unknown-value')
        self.assertEqual(actual.sdk.platform, 'unknown-value')
        self.assertEqual(actual.bot, 'unknown-value')
        self.assertEqual(actual.vpn_confidence, 'unknown-value')
        self.assertEqual(actual.proxy_confidence, 'unknown-value')
        self.assertEqual(actual.tampering_confidence, 'unknown-value')
        self.assertEqual(actual.rare_device_percentile_bucket, 'unknown-value')

    def test_known_enum_values_still_work(self) -> None:
        """Known enum values should continue to work as before."""
        data = self._load_event_json()

        event = Event.from_json(json.dumps(data))
        actual = event.actual_instance
        self.assertIsInstance(actual, EventDevice)
        self.assertEqual(actual.proxy_details.proxy_type, 'residential')
        self.assertEqual(actual.sdk.platform, 'js')
        self.assertEqual(actual.source, EventSource.DEVICE)

    def test_event_with_edge_source(self) -> None:
        """The edge source value should be deserialized into the enum member."""
        data = self._load_event_json()
        edge_payload = {
            'event_id': data['event_id'],
            'timestamp': data['timestamp'],
            'ip_info': data['ip_info'],
            'source': 'edge',
        }

        event = Event.from_json(json.dumps(edge_payload))
        self.assertIsInstance(event.actual_instance, EventEdge)
        self.assertEqual(event.actual_instance.source, EventSource.EDGE)


if __name__ == '__main__':
    unittest.main()
