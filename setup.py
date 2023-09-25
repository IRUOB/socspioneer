from setuptools import find_packages, setup

package_name = 'socspioneer'

setup(
    name=package_name,
    version='3.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yan',
    maintainer_email='yxw257@student.bham.ac.uk',
    description='SOCSPioneer package for ROS Humble with simulation support.',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'twist = socspioneer.twist:main'
        ],
    },
)
