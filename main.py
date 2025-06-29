import cv2
import argparse
import os

def cartoonify(image_path, sigma_color=300, sigma_space=300):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not read the image at {image_path}")
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9, 9
    )

    color = cv2.bilateralFilter(img, d=9, sigmaColor=sigma_color, sigmaSpace=sigma_space)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

def save_cartoon_image(cartoon_image, output_path):
    cv2.imwrite(output_path, cartoon_image)
    print(f"✅ Cartoon image saved to: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Cartoonify an image using OpenCV")
    parser.add_argument("input", help="Path to input image")
    parser.add_argument("output", help="Path to save cartoon image")
    parser.add_argument("--sigma_color", type=int, default=300, help="Sigma color value for bilateral filter")
    parser.add_argument("--sigma_space", type=int, default=300, help="Sigma space value for bilateral filter")

    args = parser.parse_args()

    cartoon = cartoonify(args.input, args.sigma_color, args.sigma_space)
    if cartoon is not None:
        save_cartoon_image(cartoon, args.output)

if __name__ == "__main__":
    main()

