from setuptools import setup

setup(
    name='qr',
    packages=['qr'],
    include_package_data=True,
    install_requires=[
        "flask", "Image", "qrcode"
    ],
    version="0.0.3"
)  
