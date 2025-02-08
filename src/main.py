from image_parser import parse_image_from_path


text = parse_image_from_path(
    "resources/receipt_images/photo_2025-02-07_15-12-24.jpg",
    lang="rus"
)
print(text)
