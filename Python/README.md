# Randomer Forest (rerf) Python Package

## Requirements

Python bindings are made using [pybind11](https://github.com/pybind/pybind11).

C++ compiler (gcc)

  ```sh
  sudo apt-get install build-essential cmake python3-dev libomp-dev   # Ubuntu/Debian
  ```

## Environment

Activate virtualenv

```sh
python3 -m venv env
. env/bin/activate
```

Install requirements

```sh
pip install pybind11
```

- Install from github

  ```sh
  pip install -e "git+https://github.com/neurodata/RerF.git@pybind#egg=rerf&subdirectory=Python"
  ```

- Build from source

  Get the source files:

  ```sh
  git clone https://github.com/neurodata/R-RerF.git
  ```
  
  You may have to initialize the RerF/src submodule (these commands can also be found in RerF/src/submodule_readme.md):
  ```sh
  cd RerF/src
  git submodule update --init
  git config --global submodule.recurse true
  git config --global status.submoduleSummary true
  cd ../..
  ```
  Then, go to the Python directory:
  ```sh
  cd R-RerF/Python
  ```

  Then either:
  
  - Build the package using `setup.py`

    ```sh
    pip install -e .
    ```

  - Run the following compile script

    ```sh
    c++ -O3 -Wall -shared -std=c++14 -fPIC `python3 -m pybind11 --includes` packedForest.cpp -o pyfp`python3-config --extension-suffix`
    ```

  Note: problems running the compile command on alternate shells (`fish`).  Make sure to use `bash` for the time being.

## Run the example

[Example.py](example.py)

## Tests

We use pytest for Python testing

Run the tests from command line at the root of the repo (`RerF/`)

  ```sh
  python -m pytest
  ```
