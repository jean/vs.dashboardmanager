from setuptools import setup, find_packages
import os

version = '0.3.1-SVN_UNRELEASED'

setup(name='vs.dashboardmanager',
      version=version,
      description="An extended Dashboard manager based on collective.portletpage",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Andreas Jung',
      author_email='info@zopyx.com',
      url='http://pypi.python.org/pypi/vs.dashboardmanager',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['vs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.portletpage',
          'archetypes.schemaextender',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      paster_plugins=["ZopeSkel"],
      )
