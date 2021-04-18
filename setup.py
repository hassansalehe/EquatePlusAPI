''' Setup file for PyPI'''

from distutils.core import setup

setup(
    name='hisaapi',
    packages=['hisaapi'],
    version='1.0',
    license='MIT',
    description='Unofficial API for accessing current stock prices converted to Euros',
    author='Hassan Salehe Matar',
    author_email='hassansalehe@gmail.com',
    url='https://github.com/hassansalehe/hisaapi',
    download_url='https://github.com/hassansalehe/hisaapi/archive/v1.0.tar.gz',
    keywords=['Hisa', 'API', 'Stock', "Share"],
    install_requires=[
        'investpy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Stocks",
        "Topic :: Office/Business :: Financial :: Shares",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
