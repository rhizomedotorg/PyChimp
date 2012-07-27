from distutils.core import setup

setup(
    name='pychimp',
    version='0.1',
    description='A reusable Django app for queuing the sending of email',
    author='Hunter Ford',
    author_email='hunterford@gmail.com',
    url='http://code.google.com/p/pychimp/',
    packages=[
        'pychimp',
    ],
    package_dir={'pychimp': 'pychimp'},
)
