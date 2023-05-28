from PIL import Image, ImageFilter
import os
import glob
import csv


def one():
    os.chdir("files")
    path = os.getcwd()

    if not os.path.isdir("new_imgs"):
        os.mkdir("new_imgs")

    imgs = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for file in imgs:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.EMBOSS)
            new_img.show()
            os.chdir("new_imgs")
            new_img.save("new_" + file)
            os.chdir(path)


def two():
    os.chdir("files")
    path = os.getcwd()

    if not os.path.isdir("new_imgs"):
        os.mkdir("new_imgs")

    for file in glob.glob("*.jpg"):
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.EMBOSS)
            new_img.show()
            os.chdir("new_imgs")
            new_img.save("new_" + file)
            os.chdir(path)


def three():
    output = "Нужно купить:\n"
    sum = 0

    with open("data.csv", newline="") as value:
        reader = csv.reader(value)
        headline = next(value)

        for row in reader:
            output = output + row[0] + " - " + row[1] + " шт. за " + row[2] + " руб.\n"
            sum += (int(row[2]) * int(row[1]))

    print(f"{output}Итоговая сумма = {sum} руб.")


# one()
# two()
# three()