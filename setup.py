# -*- encoding: utf-8 -*-
# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

import io
import re

from setuptools import find_packages, setup

dev_requirements = [
    "anyio==3.6.1",
    "asgiref==3.5.2",
    "black==22.6.0",
    "certifi==2022.6.15",
    "charset-normalizer==2.1.0",
    "click==8.1.3",
    "dnspython==2.2.1",
    "email-validator==1.2.1",
    "fastapi==0.79.0",
    "greenlet==1.1.2",
    "h11==0.13.0",
    "httptools==0.4.0",
    "idna==3.3",
    "itsdangerous==2.1.2",
    "Jinja2==3.1.2",
    "MarkupSafe==2.1.1",
    "mypy-extensions==0.4.3",
    "orjson==3.7.11",
    "pathspec==0.9.0",
    "platformdirs==2.5.2",
    "pydantic==1.9.1",
    "PyMySQL==1.0.2",
    "python-dotenv==0.20.0",
    "python-multipart==0.0.5",
    "PyYAML==6.0",
    "requests==2.28.1",
    "six==1.16.0",
    "sniffio==1.2.0",
    "SQLAlchemy==1.4.40",
    "starlette==0.19.1",
    "tomli==2.0.1",
    "typing_extensions==4.3.0",
    "ujson==5.4.0",
    "urllib3==1.26.11",
    "uvicorn==0.17.6",
    "uvloop==0.16.0",
    "watchgod==0.8.2",
    "websockets==10.3",
]
unit_test_requirements = [
    "anyio==3.6.1",
    "asgiref==3.5.2",
    "black==22.6.0",
    "certifi==2022.6.15",
    "charset-normalizer==2.1.0",
    "click==8.1.3",
    "dnspython==2.2.1",
    "email-validator==1.2.1",
    "fastapi==0.79.0",
    "greenlet==1.1.2",
    "h11==0.13.0",
    "httptools==0.4.0",
    "idna==3.3",
    "itsdangerous==2.1.2",
    "Jinja2==3.1.2",
    "MarkupSafe==2.1.1",
    "mypy-extensions==0.4.3",
    "orjson==3.7.11",
    "pathspec==0.9.0",
    "platformdirs==2.5.2",
    "pydantic==1.9.1",
    "PyMySQL==1.0.2",
    "python-dotenv==0.20.0",
    "python-multipart==0.0.5",
    "PyYAML==6.0",
    "requests==2.28.1",
    "six==1.16.0",
    "sniffio==1.2.0",
    "SQLAlchemy==1.4.40",
    "starlette==0.19.1",
    "tomli==2.0.1",
    "typing_extensions==4.3.0",
    "ujson==5.4.0",
    "urllib3==1.26.11",
    "uvicorn==0.17.6",
    "uvloop==0.16.0",
    "watchgod==0.8.2",
    "websockets==10.3",
]
integration_test_requirements = [
    "anyio==3.6.1",
    "asgiref==3.5.2",
    "black==22.6.0",
    "certifi==2022.6.15",
    "charset-normalizer==2.1.0",
    "click==8.1.3",
    "dnspython==2.2.1",
    "email-validator==1.2.1",
    "fastapi==0.79.0",
    "greenlet==1.1.2",
    "h11==0.13.0",
    "httptools==0.4.0",
    "idna==3.3",
    "itsdangerous==2.1.2",
    "Jinja2==3.1.2",
    "MarkupSafe==2.1.1",
    "mypy-extensions==0.4.3",
    "orjson==3.7.11",
    "pathspec==0.9.0",
    "platformdirs==2.5.2",
    "pydantic==1.9.1",
    "PyMySQL==1.0.2",
    "python-dotenv==0.20.0",
    "python-multipart==0.0.5",
    "PyYAML==6.0",
    "requests==2.28.1",
    "six==1.16.0",
    "sniffio==1.2.0",
    "SQLAlchemy==1.4.40",
    "starlette==0.19.1",
    "tomli==2.0.1",
    "typing_extensions==4.3.0",
    "ujson==5.4.0",
    "urllib3==1.26.11",
    "uvicorn==0.17.6",
    "uvloop==0.16.0",
    "watchgod==0.8.2",
    "websockets==10.3",
]
run_requirements = [
    "anyio==3.6.1",
    "asgiref==3.5.2",
    "black==22.6.0",
    "certifi==2022.6.15",
    "charset-normalizer==2.1.0",
    "click==8.1.3",
    "cryptography",
    "dnspython==2.2.1",
    "email-validator==1.2.1",
    "fastapi==0.79.0",
    "greenlet==1.1.2",
    "h11==0.13.0",
    "httptools==0.4.0",
    "idna==3.3",
    "itsdangerous==2.1.2",
    "Jinja2==3.1.2",
    "MarkupSafe==2.1.1",
    "mypy-extensions==0.4.3",
    "orjson==3.7.11",
    "pathspec==0.9.0",
    "platformdirs==2.5.2",
    "pydantic==1.9.1",
    "PyMySQL==1.0.2",
    "python-dotenv==0.20.0",
    "python-multipart==0.0.5",
    "PyYAML==6.0",
    "requests==2.28.1",
    "six==1.16.0",
    "sniffio==1.2.0",
    "SQLAlchemy==1.4.40",
    "starlette==0.19.1",
    "tomli==2.0.1",
    "typing_extensions==4.3.0",
    "ujson==5.4.0",
    "urllib3==1.26.11",
    "uvicorn==0.17.6",
    "watchgod==0.8.2",
    "websockets==10.3",
]

with io.open("./user_image_fastapi/__init__.py", encoding="utf8") as version_f:
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_f.read(), re.M
    )
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with io.open("README.md", encoding="utf8") as readme:
    long_description = readme.read()

setup(
    name="user_image_fastapi",
    version=version,
    author="Caio Dantas",
    author_email="caiodantas@gmail.com",
    packages=find_packages(exclude="tests"),
    include_package_data=True,
    url=("https://github.com/dantascaio/user-image-fastapi"),
    license="MIT",
    description="Stores user images on database",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
        "dev": dev_requirements,
        "unit": unit_test_requirements,
        "integration": integration_test_requirements,
    },
    python_requires="==3.9.*",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.9",
    ],
    keywords=[],
    entry_points={
        "console_scripts": ["user_image_fastapi = user_image_fastapi.main:app"],
    },
)
