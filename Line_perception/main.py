# assumtion
# 선들이 평행하게 뻗어 있을거임
# 정면에서 후방으로 갈수록 안쪽으로 꺾여서 있을거임
# 수평선에 닿지는 않고 흐릿해지거나 다른 지형지물에 의해 없어질거임
# 우리가 원하는 차선 정보가 담기지 않을 부분은 과감히 지워버림

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math

from moviepy.editor import VideoFileClip
from IPython.display import HTML

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)   # 원본이랑 크기, 타입, 차원 동일한 까만 이미지
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)  # 그릴 이미지, 꼭짓점들, 채울 색상 (255, 255, 255)
    # 만들어진 마스크는 까만 배경에 다각형 내부만 흰색인 배경임
    masked_image = cv2.bitwise_and(img, mask)  # and 연산이므로 마스크의 까만 부분은 이미지에서 삭제되고 다각형부분만 남음
    return masked_image

def draw_lines(img, lines, color=[255, 0, 0], thickness=3):
    line_img = np.zeros(
        (
            img.shape[0],
            img.shape[1],
            3), dtype=np.uint8
    )
    img = np.copy(img)
    if lines is None:
        return

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2), color, thickness)
    img = cv2.addWeighted(img, 0.8, line_img, 1.0, 0.0)
    return img

# image = mpimg.imread('./sample.jpg')

def pipeline(image):

    height = image.shape[0]
    width = image.shape[1]
    # region of interest ( triangle )
    region_of_interest_vertices = [
        (100, height),
        (width / 2, height / 2 + 50),
        (width-100, height)
    ]


    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    # 흑백변환
    cannyed_image = cv2.Canny(gray_image, 100, 200)     # edge 검출

    cropped_image = region_of_interest(
        cannyed_image,
        np.array([region_of_interest_vertices], np.int32)
    )

    lines = cv2.HoughLinesP(
        cropped_image,
        rho=6,
        theta=np.pi / 60,
        threshold=160,
        lines=np.array([]),
        minLineLength=40,
        maxLineGap=25
    )

    left_line_x = []
    left_line_y = []
    right_line_x = []
    right_line_y = []

    for line in lines:
        for x1, y1, x2, y2 in line:
            slope = (y2 - y1) / (x2 - x1)
            if math.fabs(slope) < 0.5:
                continue
            if slope <= 0:
                left_line_x.extend([x1, x2])
                left_line_y.extend([y1, y2])
            else:
                right_line_x.extend([x1, x2])
                right_line_y.extend([y1, y2])

    min_y = int(image.shape[0] * (3 / 5))
    max_y = int(image.shape[0])

    poly_left = np.poly1d(np.polyfit(
        left_line_y,
        left_line_x,
        deg = 1
    ))

    left_x_start = int(poly_left(max_y))
    left_x_end = int(poly_left(min_y))

    poly_left = np.poly1d(np.polyfit(
        right_line_y,
        right_line_x,
        deg = 1
    ))

    right_x_start = int(poly_left(max_y))
    right_x_end = int(poly_left(min_y))

    line_image = draw_lines(
        image,
        [[
            [left_x_start, max_y, left_x_end, min_y],
            [right_x_start, max_y, right_x_end, min_y]
        ]],
        thickness=5,
    )

    return line_image


white_output = './solidWhiteRight.mp4'
clip1 = VideoFileClip('./solidWhiteRight.mp4')
white_clip = clip1.fl_image(pipeline)
white_clip.write_videofile(white_output, audio=False)
