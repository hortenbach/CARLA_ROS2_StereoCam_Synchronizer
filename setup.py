from setuptools import setup

package_name = 'carla_vo'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hortenbach',
    maintainer_email='hortenbach@todo.todo',
    description='tools for stereo odometry for CARLA',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'stereo_syncronizer2 = carla_vo.stereo_sync2:main'
        ],
    },
)
