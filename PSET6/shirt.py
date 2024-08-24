import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    _, input_ext = sys.argv[1].split(".")
    _, output_ext = sys.argv[2].split(".")
    if output_ext.lower() not in ("jpg", "jpeg", "png") or input_ext.lower() not in (
        "jpg",
        "jpeg",
        "png",
    ):
        sys.exit("Wrong input or output file type")
    if output_ext != input_ext:
        sys.exit("Input and output have different extensions")
    adjuster(sys.argv[1], sys.argv[2])


def adjuster(input, output):
    try:
        with Image.open(input) as photo, Image.open("shirt.png") as shirt:
            size = shirt.size
            photo = ImageOps.fit(
                photo,
                size,
            )
            photo.paste(shirt, shirt)
            photo.save(output)
    except FileNotFoundError:
        sys.exit("Input file does not exist")


if __name__ == "__main__":
    main()
