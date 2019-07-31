
# Rudi

If you want to train a CNN, the custom dataset must be a collection of images of the same aspect ratio, extension, etc.
This script is gonna do that for you. Rudi is a command line tool for converting and augmenting your dataset of images.

# Installation

Install `Python3` and then run the following command:
```sh
pip install rudi
```

or clone the repo firs 
```sh
git clone https://github.com/liashchynskyi/rudi
cd rudi
```
and run `python setup.py install` or `pip install .`

# Usage
![Imgur](https://i.imgur.com/KIi431Z.png)
---
* [Convert a dataset](#convert-a-dataset)
* [Dataset augmentation](#dataset-augmentation)
* [Donate](#donate)

# Convert a dataset

For example, you have a basic tree of the root directory (the script will also work if the root containt only images without other dirs).
```
root    
└───class1
│   │   image_c1.png
│   │   image_c2.png
│   └───subdirectory    
└───class2
    │   image_c1.png
    │   image_c2.png
```

Just run `rudi convert --help`
![Imgur](https://i.imgur.com/GAWRBja.png)

Let's convert images in current directory to `jpg` format and set new aspect ratio to `224px`.
```sh
rudi convert -t jpg --target-size=224 ./
```
Output images will be saved in `output` dir of the root.

# Dataset augmentation

Command: `rudi augment --help`
![Imgur](https://i.imgur.com/64Ijbjr.png)

There are a few supported operations:
* `flip` - random image flipping followed by `-p` option
* `rotate` - random image rotation followed by `-p`,`-mlr` and `-mrr` options
* `distortion` - random image distortion followed by `-p`,`-mg` and `-gwh` options
* `skew` - random image skewing followed by `-p` option and constant `magnitude` value of `0.7`
* `zoom` - random image zooming followed by `-p`,`-minf` and `-maxf` options

Output images will be saved in `output` dir of the root.

# Donate
Just put a star on this repository 🌞 Thanks!

<div align="center">
made by <a href="https://github.com/liashchynskyi">@liashchynskyi</a>
</div>