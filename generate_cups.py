import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, Circle, Ellipse
import numpy as np
import os

# 创建输出目录
OUTPUT_DIR = "cup_images"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def createCupImage1():
    """生成第一张杯子图片 - 经典马克杯"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    
    # 杯身主体
    cup_body = Rectangle((3, 2), 4, 5, facecolor='lightblue', 
                        edgecolor='navy', linewidth=2)
    ax.add_patch(cup_body)
    
    # 杯底
    cup_bottom = Ellipse((5, 2), 4, 0.5, facecolor='lightblue', 
                        edgecolor='navy', linewidth=2)
    ax.add_patch(cup_bottom)
    
    # 杯口
    cup_top = Ellipse((5, 7), 4, 0.5, facecolor='white', 
                     edgecolor='navy', linewidth=2)
    ax.add_patch(cup_top)
    
    # 杯把手
    handle = patches.Arc((7.2, 4.5), 1.5, 3, angle=0, theta1=30, theta2=330,
                        color='navy', linewidth=3)
    ax.add_patch(handle)
    
    # 装饰图案
    heart = patches.Circle((5, 4.5), 0.5, facecolor='red', alpha=0.7)
    ax.add_patch(heart)
    
    ax.set_title('经典马克杯', fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/cup1_classic_mug.png', dpi=300, bbox_inches='tight')
    plt.close()

def createCupImage2():
    """生成第二张杯子图片 - 咖啡杯"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    
    # 杯身 - 梯形状
    cup_points = np.array([[3.5, 2], [6.5, 2], [6, 6.5], [4, 6.5]])
    cup_body = patches.Polygon(cup_points, facecolor='saddlebrown', 
                              edgecolor='darkred', linewidth=2)
    ax.add_patch(cup_body)
    
    # 杯底
    cup_bottom = Ellipse((5, 2), 3, 0.4, facecolor='saddlebrown', 
                        edgecolor='darkred', linewidth=2)
    ax.add_patch(cup_bottom)
    
    # 杯口
    cup_top = Ellipse((5, 6.5), 2, 0.3, facecolor='black', 
                     edgecolor='darkred', linewidth=2)
    ax.add_patch(cup_top)
    
    # 托盘
    saucer = Ellipse((5, 1.5), 5, 0.8, facecolor='wheat', 
                    edgecolor='darkred', linewidth=2)
    ax.add_patch(saucer)
    
    # 杯把手
    handle = patches.Arc((6.8, 4), 1.2, 2.5, angle=0, theta1=45, theta2=315,
                        color='darkred', linewidth=3)
    ax.add_patch(handle)
    
    # 咖啡蒸汽
    for i, x_offset in enumerate([-0.3, 0, 0.3]):
        steam = patches.Arc((5 + x_offset, 7.5 + i*0.2), 0.3, 0.8, 
                           angle=0, theta1=0, theta2=180,
                           color='gray', linewidth=2, alpha=0.6)
        ax.add_patch(steam)
    
    ax.set_title('咖啡杯', fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/cup2_coffee_cup.png', dpi=300, bbox_inches='tight')
    plt.close()

def createCupImage3():
    """生成第三张杯子图片 - 茶杯"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    
    # 杯身 - 优雅的弧形
    cup_body = patches.Arc((5, 4), 3.5, 4, angle=0, theta1=0, theta2=180,
                          color='pink', linewidth=8)
    ax.add_patch(cup_body)
    
    # 杯底连接线
    bottom_line = plt.Line2D([3.25, 6.75], [4, 4], color='pink', linewidth=8)
    ax.add_line(bottom_line)
    
    # 杯口
    cup_top = Ellipse((5, 6), 3.5, 0.4, facecolor='lightpink', 
                     edgecolor='deeppink', linewidth=2)
    ax.add_patch(cup_top)
    
    # 杯底
    cup_bottom = Ellipse((5, 4), 3.5, 0.4, facecolor='lightpink', 
                        edgecolor='deeppink', linewidth=2)
    ax.add_patch(cup_bottom)
    
    # 精致的托盘
    saucer = Ellipse((5, 3.5), 5.5, 0.8, facecolor='lavender', 
                    edgecolor='deeppink', linewidth=2)
    ax.add_patch(saucer)
    
    # 小巧的把手
    handle = patches.Arc((7, 5), 0.8, 1.5, angle=0, theta1=60, theta2=300,
                        color='deeppink', linewidth=3)
    ax.add_patch(handle)
    
    # 花朵装饰
    for angle in [0, 72, 144, 216, 288]:
        x = 5 + 0.6 * np.cos(np.radians(angle))
        y = 5 + 0.6 * np.sin(np.radians(angle))
        flower = patches.Circle((x, y), 0.15, facecolor='gold', alpha=0.8)
        ax.add_patch(flower)
    
    ax.set_title('精致茶杯', fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/cup3_tea_cup.png', dpi=300, bbox_inches='tight')
    plt.close()

def createCupImage4():
    """生成第四张杯子图片 - 运动水杯"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    
    # 杯身 - 高大的圆柱形
    cup_body = Rectangle((3.5, 2), 3, 6, facecolor='lightgreen', 
                        edgecolor='darkgreen', linewidth=2)
    ax.add_patch(cup_body)
    
    # 杯底
    cup_bottom = Ellipse((5, 2), 3, 0.4, facecolor='lightgreen', 
                        edgecolor='darkgreen', linewidth=2)
    ax.add_patch(cup_bottom)
    
    # 杯盖
    lid = Ellipse((5, 8), 3, 0.4, facecolor='darkgreen', 
                 edgecolor='black', linewidth=2)
    ax.add_patch(lid)
    
    # 吸管
    straw = Rectangle((5.8, 8), 0.2, 1.5, facecolor='red', 
                     edgecolor='darkred', linewidth=1)
    ax.add_patch(straw)
    
    # 握把区域
    grip_lines = []
    for y in np.linspace(3, 7, 8):
        line = plt.Line2D([3.5, 6.5], [y, y], color='darkgreen', 
                         linewidth=1, alpha=0.5)
        ax.add_line(line)
    
    # 品牌标志
    logo = patches.Circle((5, 5), 0.8, facecolor='white', 
                         edgecolor='darkgreen', linewidth=2)
    ax.add_patch(logo)
    
    # 标志内的文字用简单图形代替
    inner_circle = patches.Circle((5, 5), 0.4, facecolor='darkgreen')
    ax.add_patch(inner_circle)
    
    ax.set_title('运动水杯', fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/cup4_sports_bottle.png', dpi=300, bbox_inches='tight')
    plt.close()

def generateAllCups():
    """生成所有杯子图片"""
    print("开始生成杯子图片...")
    
    createCupImage1()
    print("✓ 已生成第1张图片：经典马克杯")
    
    createCupImage2()
    print("✓ 已生成第2张图片：咖啡杯")
    
    createCupImage3()
    print("✓ 已生成第3张图片：精致茶杯")
    
    createCupImage4()
    print("✓ 已生成第4张图片：运动水杯")
    
    print(f"\n所有图片已保存到 '{OUTPUT_DIR}' 文件夹中！")

if __name__ == "__main__":
    generateAllCups()


