import pyMeow as pm
from math import cos, sin, pi

# تنظیمات قابل تغییر برای دایره بیضی شکل
ellipse_left = {
    "radius_x": 399 ,      # شعاع افقی دایره (برای بیضی) - بزرگتر شده
    "radius_y": 328,      # شعاع عمودی دایره (برای بیضی) - بزرگتر شده
    "angle": 0,           # زاویه چرخش دایره به سمت راست
    "num_points": 36,     # تعداد نقاط دایره برای رسم
    "color": pm.new_color(139, 69, 19, 255),  # رنگ قهوه‌ای ملایم
}

ellipse_right = {
    "radius_x": 366 ,      # شعاع افقی دایره (برای بیضی) - بزرگتر شده
    "radius_y": 285,      # شعاع عمودی دایره (برای بیضی) - بزرگتر شده
    "angle": 0,           # زاویه چرخش دایره به سمت راست
    "num_points": 86,     # تعداد نقاط دایره برای رسم
    "color": pm.new_color(139, 69, 19, 255),  # رنگ قهوه‌ای ملایم
}

def draw_rotated_ellipse(settings, centerX, centerY):
    radius_x = settings["radius_x"]
    radius_y = settings["radius_y"]
    angle = settings["angle"]
    num_points = settings["num_points"]
    color = settings["color"]
    
    points = []
    
    # محاسبه نقاط بیضی قبل از چرخش
    for i in range(num_points):
        angle_step = 2 * pi * i / num_points
        x = centerX + radius_x * cos(angle_step)
        y = centerY + radius_y * sin(angle_step)
        
        # چرخش نقاط با استفاده از زاویه
        rotated_x = centerX + (x - centerX) * cos(angle) - (y - centerY) * sin(angle)
        rotated_y = centerY + (x - centerX) * sin(angle) + (y - centerY) * cos(angle)
        
        points.append((rotated_x, rotated_y))
    
    # رسم بیضی چرخیده
    for i in range(num_points):
        next_index = (i + 1) % num_points
        pm.draw_line(points[i][0], points[i][1], points[next_index][0], points[next_index][1], color)

# آغاز حلقه رسم با تنظیم FPS به حداقل (1)
pm.overlay_init(fps=1)  # تنظیم FPS به کمترین مقدار (1)
while pm.overlay_loop():
    pm.begin_drawing()  # شروع رسم
    
    # تغییرات پویا با استفاده از زمان واقعی (با `time.time()` تغییرات پویا ایجاد می‌شود)  # زمان سپری شده از شروع برنامه
    ellipse_left["color"] = pm.new_color(
        int((1 * 10) % 255), 100, int((1 * 5) % 255), 255
    )  # تغییر رنگ به طور پویا
    
    # رسم بیضی در مختصات (642, 424)
    #draw_rotated_ellipse(ellipse_left, 653, 490)
    draw_rotated_ellipse(ellipse_right, 784, 355)
    
    pm.end_drawing()  # پایان رسم
