# SE-AGH: Project #2

This repository contains a Bayesian network project for the Expert Systems course at AGH University of Science and Technology (2020/2021).

The knowledge used by the system is based on the [Mushroom dataset](https://archive.ics.uci.edu/ml/datasets/mushroom) from the UCI Machine Learning Repository.

## Installation guide

### Requirements

This code was tested using Python 3.6.9, but presumably it should also work with other 3.x versions. Additionally, a [SMILE](https://www.bayesfusion.com/smile/) license is required. This README provides instructions for obtaining an academic license for those eligible, however a business license should also be appropriate.

### Setup

This project is based on a [GeNIe](https://www.bayesfusion.com/genie/) model and uses the [SMILE](https://www.bayesfusion.com/smile/) engine for inference.

You do not need to setup GeNIe, since the static model is already loaded into the project, however some setup is necessary for the SMILE library.

1. Install the required dependencies as per usual using the command `pip3 install -r requirements.txt`.
2. If you're eligible for an academic license, go to [SMILE's website](https://download.bayesfusion.com/files.html?category=Academia#SMILE) and download a zip with your access key. Unzip the file and copy the `pysmile_license.py` file into the root of the project. Otherwise, you can consult the [appropriate website](https://download.bayesfusion.com/files.html?category=Business) to inquire about obtaining a business license.

### Usage
Once you install all the dependencies, you can start the program by running the following command:

```bash
python3 model.py
```

**Note**: If you experience issues with the way the app scales on a high-DPI display, as a workaround you can try to play with the following environment variables:

```bash
export QT_AUTO_SCREEN_SCALE_FACTOR=1
export QT_SCALE_FACTOR=0.5
```

## Bibliography

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.
