# -*- coding: utf-8 -*-
# Copyright © NeonJonn 2021-present
#
# This file is part of Neon.
#
# Neon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Neon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Neon. If not, see <https://www.gnu.org/licenses/>.

import os
import re
import types

from setuptools import find_namespace_packages, setup

name = "neon"


def parse_meta():
    with open(os.path.join(name, "__init__.py")) as fp:
        code = fp.read()

    token_pattern = re.compile(
        r"^__(?P<key>\w+)?__\s*=\s*(?P<quote>(?:'{3}|\"{3}|'|\"))(?P<value>.*?)(?P=quote)",
        re.M,
    )

    groups = {}

    for match in token_pattern.finditer(code):
        group = match.groupdict()
        groups[group["key"]] = group["value"]

    return types.SimpleNamespace(**groups)


def long_description():
    with open("README.md") as fp:
        return fp.read()


def parse_requirements_file(path):
    with open(path) as fp:
        dependencies = (d.strip() for d in fp.read().split("\n") if d.strip())
        return [d for d in dependencies if not d.startswith("#")]


meta = parse_meta()

setup(
    name="lightbulb-neon",
    version=meta.version,
    description="An add-on for Lightbulb making it easier to handle component interactions",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    author="neonjonn",
    author_email="",
    url="https://github.com/neonjonn/lightbulb-neon",
    packages=find_namespace_packages(include=[name + "*"]),
    license="GPL-3.0",
    install_requires=parse_requirements_file("requirements.txt"),
    python_requires=">=3.8.0,<3.11",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
