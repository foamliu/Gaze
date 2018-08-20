import setuptools

setuptools.setup(
    name="gaze",
    version="0.0.3",
    author="Peisheng Wang",
    author_email="t-peiwa@microsoft.com",
    description="Gaze integrates the computing power of private clouds with data from IoT devices such as cameras,"
                " providing scalable video analytics capacity on the Edge",
    url="https://github.com/foamliu/Gaze",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)