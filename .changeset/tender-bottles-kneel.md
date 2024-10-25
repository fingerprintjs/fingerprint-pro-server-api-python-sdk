---
'fingerprint-pro-server-api-python-sdk': patch
---

- Move existing and add new error examples to `/schemas/paths/examples/errors`.
- Replace GET /events TooManyRequests examples with a single `get_event_200_too_many_requests_error.json`.
- Update `products.identification.error.message` in `get_event_200_<...>.json` examples.
- Rename GET /visitors example files.
