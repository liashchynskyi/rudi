
# Image converter

If you want to train your network model you need to take the images of the same aspect ratio.

I wrote the next script for doing this thing. The script supports converting only to **JPG**.

### Requirements
1. Installed **Python 3** environment;
2. Installed **Pillow** library;
3. Root directory of your images. 

**The script only works if your root directory contains directories of the image classes inside.** It is necessary for multithreading executing (one class folder - one thread), after that if the class folder also contains the other directories inside, the script will work recursively. 

For example:
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

## How to use it?

Download and install dependencies:
```sh
$ pip install Pillow
```
or
```sh
$ python -m pip install Pillow
```
Run it:
```sh
$ python converter.py -r ROOT_DIR -f SIZE
```
* ROOT_DIR - root directory of the images;
* SIZE - image size after conversion.

For help use `-h` or `--help`.
