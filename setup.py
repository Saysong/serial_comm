from setuptools import setup

package_name = 'serial_comm'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools', 'pyserial'],
    zip_safe=True,
    maintainer='Cesar Morales Xochipiltecatl',
    maintainer_email='mcesar@gatech.edu',
    description='ROS2 package for reading serial data from USB',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'serial_publisher = serial_comm.serial_publisher:main',
            'serial_subscriber = serial_comm.serial_subscriber:main',
        ],
    },
)

