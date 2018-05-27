import ast
import re
from setuptools import setup
import sys

assert sys.version_info >= (3, 6, 0), "black requires Python 3.6+"
from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent


def get_long_description() -> str:
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()


def get_version() -> str:
    black_py = CURRENT_DIR / "black.py"
    _version_re = re.compile(r"__version__\s+=\s+(?P<version>.*)")
    with open(black_py, "r", encoding="utf8") as f:
        match = _version_re.search(f.read())
        version = match.group("version") if match is not None else '"unknown"'
    return str(ast.literal_eval(version))


setup(
    name="black",
    version=get_version(),
    description="Python interface for National Oceanic and Atmospheric Administration's  \
         (NOAA) U.S. Temperature and Precipitation Seasonal (long-term) Weather Outlooks (forecasts)",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="noaa long-term weather forecast outlook seasonal precipitation temperature shapefile geo",
    author="Daniel Sequeria",
    author_email="",
    url="https://github.com/dapbs/horai'",
    python_requires=">=3.6",
    license="MIT",
    py_modules=["horai"],
    packages=["horai"]
)
