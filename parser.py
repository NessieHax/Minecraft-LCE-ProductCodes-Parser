import os, argparse
from ProductCodeReader import ProductCodeReader

def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("console_product_file", action="store", type=str)
    argParser.add_argument("console_type", action="store", type=str, help="Specifies the console type", choices=["WIIU", "PS3", "PSV", "XBX"])
    argParser.add_argument("-l", "--list", action="store_true")
    # subParser = argParser.add_subparsers(title="modifiers", description="Allows modifications on the file")
    # addParser = subParser.add_parser("add")
    # addParser.add_argument("name", action="store", type=str, help="Name of the Product")
    # addParser.add_argument("category_type", action="store", type=int, help="Value between 0 and 4 (0 = Map Pack | 1 = Skin Pack | 2 = Texture Pack | 3 = Mash-Up Pack | 4 = Bundle Pack)")
    # addParser.add_argument("dlc_name", action="store", type=str, help="Name of the dlc image")
    # addParser.add_argument("pack_graphic_id", action="store", type=int, help="Id of the pack graphic to use (see MediaArc/Graphics/PackGraphics)")
    # delParser = subParser.add_parser("delete")
    # delParser.add_argument("name")
    # modParser = subParser.add_parser("modify")
    # modParser.add_argument("name")
    # modParser.add_argument("value", action="store")
    args = argParser.parse_args()

    if not os.path.exists(args.console_product_file): raise Exception("File does not exist")
    with open(args.console_product_file, "rb") as file:
        productReader = ProductCodeReader(args.console_type)
        productReader.process(file)

    if args.list:
        print(productReader)

if __name__ == "__main__":
    main()