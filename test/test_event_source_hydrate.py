import json
import unittest
from pathlib import Path
from typing import Any

from fingerprint_server_sdk import Event
from fingerprint_server_sdk.models.event_device import EventDevice
from fingerprint_server_sdk.models.event_edge import EventEdge
from fingerprint_server_sdk.models.event_source import EventSource

MOCK_DIR = Path(__file__).resolve().parent / 'mocks'


class TestEventSourceHydrate(unittest.TestCase):
    """Omit source hydrates to EventDevice; edge stays EventEdge."""

    def _load_event_json(self) -> dict[str, Any]:
        mock_file = MOCK_DIR / 'events' / 'get_event_200.json'
        return json.loads(mock_file.read_text(encoding='utf-8'))

    def test_omit_source_deserializes_event_device(self) -> None:
        data = self._load_event_json()
        data.pop('source', None)

        event = Event.from_json(json.dumps(data))

        self.assertIsInstance(event.actual_instance, EventDevice)
        self.assertEqual(event.actual_instance.source, EventSource.DEVICE)

    def test_edge_source_stays_event_edge(self) -> None:
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
        self.assertNotEqual(event.actual_instance.source, EventSource.DEVICE)

    def test_empty_source_deserializes_event_device(self) -> None:
        data = self._load_event_json()
        data['source'] = ''

        event = Event.from_json(json.dumps(data))

        self.assertIsInstance(event.actual_instance, EventDevice)
        self.assertEqual(event.actual_instance.source, EventSource.DEVICE)

    def test_unknown_source_fails(self) -> None:
        data = self._load_event_json()
        data['source'] = 'webhook'

        with self.assertRaisesRegex(ValueError, 'unknown Event source'):
            Event.from_json(json.dumps(data))


if __name__ == '__main__':
    unittest.main()
