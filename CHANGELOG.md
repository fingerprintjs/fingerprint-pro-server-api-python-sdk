# Changelog

<!--next-version-placeholder-->

## v2.4.0 (2023-07-31)

### Feature

* Add raw device attributes support ([`6b81649`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/6b81649005cdd336173dd33ae41143fc8aa4f5ef))
* Add support for smart signals ([`28926b8`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/28926b87954f31f0bbaa917dc7b956217c61e5a6))

### Documentation

* Improve model documentation, add special fix for `RawDeviceAttributesResult` documentation ([`36ddc0d`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/36ddc0df68dc394640e01ad0fd060d353ef7eb63))
* **README:** Use `pagination_key` in README example instead of deprecated `before` ([`5dd6e55`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/5dd6e5528bbe710f54e3bd9c5660d15fe5aa548c))

## v2.3.0 (2023-06-06)
### Feature
* Update schema with correct `IpLocation` format and doc updates ([`d501cfa`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/d501cfa13b585e881c0645eed6dd89c09ea46a78))

## v2.2.0 (2023-05-16)
### Feature
* Introduce additional signals ([`4e5fc79`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/4e5fc79eebc0d67bd5b451636e60c461f08dd7ee))

## v2.1.0 (2023-02-03)
### Feature
* Improve error reporting by adding `KnownApiException` class ([`f60625a`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/f60625a209525a3591b4e2f1f52c38550f6a303e))

### Fix
* Set `retry_after` to `1` in case of missed header ([`1d5b5b9`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/1d5b5b9ba91b0cf265f31130bc246275abf97f20))
* Add `retry_after` value from header to `ManyRequestsResponse` error ([`25dc803`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/25dc8035626b9dff388cd94b74ecc8fc4f4782a3))
* Update schema ([`c9be3d3`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/c9be3d36266e065fa606591fef6c6357f14e8556))

### Documentation
* Extend example with new error reporting ([`d78d12b`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/d78d12bbe44116c75d1deb802cc386fd12b993eb))

## v2.0.0 (2023-01-16)
### Feature
* Update schema ([`065f23c`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/065f23cd8afc3f87a9186927942b86a75981c6f8))

### Breaking
* `StSeenAt` type renamed to `SeenAt` ([`065f23c`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/065f23cd8afc3f87a9186927942b86a75981c6f8))

### Documentation
* Add coverage badge ([`f8c6236`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/f8c623687b3b41422606b763b81e0f4e98a97bc4))
* Add instruction how to run tests ([`5eb8115`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/5eb81158eba44968d40725d66da2dfa24d54c9cd))

## v1.3.0 (2022-10-25)
### Feature
* Update schema to support url field for botd result ([`24bfdf0`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/24bfdf0339bf9965b7e5a31e0871304c87562c7e))

### Fix
* Restore some parts of api_doc.mustache template from swagger-codegen repository ([`5b6b531`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/5b6b531244cebbf00b8f1d8bc580301ed5b7ac01))

## v1.2.0 (2022-09-14)
### Feature
* Introduce /event/{request_id} endpoint ([`3e587d0`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/3e587d08b6b02532667c382daf27f05a80a98a4b))

### Documentation
* **README:** Add examples to readme ([`13256fd`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/13256fd34a1275c9c3a9ca8c01cd5beb1fafa668))

## v1.1.0 (2022-08-25)
### Feature
* Support nullable types ([`7ac3b07`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/7ac3b07a9622ddeb9e332a793f02f8112bcd3b7f))

### Fix
* Regenerate schema with nullable types support ([`9c05f3e`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9c05f3e9492c3a1374ef5a950b95420be9600af5))

## v1.0.0 (2022-08-24)
### Feature
* Stable release ([`993a34a`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/993a34af407279b75b98d1b72e439e799c072cae))

### Breaking
* stable release  ([`993a34a`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/993a34af407279b75b98d1b72e439e799c072cae))

## v0.0.4 (2022-08-19)
### Fix
* Add correct links to documentation from PyPI ([`af8264f`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/af8264f6e9cabc7aa75c1e2b5269045884373600))

### Documentation
* Improve setup instruction ([`c95f794`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/c95f79468050b332313f1bfcf803b249624bf493))
* Remove extra imports, use print instead of pprint in example ([`9cccd53`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9cccd53a7fcf05d60cdab484a2aaf43c5a83038d))
* Add keywords ([`93fc3a2`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/93fc3a2c3c993905a6133776e0dca531ff26e683))

## v0.0.3 (2022-08-17)
### Fix
* Sync version in generated code ([`0181453`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/0181453ea61341188c04bcad4bb81d8769bf5664))
* Update release commit message to not trigger new release ([`9d079ca`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/9d079ca4aa0c04b7e77c7f76fe8c3fee673bf9e9))

## v0.0.2 (2022-08-16)
### Documentation
* Add pypi badge ([`af44bbb`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/af44bbb457f6d56e640b944c28ecd9d14e559f53))
* Add ci badges ([`ac20d9e`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/ac20d9ea07b2d1b8cc851a0c25c3318cd81c87e2))

## v0.0.2-beta.9 (2022-08-15)
### Documentation
* Add author ([`ad95a50`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/ad95a5038641a9dc94237894d78bf03cd3ac69e4))
* Update description ([`4b28f0f`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/4b28f0fac38700e27d41baee25e857de975af110))

## v0.0.2-beta.8 (2022-08-12)
### Documentation
* Use full url to logo ([`5cd84fa`](https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/commit/5cd84fabbf1a230a41f0e93039e2739227f79597))

## v0.0.2-beta.7 (2022-08-12)


## v0.0.2-beta.6 (2022-08-12)


## v0.0.2-beta.5 (2022-08-12)


## v0.0.2-beta.4 (2022-08-12)

