from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.properties import StringProperty, DictProperty
import random
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

class WelcomeScreenManager:
    pass

class SuggestionScreenManager:
    pass

class MovieApp(App):
    user_name = StringProperty('')
    movies = DictProperty({
        'Ação': ['Mad Max: Estrada da Fúria', 'John Wick', 'Duro de Matar'],
        'Comédia': ['Superbad', 'A Morte te Dá Parabéns', 'As Branquelas'],
        'Drama': ['À Espera de um Milagre', 'O Poderoso Chefão', 'Forrest Gump'],
        'Terror': ['It: A Coisa', 'O Exorcista', 'Hereditário'],
        'Ficção Científica': ['Blade Runner 2049', 'Duna', 'Matrix']
    })

    def build(self):
        sm = ScreenManager(transition=SlideTransition(direction="left", duration=0.5))
        return sm

    def suggest_movie(self, genre):
        if genre in self.movies:
            return random.choice(self.movies[genre])
        return None

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)  # Removido background_color
        self.title_label = Label(text='Bem-vindo ao App de Filmes', font_size=30, bold=True, color=(0, 0.8, 2, 1))
        layout.add_widget(self.title_label)

        self.name_input = TextInput(hint_text='Digite seu nome', size_hint_y=None, height=40, background_color=(1, 1, 1, 1))
        layout.add_widget(self.name_input)

        self.continue_button = Button(text='Continuar', size_hint_y=None, height=40, background_color=(0, 0.5, 1, 1))
        self.continue_button.bind(on_press=self.go_to_suggestion)
        layout.add_widget(self.continue_button)
        self.add_widget(layout)

    def go_to_suggestion(self, instance):
        app = App.get_running_app()
        app.user_name = self.name_input.text
        self.manager.current = 'suggestion'

class SuggestionScreen(Screen):
    def __init__(self, **kwargs):
        super(SuggestionScreen, self).__init__(**kwargs)
        self.movies = {
            'Ação': ['Mad Max: Estrada da Fúria', 'John Wick', 'Duro de Matar'],
            'Comédia': ['Superbad', 'A Morte te Dá Parabéns', 'As Branquelas'],
            'Drama': ['À Espera de um Milagre', 'O Poderoso Chefão', 'Forrest Gump'],
            'Terror': ['It: A Coisa', 'O Exorcista', 'Hereditário'],
            'Ficção Científica': ['Blade Runner 2049', 'Duna', 'Matrix']
        }
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.title_label = Label(text='App de Filmes', font_size=24, bold=True, color=(0, 0.8, 2, 1))
        layout.add_widget(self.title_label)

        self.genre_spinner = Spinner(
            text='Escolha o gênero',
            values=list(self.movies.keys()),
            size_hint_y=None,
            height=40
        )
        layout.add_widget(self.genre_spinner)
        self.limpar_button = Button(text='Limpar', size_hint_y=None, height=40, background_color=(1, 0, 0, 1))
        self.limpar_button.bind(on_press=self.on_button_limpar)
        layout.add_widget(self.limpar_button)

        self.button = Button(text='Sugerir filme', size_hint_y=None, height=40, background_color=(0, 0.5, 1, 1))
        self.button.bind(on_press=self.on_button_press)

        layout.add_widget(self.button)
        self.result_label = Label(text='', font_size=18)
        layout.add_widget(self.result_label)
        self.add_widget(layout)

    def on_button_press(self, instance):
        genero = self.genre_spinner.text
        app = App.get_running_app()
        nome = getattr(app, 'user_name', '')
        if genero == 'Escolha o gênero':
            self.result_label.text = "Escolha um gênero!"
            return
        filme = random.choice(self.movies[genero])
        self.result_label.text = f"{nome}, assista: {filme}"

    def on_button_limpar(self, instance):
        self.genre_spinner.text = 'Escolha o gênero'
        self.result_label.text = ''

    

class MovieApp(App):
    def build(self):
        self.user_name = ''
        sm = ScreenManager(transition=SlideTransition(direction="left", duration=0.5))
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(SuggestionScreen(name='suggestion'))
        return sm

if __name__ == '__main__':
    MovieApp().run()
