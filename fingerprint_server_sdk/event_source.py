"""Hydrate a missing Event source before oneOf discriminator lookup."""

from __future__ import annotations

import json
from typing import Any


def hydrate_event_discriminator(class_name: str, json_str: str, property_name: str) -> tuple[str, Any]:
    payload = json.loads(json_str)
    data_type = payload.get(property_name)
    if class_name != "Event":
        return json_str, data_type
    if data_type is None or data_type == "":
        payload["source"] = "device"
        return json.dumps(payload), "device"
    if data_type not in ("device", "edge"):
        raise ValueError(f"unknown Event source: {data_type!r}")
    return json_str, data_type
