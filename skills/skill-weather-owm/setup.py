from setuptools import setup, find_packages

setup(
    name="skill-weather-owm",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    include_package_data=True,
    package_data={"": ["locale/en-us/*.intent"]},
    entry_points={
        "ovos.plugin.skill": [
            "skill-weather-owm=__init__:WeatherSkill"
        ]
    }
)
