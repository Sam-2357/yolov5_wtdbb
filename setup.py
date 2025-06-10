from setuptools import setup, find_packages

setup(
    name="yolov5-wtdbb",
    version="0.0.1",
    python_requires=">=3.8",
    # keep only real Python packages, ignore data/ etc.
    packages=find_packages(exclude=("data*", "segment*", "classify*", "runs*", "weights*")),
    install_requires=[
        "torch>=2.0",
        "opencv-python>=4.5",
        "numpy",
        # whatever else Ultralytics requires
    ],
)
