from setuptools import setup

setup(
    name="swserver",
    version="0.1",
    description="Server for smart watch task deployment",
    long_description="Server for smart watch task deployment",
    author="Ioan-Matei Sarivan",
    author_email="ioanms@mp.aau.dk",
    packages=[
        "swserver"
    ],
    package_dir={
        "swserver":"swserver"
        },
    entry_points={
        "console_scripts": [
            "swserver=swserver.__init__:main"
        ]
    },
    package_data={
        "swserver": ["json/*"
         ]
    },
    include_package_data=True,
    install_requires=[
        "paho-mqtt"
    ],
    zip_safe=False,
    keywords="swserver",
    classifiers=[
        "Development Status :: Experimental",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8"
    ]

)