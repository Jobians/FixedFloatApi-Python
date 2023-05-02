from distutils.core import setup

setup(
    name='FixedFloatApi',
    packages=['fixedfloatapi'],
    version='0.1.0',
    license='MIT',
    description='Python wrapper for interacting with the FixedFloat API to exchange cryptocurrencies.',
    author='JobiansTechie',
    author_email='jobianstechie@gmail.com',
    url='https://github.com/Jobians/FixedFloatApi-Python',
    keywords = ['FixedFloat', 'Api', 'FixedFloat Python'],
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
