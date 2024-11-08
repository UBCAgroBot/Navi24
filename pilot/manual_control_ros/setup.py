from setuptools import find_packages, setup

package_name = 'ros_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vscode',
    maintainer_email='adrismir@gmail.com',
    description='A ROS package that sends information between an image publisher and subscriber',
    license='No license',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
