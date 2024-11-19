from setuptools import setup, find_packages

setup(
    name="hello-world-emoji",
    version="0.1.0",
    description="A simple script that prints a colorful 'Hello, World!' with emojis",
    author="Tadas",
    author_email="admin@lanlab.xyz",
    packages=find_packages(),
    py_modules=["hello"],
    install_requires=[
        "termcolor",
        "emoji",
    ],
    entry_points={
        "console_scripts": [
            "hello-world-emoji=hello:hello",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
