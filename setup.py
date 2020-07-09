import setuptools



setuptools.setup(
    name="pycreate2", # Replace with your own username
    version="1.0.0",
    author="Zichun",
    author_email="zhuang42@cs.toronto.edu",
    description="pycreate2",
    long_description_content_type="text",
    long_description="This package is forked from MomsFriendlyRobotCompany/pycreate2"
    packages=setuptools.find_packages(),
    url="https://github.com/zhuang42/pycreate2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["importlib_metadata"],
    python_requires='>=3.6',
)
