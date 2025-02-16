import cv2
import numpy as np
import argparse
import os
import matplotlib.pyplot as plt

# دریافت ورودی از کاربر
parser = argparse.ArgumentParser(description="Convert an image to different bit depths.")
parser.add_argument("--image", type=str, required=True, help="Path to the input image")
parser.add_argument("--bit-depth", type=int, choices=[1, 4, 8], default=8, help="Bit depth (1, 4, or 8)")
args = parser.parse_args()

# خواندن تصویر در حالت خاکستری
image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found!")
    exit()

# تابع کاهش عمق بیت
def reduce_bit_depth(image, bit_depth):
    levels = 2 ** bit_depth  # تعداد سطوح رنگی
    factor = 256 // levels  # مقدار مقیاس بندی
    reduced_image = (image // factor) * factor  # کاهش سطوح رنگی
    return reduced_image

# ایجاد پوشه برای ذخیره خروجی
output_folder = "results"
os.makedirs(output_folder, exist_ok=True)

# کاهش عمق بیت و ذخیره تصویر
output_path = os.path.join(output_folder, f"image_{args.bit_depth}bit.png")
if args.bit_depth == 1:
    processed_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
else:
    processed_image = reduce_bit_depth(image, args.bit_depth)

cv2.imwrite(output_path, processed_image)
print(f"Processed image saved at: {output_path}")

# نمایش تصاویر
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(image, cmap="gray")
ax[0].set_title("Original (8-bit)")
ax[0].axis("off")

ax[1].imshow(processed_image, cmap="gray")
ax[1].set_title(f"{args.bit_depth}-bit")
ax[1].axis("off")

plt.show()
