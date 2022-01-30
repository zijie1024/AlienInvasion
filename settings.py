# _*_ coding : utf-8 _*_
# @Time : 2022/1/29 19:33
# @Author : 字节幺零二四
# @Filename : settings
# @Project : AlienInvasion
class Settings:
    """存储游戏中所有设置"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_size = (800, 400)
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_limit = 3
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        # 外星人设置
        self.fleet_drop_speed = 10
        # 加快游戏的节奏
        self.speedup_scale = 1.1
        # 外星人分数提高的速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始随游戏进行而变化的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction 为1表示向右移动，为-1表示向左移动
        self.fleet_drop_direction = 1
        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置和外星人的分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
