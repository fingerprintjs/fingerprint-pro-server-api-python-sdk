# coding: utf-8

"""
    Fingerprint Server API

    Fingerprint Server API allows you to search, update, and delete identification events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pathlib
import re

from setuptools import setup, find_packages  # noqa: H301

NAME = "fingerprint-pro-server-api-sdk"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2023.7.22",
    "python-dateutil>=2.5.3",
    "urllib3>=1.23",
    "cryptography"
]


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')
long_description = re.sub("<source[^>]*>\n", '', long_description.replace("<picture>\n", "").replace("</picture>\n", ""))
long_description = re.sub(r"(?P<prefix>\[[^]]*]\()(?P<postfix>docs/[^)]*\))", '\g<prefix>https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/blob/main/\g<postfix>', long_description)

setup(
    name=NAME,
    description="Fingerprint Server API allows you to search, update, and delete identification events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device. ",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    license_files=["LICENSE"],
    author="Fingerprint",
    author_email="support@fingerprint.com",
    project_urls={
        "Changelog": "https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/blob/main/CHANGELOG.md",
        "Code": "https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk",
        "Issue Tracker": "https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk/issues",
    },
    keywords=["Swagger", "Fingerprint Server API", "browser", "detection", "fingerprint", "identification",
              "fingerprinting", "browser-fingerprinting", "browser-fingerprint", "fraud-detection", "fraud",
              "audio-fingerprinting", "fingerprintjs", "fingerprintjs-pro", "visitor-identifier"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Security',
    ],
)
