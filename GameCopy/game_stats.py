class GameStats():
    # ����������� ��������� ����������
    
    def __init__(self, ai_settings):
        
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # ������ ���� � ���������� ���������.
        self.game_active = False
        
        # ��������� ���� �� ������ ����������.
        self.high_score = 1000
        
    def reset_stats(self):
        # ��������� ����������
        self.ships_left = self.ai_settings.ship_limit
        self.score = 1000000
        self.level = 1
