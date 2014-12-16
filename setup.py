import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


# See http://pytest.org/latest/goodpractises.html
class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


exec(open('sfs/_version.py').read())  # "import" __version__

setup(
    name="SoundFieldSynthesis",
    version=__version__,
    packages=['sfs'],
    install_requires=[
        'numpy',
        'scipy',
    ],

    author="SFS Toolbox Developers",
    author_email="sfstoolbox@gmail.com",
    description="Sound Field Synthesis Toolbox",
    long_description=open('README.rst').read(),
    license="MIT",
    keywords="audio SFS WFS Ambisonics".split(),
    url="http://github.com/sfstoolbox",
    platforms='any',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
    ],

    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
