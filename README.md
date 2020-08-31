# SCS-Siam PyTorch implementation
## Introduction
This is my project in the direction of Visual Object Tracking.

**SCS-Siam architecture**

![img1](https://github.com/mustansarfiaz/SCS-Siam/blob/master/framework/framework.png)

## How to Run - Training
1. **Prerequisites:** The project was built using **python 3.7** and tested on Ubuntu 18.04. It was tested on a **NVIDIA GeForce GTX 1080**. Furthermore it requires [PyTorch 1.0 or more](https://pytorch.org/).

2. Download the **GOT-10k** Dataset in http://got-10k.aitestunion.com/downloads and extract it on the folder of your choice, in my case it is `/media/mustansar/data/benchmarks/GOT-10k` (OBS: data reading is done in execution time, so if available extract the dataset in your SSD partition).


3. Download the ImageNet VID Dataset in http://bvisionweb1.cs.unc.edu/ILSVRC2017/download-videos-1p39.php and extract it on the folder of your choice (OBS: data reading is done in execution time, so if available extract the dataset in your SSD partition). You can get rid of the test part of the dataset, since it has no Annotations.

4. In **config.py** script `root_dir_for_GOT_10k`, `root_dir_for_VID and` and `root_dir_for_OTB` change to your directory. 
```
root_dir_for_GOT_10k = '/media/mustansar/data/benchmarks/GOT-10k' <-- change to your directory 
root_dir_for_VID     = '/media/mustansar/data/benchmarks/VID'     <-- change to your directory
root_dir_for_OTB     = '/media/mustansar/data/benchmarks/OTB2015' <-- change to your directory 
```

5. Run the **train.py** script:
```
python3 train.py
```

## How to Run - Testing
1. Download pretrained `model_e32.pth` from [Google-Drive] (https://drive.google.com/file/d/1HkTxVQ58b0dAPHbySI3wSdBTLudpzqsy/view?usp=sharing), and put the file under `model/model_e32.pth`.

2. Run the **test.py** script:
```
python3 test.py
```

## Results - 
**OTB2015**
<center>
    <figure>
        <figcaption>
            <img src="framework/result_otb.jpg" height="60%" width="100%">
        </figcaption>
    </figure>
</center>

## Citing
```
@article{fiaz2020learning,
  title={Learning Soft Mask Based Feature Fusion with Channel and Spatial Attention for Robust Visual Object Tracking},
  author={Fiaz, Mustansar and Mahmood, Arif and Jung, Soon Ki},
  journal={Sensors},
  volume={20},
  number={14},
  pages={4021},
  year={2020},
  publisher={Multidisciplinary Digital Publishing Institute}
}
```


