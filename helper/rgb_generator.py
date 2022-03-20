import re

from helper.lib_helper import check_is_file_exist
import webcolors

COLOR_RES_REGEX = "<color name=\"(.*)\">(.*)<\/color>"
OUTPUT_DATASET_RGBA_BUILDER = "%s,%s,%s\n"


# Convert Hex to RGBA
# EG: #AD689C9E will return 104,156,158,173
def hex_to_rgba(hex) -> str:
    try:
        # will raise error if alpha found in hex
        rgb = webcolors.hex_to_rgb(hex)
        # hardcoded alpha to 255
        return ','.join([str(rgb.red), str(rgb.green), str(rgb.blue), str(255)])
    except ValueError:
        temp_hex = '#' + hex[3:]
        rgb = webcolors.hex_to_rgb(temp_hex)
        alpha = int(hex[1:3], 16)
        return ','.join([str(rgb.red), str(rgb.green), str(rgb.blue), str(alpha)])


def generate_rgb_from_colors_xml(file_path):
    is_file_exist = check_is_file_exist(file_path)

    if is_file_exist:
        with open(file_path, 'r') as file:
            with open('color_dataset_rgba.txt', 'w') as output:
                for line in file:
                    line = line.strip()
                    regex_matcher = re.match(COLOR_RES_REGEX, line)
                    if regex_matcher:
                        hex = regex_matcher[2]
                        rgba = hex_to_rgba(hex)
                        result = OUTPUT_DATASET_RGBA_BUILDER % (regex_matcher[1], regex_matcher[2], rgba)
                        output.write(result)


def main():
    # color_file_path = sys.argv[1]
    generate_rgb_from_colors_xml('color_dataset_sample.txt')


if __name__ == '__main__':
    main()
