from setuptools import setup, find_packages

setup(
    name='purchase_broker',
    version='0.0.1',
    description='Custom app for managing purchase broker contracts',
    author='Your Name',
    author_email='email@example.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe']
)
