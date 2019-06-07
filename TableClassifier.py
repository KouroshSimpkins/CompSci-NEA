import os
import cv2
import imutils

def pre_process_image(img, save_in_file, morph_size=(8, 8)):
    
    # Make image monochrome
    pre = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Otsu threshold
    pre = cv2.threshold(pre, 250, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    cpy = pre.copy()
    struct = cv2.getStructuringElement(cv2.MORPH_RECT, morph_size)
    cpy = cv2.dilate(~cpy, struct, anchor=(-1, -1), iterations=1)
    pre = ~cpy

    if save_in_file is not None:
        cv2.imwrite(save_in_file, pre)
    return pre

def find_text_boxes(pre, min_text_height_limit=6, max_text_height_limit=40):
    # Searching for text spots contours
    contours = cv2.findContours(pre, cv2.RETR_LIST, cv2.CHAIN_IN_APPROX_SAMPLE)
    contours = contours[0] if imutils.is_cv2() else contours[1]

    # Getting bounding boxes for text based on size assumptions
    boxes = []
    for contour in contours:
        box = cv2.boundingRect(contour)
        h = box[3]
        
        if min_text_height_limit < h < max_text_height_limit:
            boxes.append(box)

    return boxes

def find_table_in_boxes(boxes, cell_threshold=10, min_colums=2):
    rows = {}
    cols = {}

    # Clustering the bounding boxes by their positions
    for box in boxes:
        (x, y, w, h) = box
        col_key = x // cell_threshold
        row_key = y // cell_threshold
        cols[row_key] = [box] if col_key not in cols else cols[col_key] + [box]
        rows[row_key] = [box] if row_key not in rows else rows[row_key] + [box]

    table_cells = list(filter(lambda r: len(r) >= min_colums, rows.values()))
    table_cells = [list(sorted(tb)) for tb in table_cells]
    table_cells = list(sorted(table_cells, key=lambda r: r[0][1]))

    return table_cells

    