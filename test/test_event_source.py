import json
import unittest
from pathlib import Path
from typing import Any

from fingerprint_server_sdk import Event
from fingerprint_server_sdk.models.event_source import EventSource

MOCK_DIR = Path(__file__).resolve().parent / 'mocks' / 'events'


def _load(name: str) -> dict[str, Any]:
    return json.loads((MOCK_DIR / name).read_text(encoding='utf-8'))


class TestEventSource(unittest.TestCase):
    """Event stays one model whether or not `source` is present (flat v4 schema)."""

    def test_legacy_event_without_source(self) -> None:
        data = _load('get_event_200.json')
        data.pop('source', None)

        event = Event.from_dict(data)

        self.assertIsNotNone(event)
        assert event is not None
        self.assertIsNone(event.source)
        self.assertEqual(event.event_id, data['event_id'])
        self.assertEqual(event.identification.visitor_id, data['identification']['visitor_id'])
        self.assertNotIn('source', event.to_dict())

    def test_edge_event_without_identification(self) -> None:
        data = _load('get_event_with_edge_200.json')
        self.assertEqual(data['source'], 'edge')
        self.assertNotIn('identification', data)

        event = Event.from_json(json.dumps(data))

        self.assertIsNotNone(event)
        assert event is not None
        self.assertEqual(event.source, EventSource.EDGE)
        self.assertIsNone(event.identification)
        self.assertEqual(event.bot_info.name, 'ChatGPT Agent')
        self.assertEqual(event.to_dict()['source'], 'edge')

    def test_device_event_with_source(self) -> None:
        data = _load('get_event_200.json')
        data['source'] = 'device'

        event = Event.from_dict(data)

        assert event is not None
        self.assertEqual(event.source, EventSource.DEVICE)
        self.assertIsNotNone(event.identification)
