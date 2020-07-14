import setuptools

with open('README.md', 'r') as file:
    readme = file.read()

setuptools.setup(
    name="wttrpy", # Replace with your own username
    version="1.0.0",
    author="Denisov Artem",
    author_email="hashadev@yandex.ru",
    description="A little thing on Python that shows you forecast using wttr.in",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/hasha2982/wttr.py/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests>=2,<3']
)