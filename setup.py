from setuptools import find_packages
from setuptools import setup

setup(
    name="revChatGPT",
    version="0.0.34",
    license="GNU General Public License v2.0",
    author="Antonio Cheong",
    author_email="acheong@student.dalat.org",
    description="ChatGPT is a reverse engineering of OpenAI's ChatGPT API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["revChatGPT", "asyncChatGPT"],
    url="https://github.com/acheong08/ChatGPT",
    install_requires=[
        "requests",
        "httpx[http2]",
        "OpenAIAuth>=0.0.5",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "revChatGPT = revChatGPT.__main__:main",
        ]
    },
)
