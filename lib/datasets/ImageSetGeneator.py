import os
class ImageSetGenerator:

    def __init__(self, path, save_path):
        file1 = open(save_path, "w")  # write mode
        for x in os.listdir(path):
            if x.endswith(".png"):
                name = x.split(".png")[0]
                file1.write(name+"\n")
        file1.close()


if __name__ == '__main__':
    # ImageSetGenerator("../../data/firearm/train_imgs", "../../data/firearm/train_set.txt")
    ImageSetGenerator("../../data/firearm/test_imgs", "../../data/firearm/ImageSets/test_set.txt")
