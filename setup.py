#!/usr/bin/env python

import os

from setuptools import setup

ENTRY_POINTS = {
    'orange.widgets.tutorials': (
        'recommendtutorials = orangecontrib.recommend.recommendtutorials',
    ),
    'orange.widgets': (
        'Recommendation Systems = orangecontrib.recommend.widgets',
    ),
}

if __name__ == '__main__':
    setup(
        name="Orange3 Recommendation Systems Add-on",
        packages=['orangecontrib',
                  'orangecontrib.recommend',
                  'orangecontrib.recommend.recommendtutorials',
                  'orangecontrib.recommend.widgets'],
        package_data={
          'orangecontrib.recommend': ['recommendtutorials/*.ows'],
          'orangecontrib.recommend.widgets': ['icons/*'],
        },
        install_requires=['Orange'],
        entry_points=ENTRY_POINTS,
        namespace_packages=['orangecontrib'],
        include_package_data=True,
        zip_safe=False,
    )
