import os, sys
import uuid
from PIL import Image, ImageOps
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count


class Converter:

    def __init__(self, args):
        self.listDir = None
        self.root = None
        self.args = args

    def makeDir(self, path, name):
        dir = os.path.join(path, name)
        if not os.path.exists(dir):
            os.mkdir(dir)
        return dir

    def getDirs(self, root):
        self.root = root
        self.listDir = [os.path.join(root, o) for o in os.listdir(root)
                        if os.path.isdir(os.path.join(root, o))]
        self.output = self.makeDir(root, "output")
        return len(self.listDir)

    def readd(self, dir):
        for name in os.listdir(dir):
            path = os.path.join(dir, name)
            if os.path.isfile(path):
                self.convert(path)
            elif name != "output":
                self.readd(path)

    def convert(self, file):
        img = Image.open(str(file))
        out_img = ImageOps.fit(img, (self.args[1], self.args[1]), Image.ANTIALIAS, 0, (0.5, 0.5))
        out_img = out_img.convert('RGB')

        root_of_file = os.path.basename(os.path.dirname(file))
        file_out_dir = self.makeDir(self.output, root_of_file)
        file_out_path = file_out_dir + os.path.sep + uuid.uuid4().hex[:7].lower() + '.' + self.args[0]

        if self.args[0] == 'jpg':
            out_img.save(file_out_path, quality=100)
        else:
            out_img.save(file_out_path)
        print("[ 🌸 ] Converted and saved ", file_out_path)



def convert_(*args):
    pool = Pool(cpu_count())
    converter = Converter(args)
    len_dirs = converter.getDirs(args[2])
    pool.map(converter.readd, converter.listDir) if len_dirs > 0 else converter.readd(converter.root)

    pool.close()
    pool.join()
