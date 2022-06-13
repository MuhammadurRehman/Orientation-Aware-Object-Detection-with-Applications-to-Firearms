class ImageSetSpliter:

    def __init__(self, src_path, dest_path):
        file1 = open(src_path, "r")
        file_data = file1.read()
        images = file_data.split('\n')
        train_size = int(len(images) * 0.8)
        train_set = images[:train_size]
        val_set = images[train_size:]
        file1 = open(dest_path + "train.txt", "w")
        file2 = open(dest_path + "val.txt", "w")
        for l in train_set:
            file1.write(l+"\n")
        for l in val_set:
            file2.write(l+"\n")
        file1.close()
        file2.close()


if __name__ == '__main__':
    ImageSetSpliter("../../data/firearm/ImageSets/trainval.txt", "../../data/firearm/ImageSets/")
