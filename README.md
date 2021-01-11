# KBS

This repository contains the Python code used in training an object recognition model for tables recognition on PDF documents. The repository also contains the final saved model of the latest training.

## Installation

First clone the master branch of the Tensorflow Models repository
```bash
git clone https://github.com/tensorflow/models.git

```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
cd models/research
# Compile protos.
protoc object_detection/protos/*.proto --python_out=.
# Install TensorFlow Object Detection API.
cp object_detection/packages/tf1/setup.py .
python -m pip install .

```

## Test the installation
From ``models/research`` run:

```
python object_detection/builders/model_builder_tf1_test.py
```

## Using the included Python scripts

All the scripts need to be run from the appropriate folder or the results placed in ``/models/research/object_recognition/training``

### resize_images.py
```bash
python resize_images.py -d jpg_data/ -s 600 800
```

### xml_to_csv.py
Set the images folder path
```python
images_path = 'images/'
```
Run
```bash
python xml_to_csv.py
```

### pdf_to_jpg
Change both variables to the correct path
```python
pdf_data_path = './pdf_data'
jpg_data_path = './jpg_data'
```
Run
```bash
python pdf_to_jpg.py
```

### generate_tfrecord.py
Change the following lines to match the required classes, in this case:
```python
def class_text_to_int(row_label):
    if row_label == 'table':
        return 1
    else:
        return None
```
Run
```bash
python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record
python generate_tfrecord.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=test.record
```

### run_predictions.py
Place the images in the root directory together with the script
Run
```bash
python run_predictions.py
```

## Training model
```bash
python model_main.py --logtostderr --model_dir=training/ --pipeline_config_path=training/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/pipeline.config
```

## Opening Tensorboard
```bash
tensorboard --logdir=training
```

## Exporting inference graph
```bash
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/pipeline.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph
```