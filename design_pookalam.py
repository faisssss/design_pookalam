import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge, Polygon, Circle, Rectangle

def draw_design():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-11, 11)
    ax.set_ylim(-11, 11)
    ax.axis('off')
    ax.set_facecolor('whitesmoke')

    center_colors = {
        'star1': ['#FF0066', '#CC0099', '#9900CC', '#6600FF', '#3333FF', '#0066FF', '#0099CC', '#00CC99'],
        'octagon': ['#FF3333', '#FF9933', '#FFFF33', '#99FF33', '#33FF33', '#33FF99', '#33FFFF', '#3399FF'],
        'star2': ['#FF6666', '#FFB366', '#FFFF66', '#B3FF66', '#66FF66', '#66FFB3', '#66FFFF', '#66B3FF']
    }
    
    radius1 = 2.5
    radius2 = 1.5
    for i in range(8):
        angle1 = np.deg2rad(i * 45)
        angle2 = np.deg2rad((i + 0.5) * 45)
        angle3 = np.deg2rad((i - 0.5) * 45)
        
        p1 = [0, 0]
        p2 = [radius1 * np.cos(angle1), radius1 * np.sin(angle1)]
        p3 = [radius2 * np.cos(angle2), radius2 * np.sin(angle2)]
        triangle1 = Polygon([p1, p2, p3], facecolor=center_colors['star1'][i], edgecolor='black')
        ax.add_patch(triangle1)

    radius3 = 1.5
    radius4 = 1.0
    for i in range(8):
        angle1 = np.deg2rad(i * 45)
        angle2 = np.deg2rad((i + 1) * 45)
        
        p1 = [radius3 * np.cos(angle1), radius3 * np.sin(angle1)]
        p2 = [radius4 * np.cos(angle1), radius4 * np.sin(angle1)]
        p3 = [radius4 * np.cos(angle2), radius4 * np.sin(angle2)]
        p4 = [radius3 * np.cos(angle2), radius3 * np.sin(angle2)]
        
        poly = Polygon([p1, p2, p3, p4], facecolor=center_colors['octagon'][i], edgecolor='black')
        ax.add_patch(poly)

    center_star_radius = 1.0
    for i in range(8):
        angle_start = np.deg2rad(i * 45 - 22.5)
        angle_end = np.deg2rad(i * 45 + 22.5)
        wedge = Wedge((0, 0), center_star_radius, np.rad2deg(angle_start), np.rad2deg(angle_end), 
                      facecolor=center_colors['star2'][i], edgecolor='black')
        ax.add_patch(wedge)
        
    center_circle = Circle((0, 0), 0.5, facecolor='white', edgecolor='black', zorder=10)
    ax.add_patch(center_circle)
    
    petal_colors = ['#FFFF00', '#FFEA00', '#FFD500', '#FFC000', '#FFAB00', '#FF9600', '#FF8100']
    num_petals = 8
    
    for i in range(num_petals):
        angle_offset = i * (360 / num_petals)
        for j, color in enumerate(petal_colors):
            radius = 7.5 - j * 0.7
            width = 30
            start_angle = 180 + angle_offset - (width / 2)
            end_angle = 180 + angle_offset + (width / 2)
            
            wedge = Wedge((0, 0), radius, start_angle, end_angle, 
                          width=0.7, facecolor=color, edgecolor=color)
            ax.add_patch(wedge)

    mosaic_colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#3D3D3D']
    
    num_rings = 4
    base_radius = 7.8
    ring_width = 0.55
    
    for ring in range(num_rings):
        current_radius = base_radius + ring * ring_width
        circumference = 2 * np.pi * current_radius
        num_tiles = int(circumference / (ring_width*0.9))
        angle_step = 360 / num_tiles
        
        for i in range(num_tiles):
            angle_start = i * angle_step
            angle_end = (i + 1) * angle_step
            color = np.random.choice(mosaic_colors)
            
            wedge = Wedge((0, 0), current_radius + ring_width, 
                          angle_start, angle_end, width=ring_width, 
                          facecolor=color, edgecolor='black', lw=0.5)
            ax.add_patch(wedge)

    outer_circle = Circle((0, 0), 10.2, facecolor='none', edgecolor='black', lw=4)
    ax.add_patch(outer_circle)
    
    plt.show()

if __name__ == '__main__':
    draw_design()