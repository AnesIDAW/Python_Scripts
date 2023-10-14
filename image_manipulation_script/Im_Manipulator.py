import PIL.Image as IM
import os
import concurrent.futures
import argparse

def process_image(image_path, output_folder, size, format):
    im = IM.open(image_path)
    im = im.resize(size)
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    im.save(output_path, format=format)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image Manipulation Script', usage='%(prog)s [-h] -i INPUT -o OUTPUT -s SIZE SIZE -f {JPEG,PNG,GIF}')
    parser.add_argument('-i', '--input', required=True, help='Path to the input folder containing images')
    parser.add_argument('-o', '--output', required=True, help='Path to the output folder')
    parser.add_argument('-s', '--size', required=True, type=int, nargs=2, help='Image size as WIDTH HEIGHT')
    parser.add_argument('-f', '--format', required=True, choices=['JPEG', 'PNG', 'GIF'], help='Output image format (JPEG, PNG, GIF)')

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    image_size = tuple(args.size)
    image_format = args.format

    os.makedirs(output_path, exist_ok=True)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        image_files = [os.path.join(input_path, image) for image in os.listdir(input_path) \
            if image.endswith(".jpg") or image.endswith(".png")]
        
        executor.map(process_image, image_files, [output_path] * len(image_files), \
            [image_size] * len(image_files), [image_format] * len(image_files))
