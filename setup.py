from setuptools import setup, find_packages


def read_requirements(file):
    with open(file, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


EXTRAS = {
    "audio": ["openai-whisper>=20231117"],
    "semantic": ["sentence-transformers>=2.2.2"],
    "llama-index": ["llama-index>=0.10.50,<0.11"],
    "gpu": [
        "torch>=2.5,<2.6",
        "torchvision>=0.20,<0.21",
        "torchaudio>=2.5,<2.6",
        "sentence-transformers>=2.2.2",
        "openai-whisper>=20231117",
    ],
}
EXTRAS["all"] = sorted({pkg for deps in EXTRAS.values() for pkg in deps})


setup(
    name="thepipe_api",
    version="1.7.1",
    author="Emmett McFarlane",
    author_email="emmett@thepi.pe",
    description="Get clean data from tricky documents, powered by VLMs.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/emcf/thepipe",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=read_requirements("requirements.txt"),
    extras_require=EXTRAS,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "thepipe=thepipe.__init__:main",
        ],
    },
)
