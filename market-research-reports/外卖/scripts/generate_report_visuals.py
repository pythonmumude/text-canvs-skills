#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
外卖市场研究报告 - 图表生成脚本
中国外卖行业趋势报告2025
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

# 设置中文字体支持
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 设置图表风格
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

def create_market_size_chart():
    """生成市场规模趋势图"""
    # 数据
    years = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025E']
    market_size = [1250, 2000, 3000, 4410, 5770, 7152, 8934, 10350, 15000, 16357, 19000]
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # 创建渐变色条形图
    colors = plt.cm.Blues(np.linspace(0.3, 0.9, len(years)))
    bars = ax.bar(years, market_size, color=colors, edgecolor='navy', linewidth=1.5)
    
    # 添加数值标签
    for bar, size in zip(bars, market_size):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 200,
                f'{size/1000:.1f}万亿',
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # 添加趋势线
    x_points = np.arange(len(years))
    z = np.polyfit(x_points, market_size, 2)
    p = np.poly1d(z)
    ax.plot(years, p(x_points), "r--", alpha=0.8, linewidth=2, label='趋势线')
    
    ax.set_title('中国餐饮外卖市场规模趋势 (2015-2025)', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('年份', fontsize=12)
    ax.set_ylabel('市场规模（亿元）', fontsize=12)
    ax.set_ylim(0, 22000)
    ax.legend(loc='upper left')
    
    # 添加关键节点标注
    ax.annotate('2025年\n预计1.9万亿', 
                xy=(10, 19000), xytext=(8, 21000),
                fontsize=11, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='red'),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('/Users/mumu/Downloads/opencode/skill/market-research-reports/外卖/figures/01_market_size_trend.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_market_share_chart():
    """生成市场份额饼图"""
    # 数据
    labels = ['美团', '淘宝闪购', '京东外卖']
    sizes = [48, 33, 19]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    explode = (0.05, 0.02, 0.02)
    
    fig, ax = plt.subplots(figsize=(12, 10))
    
    wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                       autopct='%1.1f%%', startangle=90,
                                       textprops={'fontsize': 14, 'fontweight': 'bold'},
                                       pctdistance=0.75)
    
    # 添加中心圆创建环形图
    centre_circle = plt.Circle((0, 0), 0.45, fc='white')
    ax.add_artist(centre_circle)
    
    ax.set_title('中国外卖市场竞争格局 (2025年Q4)', fontsize=16, fontweight='bold', pad=20)
    
    # 添加详细说明
    details_text = """
    美团：绝对领导者
    - 市场份额：48%
    - 日订单：8000-9000万
    - 用户数：8亿+
    
    淘宝闪购：快速追赶者
    - 市场份额：33%
    - 日订单：5500-6000万
    - 增长：200%
    
    京东外卖：新进入者
    - 市场份额：19%
    - 日订单：3000-3500万
    - 覆盖：350+城市
    """
    
    ax.text(0, -1.5, details_text, ha='center', va='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('/Users/mumu/Downloads/opencode/skill/market-research-reports/外卖/figures/02_market_share.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_tam_sam_som_chart():
    """生成TAM/SAM/SOM同心圆图"""
    fig, ax = plt.subplots(figsize=(14, 14))
    
    # 数据（单位：万亿元）
    tam = 6.0  # 总餐饮市场
    sam = 2.5  # 可服务市场（外卖渗透率提升）
    som = 0.5  # 可获得市场（实际可获得份额）
    
    # 创建同心圆
    colors = ['#E3F2FD', '#90CAF9', '#42A5F5']
    labels = ['TAM: 总可市场\n6万亿元\n(中国餐饮总市场)', 
              'SAM: 服务可市场\n2.5万亿元\n(外卖渗透率提升后)', 
              'SOM: 可获得市场\n0.5万亿元\n(实际可获得份额)']
    
    # 绘制同心圆
    for i, (radius, color, label) in enumerate(zip([3, 2, 1], colors, labels)):
        circle = plt.Circle((0, 0), radius, color=color, ec='navy', linewidth=2, alpha=0.7)
        ax.add_patch(circle)
        
        # 添加标签
        ax.text(0, radius, label, ha='center', va='center', fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9))
    
    # 添加箭头和说明
    ax.annotate('', xy=(2.5, 0.5), xytext=(0.8, 0.3),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(2.8, 0.7, '增长空间', fontsize=12, fontweight='bold', color='red')
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('中国外卖市场 TAM/SAM/SOM 分析', fontsize=16, fontweight='bold', pad=20)
    
    # 添加说明
    note_text = """
    关键洞察：
    • 当前外卖渗透率约26%，仍有巨大提升空间
    • 随着消费习惯养成，渗透率有望达到40%+
    • 品质升级和场景扩展将推动市场扩容
    """
    ax.text(0, -3.5, note_text, ha='center', va='center', fontsize=11,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    
    plt.tight_layout()
    plt.savefig('/Users/mumu/Downloads/opencode/skill/market-research-reports/外卖/figures/03_tam_sam_som.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_instant_retail_chart():
    """生成即时零售市场规模图"""
    years = ['2020', '2021', '2022', '2023', '2024', '2025E', '2026E', '2030E']
    market_size = [2200, 3200, 4500, 6500, 7810, 9714, 10000, 20000]
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # 创建面积图
    ax.fill_between(years, market_size, alpha=0.3, color='blue')
    ax.plot(years, market_size, 'b-o', linewidth=2, markersize=10)
    
    # 添加数值标签
    for year, size in zip(years, market_size):
        ax.text(year, size + 500, f'{size}亿', ha='center', fontsize=10, fontweight='bold')
    
    ax.set_title('中国即时零售市场规模趋势 (2020-2030)', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('年份', fontsize=12)
    ax.set_ylabel('市场规模（亿元）', fontsize=12)
    ax.set_ylim(0, 25000)
    
    # 添加关键节点
    ax.axvline(x='2024', color='green', linestyle='--', alpha=0.5)
    ax.text(2024, 22000, '当前: 7810亿', ha='center', fontsize=10, color='green', fontweight='bold')
    
    ax.axvline(x='2026E', color='orange', linestyle='--', alpha=0.5)
    ax.text('2026E', 24000, '突破万亿', ha='center', fontsize=10, color='orange', fontweight='bold')
    
    ax.axvline(x='2030E', color='red', linestyle='--', alpha=0.5)
    ax.text('2030E', 23000, '2万亿', ha='center', fontsize=10, color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/Users/mumu/Downloads/opencode/skill/market-research-reports/外卖/figures/04_instant_retail_market.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_competitive_positioning_chart():
    """生成竞争定位矩阵"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 平台数据 (x: 市场覆盖度, y: 技术能力, s: 市场份额*100)
    platforms = {
        '美团': {'x': 95, 'y': 90, 'size': 48, 'color': '#FF6B6B'},
        '淘宝闪购': {'x': 85, 'y': 85, 'size': 33, 'color': '#4ECDC4'},
        '京东外卖': {'x': 60, 'y': 80, 'size': 19, 'color': '#45B7D1'}
    }
    
    # 绘制散点图
    for name, data in platforms.items():
        ax.scatter(data['x'], data['y'], s=data['size']*50, c=data['color'], 
                   alpha=0.7, edgecolors='black', linewidth=2)
        ax.text(data['x'], data['y'] + 3, name, ha='center', va='bottom', 
                fontsize=12, fontweight='bold')
    
    # 添加象限标签
    ax.text(95, 95, '领导者\n(高覆盖+高技术)', ha='center', va='center', 
            fontsize=10, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    ax.text(50, 95, '挑战者\n(低覆盖+高技术)', ha='center', va='center', 
            fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    ax.text(95, 50, '守成者\n(高覆盖+低技术)', ha='center', va='center', 
            fontsize=10, bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
    ax.text(50, 50, '补缺者\n(低覆盖+低技术)', ha='center', va='center', 
            fontsize=10, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
    
    ax.set_xlim(40, 100)
    ax.set_ylim(40, 100)
    ax.set_xlabel('市场覆盖度', fontsize=12)
    ax.set_ylabel('技术能力', fontsize=12)
    ax.set_title('外卖平台竞争定位矩阵', fontsize=16, fontweight='bold', pad=20)
    
    # 添加网格
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.axhline(y=70, color='gray', linestyle='--', alpha=0.5)
    ax.axvline(x=70, color='gray', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('/Users/mumu/Downloads/opencode/skill/market-research-reports/外卖/figures/05_competitive_positioning.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_swot_analysis_chart():
    """生成SWOT分析图"""
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # SWOT数据
    swot_data = {
        'Strengths (优势)': [
            '• 市场规模庞大，用户基数全球第一',
            '• 完善的即时配送网络',
            '• 丰富的商家供给和品类覆盖',
            '• 技术驱动的运营效率',
            '• 用户消费习惯已经养成'
        ],
        'Weaknesses (劣势)': [
            '• 平台竞争激烈，利润率承压',
            '• 骑手权益保障问题',
            '• 食品安全监管挑战',
            '• 佣金模式受商家诟病',
            '• 同质化竞争严重'
        ],
        'Opportunities (机会)': [
            '• 下沉市场渗透空间大',
            '• 即时零售品类扩展',
            '• 品质升级趋势明显',
            '• 技术创新提升效率',
            '• 政策规范促进健康发展'
        ],
        'Threats (威胁)': [
            '• 监管政策趋严',
            '• 国际竞争者潜在进入',
            '• 经济下行压力',
            '• 替代品竞争（预制菜、社区团购）',
            '• 成本持续上升'
        ]
    }
    
    # 标题
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    ax.set_title('中国外卖市场 SWOT 分析', fontsize=18, fontweight='bold', pad=20)
    
    # 颜色方案
    colors = {
        'Strengths': '#90EE90',  # 绿色
        'Weaknesses': '#FFB6C1',  # 红色
        'Opportunities': '#87CEEB',  # 蓝色
        'Threats': '#DDA0DD'  # 紫色
    }
    
    # 绘制四个象限
    positions = {
        'Strengths': (0.5, 6.5, 4.5, 5.5),
        'Weaknesses': (5, 6.5, 4.5, 5.5),
        'Opportunities': (0.5, 1, 4.5, 5.5),
        'Threats': (5, 1, 4.5, 5.5)
    }
    
    for title, (x, y, w, h) in positions.items():
        # 绘制背景
        rect = plt.Rectangle((x, y), w, h, facecolor=colors[title], alpha=0.3, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        # 添加标题
        ax.text(x + w/2, y + h - 0.5, title, ha='center', va='center', 
                fontsize=12, fontweight='bold')
        
        # 添加内容
        content = swot_data[title]
        for i, item in enumerate(content):
            ax.text(x + 0.3, y + h - 1.5 - i*0.9, item, ha='left', va='center', fontsize=9)
    
    # 添加分析结论
    conclusion = """
    战略建议：
    1. 发挥规模优势，提升运营效率
    2. 加大技术投入，构建竞争壁垒
    3. 拓展下沉市场，寻找新增长点
    4. 强化品质服务，差异化竞争
    5. 关注骑手权益，可持续发展
    """
    ax.text(5, 0.2, conclusion, ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    
    plt.tight_layout()
    plt.savefig('/Users/mumu/Downloads/opencode/skill/market-research-reports/外卖/figures/06_swot_analysis.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_porters_five_forces_chart():
    """生成波特五力分析图"""
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # 设置坐标系
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axis('off')
    ax.set_title("波特五力分析 - 中国外卖市场", fontsize=18, fontweight='bold', pad=20)
    
    # 定义位置
    positions = {
        'competitive_rivalry': {'x': 0, 'y': 0, 'label': '竞争强度', 'rating': '高', 'desc': '激烈\n(三国杀)'},
        'new_entrants': {'x': 0, 'y': 4, 'label': '新进入者威胁', 'rating': '中', 'desc': '京东入局'},
        'substitutes': {'x': 4, 'y': 0, 'label': '替代品威胁', 'rating': '中', 'desc': '预制菜/便利店'},
        'buyer_power': {'x': -4, 'y': 0, 'label': '买家议价能力', 'rating': '高', 'desc': '用户选择多'},
        'supplier_power': {'x': 0, 'y': -4, 'label': '供应商议价能力', 'rating': '低', 'desc': '商家依赖平台'}
    }
    
    # 颜色映射
    color_map = {
        '高': '#FF6B6B',
        '中': '#FFD93D',
        '低': '#6BCB77'
    }
    
    # 绘制中心圆
    center = plt.Circle((0, 0), 1.5, facecolor='#FF6B6B', edgecolor='black', linewidth=2)
    ax.add_patch(center)
    ax.text(0, 0.3, '竞争强度', ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(0, -0.5, '高', ha='center', va='center', fontsize=12, fontweight='bold', color='white')
    ax.text(0, -1.2, '(三国杀)', ha='center', va='center', fontsize=8, color='white')
    
    # 绘制五个力
    for force, data in positions.items():
        if force == 'competitive_rivalry':
            continue
        
        # 绘制连接线
        ax.plot([0, data['x']], [0, data['y']], 'k-', linewidth=2)
        
        # 绘制力圆
        color = color_map[data['rating']]
        circle = plt.Circle((data['x'], data['y']), 1.2, facecolor=color, 
                           edgecolor='black', linewidth=2, alpha=0.7)
        ax.add_patch(circle)
        
        # 添加标签
        ax.text(data['x'], data['y'] + 0.3, data['label'], ha='center', va='center', 
                fontsize=8, fontweight='bold', wrap=True)
        ax.text(data['x'], data['y'] - 0.3, data['rating'], ha='center', va='center', 
                fontsize=10, fontweight='bold')
        ax.text(data['x'], data['y'] - 1.0, data['desc'], ha='center', va='center', 
                fontsize=7, style='italic')
    
    # 添加分析说明
    analysis = """
    关键洞察：
    • 竞争强度最高：三国杀格局形成，补贴战激烈
    • 新进入者威胁中等：京东成功入局，但门槛仍高
    • 替代品威胁中等：预制菜、便利店分流部分需求
    • 买家议价能力高：用户选择多，平台需讨好用户
    • 供应商议价能力低：商家依赖平台获客
    
    战略含义：行业吸引力中等，竞争激烈，需差异化竞争
    """
    ax.text(0, -4.5, analysis, ha='center', va='center', fontsize=9,
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    
    plt.tight_layout()
    plt.savefig('/Users/mumu/Downloads/opencode/skill/market-research-reports/外卖/figures/07_porters_five_forces.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_daily_order_trend_chart():
    """生成日订单量趋势图"""
    months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    orders = [1.0, 1.2, 1.5, 1.8, 2.0, 2.2, 2.4, 2.9, 2.6, 2.5, 2.4, 2.5]
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # 绘制趋势线
    ax.plot(months, orders, 'b-o', linewidth=2, markersize=8)
    ax.fill_between(months, orders, alpha=0.2, color='blue')
    
    # 标注关键节点
    ax.annotate('京东入局\n(2月)', xy=(1, 1.2), xytext=(2, 1.5),
                fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='red'),
                bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))
    
    ax.annotate('淘宝闪购上线\n(4月)', xy=(3, 1.5), xytext=(4, 2.0),
                fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='orange'),
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    ax.annotate('补贴战峰值\n(8月)', xy=(7, 2.9), xytext=(5, 2.5),
                fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='purple'),
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    ax.set_title('2025年外卖日均订单量趋势（亿单）', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('月份', fontsize=12)
    ax.set_ylabel('日均订单量（亿单）', fontsize=12)
    ax.set_ylim(0.5, 3.5)
    ax.grid(True, linestyle='--', alpha=0.3)
    
    # 添加统计信息
    stats_text = f"""
    全年平均: {np.mean(orders):.2f}亿单
    峰值: {max(orders):.1f}亿单 (8月)
    增长率: {((orders[-1] - orders[0]) / orders[0] * 100):.0f}%
    """
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('/Users/mumu/Downloads/opencode/skill/market-research-reports/外卖/figures/08_daily_order_trend.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_platform_comparison_chart():
    """生成平台对比图"""
    platforms = ['美团', '淘宝闪购', '京东外卖']
    metrics = ['市场份额\n(%)', '用户规模\n(亿)', '日订单量\n(千万)', '覆盖城市\n(个)', '入驻商家\n(万)']
    
    # 数据矩阵
    data = np.array([
        [48, 8, 85, 2800, 450],  # 美团
        [33, 3, 55, 3500, 200],  # 淘宝闪购
        [19, 0.5, 30, 350, 150]  # 京东外卖
    ])
    
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # 创建热力图
    im = ax.imshow(data, cmap='YlOrRd', aspect='auto')
    
    # 设置标签
    ax.set_xticks(np.arange(len(metrics)))
    ax.set_yticks(np.arange(len(platforms)))
    ax.set_xticklabels(metrics, fontsize=11)
    ax.set_yticklabels(platforms, fontsize=11)
    
    # 添加数值标签
    for i in range(len(platforms)):
        for j in range(len(metrics)):
            text = ax.text(j, i, f'{data[i, j]:.1f}',
                          ha="center", va="center", color="black", fontsize=11, fontweight='bold')
    
    ax.set_title('外卖平台核心指标对比 (2025年Q4)', fontsize=16, fontweight='bold', pad=20)
    
    # 添加颜色条
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel('数值', rotation=-90, va="bottom")
    
    plt.tight_layout()
    plt.savefig('/Users/mumu/Downloads/opencode/skill/market-research-reports/外卖/figures/09_platform_comparison.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def main():
    """主函数：生成所有图表"""
    print("开始生成外卖市场研究报告图表...")
    
    # 确保输出目录存在
    import os
    output_dir = '/Users/mumu/Downloads/opencode/skill/market-research-reports/外卖/figures'
    os.makedirs(output_dir, exist_ok=True)
    
    # 生成所有图表
    charts = [
        ('市场规模趋势图', create_market_size_chart),
        ('市场份额饼图', create_market_share_chart),
        ('TAM/SAM/SOM同心圆', create_tam_sam_som_chart),
        ('即时零售市场规模', create_instant_retail_chart),
        ('竞争定位矩阵', create_competitive_positioning_chart),
        ('SWOT分析图', create_swot_analysis_chart),
        ('波特五力分析图', create_porters_five_forces_chart),
        ('日订单量趋势图', create_daily_order_trend_chart),
        ('平台对比图', create_platform_comparison_chart)
    ]
    
    for chart_name, chart_func in charts:
        try:
            print(f"生成 {chart_name}...")
            chart_func()
            print(f"✓ {chart_name} 生成成功")
        except Exception as e:
            print(f"✗ {chart_name} 生成失败: {e}")
    
    print("\n图表生成完成！")
    print(f"图表保存位置: {output_dir}")

if __name__ == '__main__':
    main()
