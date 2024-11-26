# DS-YOLO
DS-YOLO’s detailed open-source code 
# Install
Click to enter the folder, use the CMD command, and enter the following command in the command line window:

pip install -r `requirements.txt`

# Usage

- The `train.py` script is used to train the model on a custom dataset, with parameter configurations adhering to the standard conventions of the YOLO series algorithms.
- The `val.py` script is employed for model validation, allowing for a comprehensive evaluation of the experimental results.
- Additionally, the `visualize.py` script provides a visualization tool to facilitate dataset inspection, enabling further optimization of the dataset.

# Other

We have placed the improved module in `ultralytics\nn\extra_modules\block.py` for the readers' reference.
And we provide a link to the code used in the comparison experiment.

The source code reference link is as follows:

- [ultralytics](https://github.com/ultralytics/ultralytics)
- [PyTorch-Deformable-Convolution-v2](https://github.com/developer0hye/PyTorch-Deformable-Convolution-v2)
- [YOLO-FaceV2](https://github.com/Krasjet-Yu/YOLO-FaceV2)

