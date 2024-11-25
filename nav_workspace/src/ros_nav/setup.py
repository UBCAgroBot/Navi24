from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros_nav'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Arman D',
    maintainer_email='adrismir@gmail.com',
    description='Agrobot\'s navigation nodes',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor_controller = ros_nav.motor_controller:main',
            'arduino_listener = ros_nav.arduino_listener:main'
        ],
    },
)
