from setuptools import setup


setup(
    name='cldfbench_tudet',
    py_modules=['cldfbench_tudet'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'tudet=cldfbench_tudet:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
        'conllu',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
