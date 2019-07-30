import Augmentor

def augment_(args):

    p = Augmentor.Pipeline(args["root_dir"])

    #Default params
    probability_ = args["probability"]
    magnitude_ = args["magnitude"]
    left_r_ = args["left_r"]
    right_r = args["right_r"]
    grid_ = args["grid"]
    minf_ = args["min_factor"]
    maxf_ = args["max_factor"]
    num_ = args["num"]

    # Operations
    flip_ = args["flip"]
    rotate_ = args["rotate"]
    distortion_ = args["distortion"]
    skew_ = args["skew"]
    zoom_ = args["zoom"]

    if rotate_:
        p.rotate(probability=probability_, max_left_rotation=left_r_, max_right_rotation=right_r)
    if distortion_:
        p.random_distortion(probability=probability_, grid_width=grid_, grid_height=grid_, magnitude=magnitude_)
    if skew_:
        p.skew(probability=probability_, magnitude=0.7)
    if zoom_:
        p.zoom(probability=probability_, min_factor=minf_, max_factor=maxf_)
    if flip_:
        p.flip_random(probability=probability_)

    p.sample(num_)