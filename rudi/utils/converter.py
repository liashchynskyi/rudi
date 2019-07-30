import os, sys
import argparse
from PIL import Image, ImageOps
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count


class Converter:

    def __init__(self, args):
        self.listDir = None
        self.root = None
        self.args = args

    def getDirs(self, root):
        self.root = root
        self.listDir = [os.path.join(root, o) for o in os.listdir(root)
                        if os.path.isdir(os.path.join(root, o))]

    def readd(self, dir):
        for name in os.listdir(dir):
            path = os.path.join(dir, name)
            if os.path.isfile(path):
                self.convert(path)
            else:
                self.readd(path)

    def convert(self, file):
        ext = os.path.splitext(file)
        img = Image.open(str(file))
        out_img = ImageOps.fit(img, (self.args.fit_to_size, self.args.fit_to_size), Image.ANTIALIAS, 0, (0.5, 0.5))
        out_img = out_img.convert('RGB')
        if ext[1] != ".jpg":
            out_file = os.path.splitext(file)[0] + '.jpg'
        else:
            out_file = os.path.splitext(file)[0] + '_re.jpg'
        out_img.save(out_file, quality=100)
        os.remove(str(file))
        print("[+] Converted ", out_file)


parser = argparse.ArgumentParser()

parser.add_argument("-f", "--fit-to-size", type=int, help="fit all the images to that size (default: 224)", default=224)

requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-r", "--root-dir", type=str, help="root directory of the images", required=True)

args = parser.parse_args()

pool = Pool(cpu_count())
converter = Converter(args)
converter.getDirs(args.root_dir)
pool.map(converter.readd, converter.listDir)

pool.close()
pool.join()
