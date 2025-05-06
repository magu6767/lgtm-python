from PIL import Image, ImageDraw, ImageFont

# 文字列の最大幅を画像の80%にする
MAX_RATIO = 0.8

# フォントの最大サイズ
FONT_MAX_SIZE = 256
# フォントの最小サイズ
FONT_MIN_SIZE = 24

# フォントの格納先パス（環境ごとに変わる）
FONT_NAME = '/Library/Fonts/Arial Unicode.ttf'
FONT_COLOR_WHITE = (255, 255, 255, 0)
    
# アウトプット関連の定数
OUTPUT_NAME = 'output.png'
OUTPUT_FORMAT = 'PNG'

def save_with_message(fp, message):
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)

    # メッセージを描画できる領域のサイズを、タプルの要素ごとに計算する
    image_width, image_height = image.size
    message_area_width = int(image_width * MAX_RATIO)
    message_area_height = int(image_height * MAX_RATIO)

    # 1ポイントずつ小さくしながら最適なフォントサイズを求める
    for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE, -1):
        font = ImageFont.truetype(FONT_NAME, font_size)
        text_width, text_height = draw.textsize(message, font=font)

        # メッセージを描画できる領域のサイズを超えたら、そのフォントサイズは採用できない
        if text_width <= message_area_width and text_height <= message_area_height:
            position = (
                (image_width - text_width) / 2,
                (image_height - text_height) / 2
            )
            # メッセージを描画する
            draw.text(position, message, font=font, fill=FONT_COLOR_WHITE)
            break

    # 画像を保存する
    image.save(OUTPUT_NAME, OUTPUT_FORMAT)
