from setuptools import setup, find_packages

setup(
    name="ziyang-sdk",
    version="3.0.0",
    description="紫阳智库v3算力测试SDK",
    author="紫阳智库团队",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.5.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "ziyang-benchmark=ziyang.cli:main",
        ],
    },
)