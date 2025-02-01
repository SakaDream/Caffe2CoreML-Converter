# Caffe2CoreML Converter

This project provides a tool to convert Caffe models to Apple's CoreML format, enabling the use of pre-trained Caffe models in iOS applications.

## Features

- Convert Caffe models (`.caffemodel` and `.prototxt`) to CoreML models (`.mlmodel`).
- Support for common Caffe layers.
- Easy-to-use command-line interface.

## Requirements

- Python 3.6+

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/SakaDream/Caffe2CoreML-Converter.git
    cd Caffe2CoreML-Converter
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

### Note for Mac Silicon Users

CoreMLTools 4.1 may not run correctly on Mac Silicon (M1, M1 Pro, M1 Max, M2, etc.). To work around this issue, Mac Silicon users need to install Miniconda 23.1.0 (Python 3.7), create a new conda environment, and then install CoreMLTools and other dependencies within that environment. This Miniconda version has been tested on a MacBook Pro 2021 running macOS 15.2. Follow these steps:

1. Download and install Miniconda 23.1.0 (Python 3.7) from the [direct download link](https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-MacOSX-x86_64.sh).

2. Install Miniconda:
    ```sh
    chmod +x Miniconda3-py37_23.1.0-1-MacOSX-x86_64.sh
    ./Miniconda3-py37_23.1.0-1-MacOSX-x86_64.sh
    ```

    Follow the prompts during the installation:
    - When asked if you want to continue the installation, type `yes`.
    - Press `ENTER` to review the license agreement.
    - Type `yes` to accept the license terms.
    - Press `ENTER` to confirm the installation location or specify a different location.
    - Type `yes` to initialize Miniconda3 by running `conda init`.

    After the installation is complete, close and re-open your current shell for the changes to take effect.

3. Create a new conda environment:
    ```sh
    conda create --name coreml-env python=3.7
    conda activate coreml-env
    ```

4. Install the required Python packages within the conda environment:
    ```sh
    pip install -r requirements.txt
    ```

5. Run the Python script normally within the conda environment.

6. Once you are done working with the CoreML environment, you can deactivate the conda environment by running:
    ```sh
    conda deactivate
    ```

## Usage

```sh
$ python script.py -h           
usage: script.py [-h] --caffemodel CAFFEMODEL --prototxt PROTOTXT --labels
                 LABELS --output OUTPUT

Convert Caffe model to CoreML model.

optional arguments:
  -h, --help            show this help message and exit
  --caffemodel CAFFEMODEL
                        Path to the Caffe model file.
  --prototxt PROTOTXT   Path to the Caffe deploy prototxt file.
  --labels LABELS       Path to the labels file.
  --output OUTPUT       Path to save the CoreML model.
```

### Example

```sh
python script.py --caffemodel models/oxford102.caffemodel --prototxt models/deploy.prototxt --labels models/flower-labels.txt --output models/FlowerClassifier.mlmodel
```

## Running on Docker

You can also run the converter using Docker.

1. Build the Docker image:
    ```sh
    docker build --platform linux/amd64 -t caffe2coreml-converter .
    ```

2. Run the converter inside the Docker container:
    ```sh
    docker run --platform linux/amd64 --rm -v $(pwd):/workdir caffe2coreml-converter \
        --caffemodel <path/to/model.caffemodel> \
        --prototxt <path/to/deploy.prototxt> \
        --labels <path/to/labels.txt> \
        --output <path/to/output.mlmodel>
    ```

### Example

```sh
docker run --platform linux/amd64 --rm -v $(pwd):/workdir caffe2coreml-converter \
    --caffemodel models/oxford102.caffemodel \
    --prototxt models/deploy.prototxt \
    --labels models/flower-labels.txt \
    --output models/FlowerClassifier.mlmodel
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Caffe](http://caffe.berkeleyvision.org/)
- [CoreMLTools](https://github.com/apple/coremltools)
