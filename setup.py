from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Streaming Videos data via networks'
LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

setup(
    name="dut_tea",
    version=VERSION,
    author="Dut",
    author_email="<mduc221199@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    url = "https://github.com/minhduc1999/dut_tea.git",
    project_urls = {
        "Source": "https://github.com/minhduc1999/dut_tea.git",
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)