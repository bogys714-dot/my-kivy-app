from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
import requests
import json
from threading import Thread
import time

class MeteoApp(App):
    def build(self):
        self.ip_address = "192.168.1.219"  # IP по умолчанию
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Заголовок
        title = Label(text='🌤️ Метеостанция', size_hint_y=None, height=50, font_size=24, bold=True)
        
        # Поле для ввода IP
        ip_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        ip_layout.add_widget(Label(text='IP адрес:', size_hint_x=0.3))
        self.ip_input = TextInput(text=self.ip_address, multiline=False, size_hint_x=0.7)
        ip_layout.add_widget(self.ip_input)
        
        # Кнопки
        btn_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        self.connect_btn = Button(text='Подключиться', on_press=self.connect_to_station)
        self.refresh_btn = Button(text='Обновить', on_press=self.refresh_data)
        btn_layout.add_widget(self.connect_btn)
        btn_layout.add_widget(self.refresh_btn)
        
        # Область для данных
        self.data_layout = GridLayout(cols=2, size_hint_y=None, spacing=10)
        self.data_layout.bind(minimum_height=self.data_layout.setter('height'))
        
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.data_layout)
        
        # Статус
        self.status_label = Label(text='Готов к подключению', size_hint_y=None, height=30)
        
        # Добавляем все элементы
        self.layout.add_widget(title)
        self.layout.add_widget(ip_layout)
        self.layout.add_widget(btn_layout)
        self.layout.add_widget(scroll)
        self.layout.add_widget(self.status_label)
        
        # Автоподключение при запуске
        Clock.schedule_once(lambda dt: self.connect_to_station(None), 1)
        
        return self.layout
    
    def connect_to_station(self, instance):
        self.ip_address = self.ip_input.text.strip()
        self.status_label.text = 'Подключаемся...'
        Thread(target=self.fetch_data).start()
    
    def refresh_data(self, instance):
        self.status_label.text = 'Обновляем данные...'
        Thread(target=self.fetch_data).start()
    
    def fetch_data(self):
        try:
            # Получаем текущие данные
            response = requests.get(f'http://{self.ip_address}/data', timeout=5)
            data = response.json()
            
            # Получаем историю
            history_response = requests.get(f'http://{self.ip_address}/history', timeout=5)
            history = history_response.json()
            
            # Обновляем UI в основном потоке
            Clock.schedule_once(lambda dt: self.update_ui(data, history), 0)
            
        except Exception as e:
            Clock.schedule_once(lambda dt: self.show_error(str(e)), 0)
    
    def update_ui(self, data, history):
        self.data_layout.clear_widgets()
        
        # Текущие данные
        self.add_data_row('🌡️ Температура', f"{data['temperature']} °C")
        self.add_data_row('💧 Влажность', f"{data['humidity']} %")
        self.add_data_row('📊 Давление', f"{data['pressure']} мм рт.ст.")
        
        # Последние 5 записей истории
        self.add_data_row('', '')  # Пустая строка
        self.add_data_row('📈 История', 'Последние записи:')
        
        for i, record in enumerate(history[-5:]):  # Последние 5 записей
            from datetime import datetime
            timestamp = datetime.fromtimestamp(record['t']).strftime('%H:%M')
            self.add_data_row(f'🕒 {timestamp}', f"{record['temp']}°C, {record['hum']}%")
        
        self.status_label.text = 'Данные обновлены'
    
    def add_data_row(self, label, value):
        self.data_layout.add_widget(Label(text=label, size_hint_y=None, height=40))
        self.data_layout.add_widget(Label(text=value, size_hint_y=None, height=40))
    
    def show_error(self, error):
        self.data_layout.clear_widgets()
        self.add_data_row('❌ Ошибка', str(error))
        self.status_label.text = 'Ошибка подключения'

if __name__ == '__main__':
    MeteoApp().run()