import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='',
    author='',
    author_email='',
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    project_urls = {
    },
    license='MIT',
    packages=[],
    install_requires=[
      'requests',
      'uuid',
],
)