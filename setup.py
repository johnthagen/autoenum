import setuptools

install_requires = []
try:
    import enum  # noqa
except ImportError:
    install_requires.append('enum34')


setuptools.setup(
    name='autoenum',
    version='1.0.0',

    description='Auto numbered enum class',
    long_description=open('README.rst').read(),
    keywords='enum enumerations autonumber',

    author='John Hagen',
    author_email='johnthagen@gmail.com',
    url='https://github.com/johnthagen/autoenum',
    license='MIT',
    install_requires=install_requires,

    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
