from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import random

class WelcomeScreen(Screen):
    def go_to_content(self):
        app = App.get_running_app()
        app.user_name = self.ids.name_input.text
        app.root.current = 'suggestion'

class SuggestionScreen(Screen):
    movies = {
        'Ação': ['Filme Ação 1', 'Filme Ação 2'],
        'Animação': ['Filme Animação 1', 'Filme Animação 2'],
        'Ficção Científica': ['Filme Ficção 1', 'Filme Ficção 2'],
        'Aventura': ['Filme Aventura 1', 'Filme Aventura 2'],
        'Terror': ['Filme Terror 1', 'Filme Terror 2'],
        'Drama': ['Filme Drama 1', 'Filme Drama 2'],
        'Comédia': ['Filme Comédia 1', 'Filme Comédia 2'],
        'Romance': ['Filme Romance 1', 'Filme Romance 2'],
        'Suspense': ['Filme Suspense 1', 'Filme Suspense 2']
    }

    def suggest_movie(self):
        genero = self.ids.genre_spinner.text
        app = App.get_running_app()
        nome = getattr(app, 'user_name', 'Usuário')
        if genero == 'Escolha o gênero':
            self.ids.result_label.text = "Escolha um gênero!"
            return
        filme = random.choice(self.movies[genero])
        self.ids.result_label.text = f"{nome}, assista: {filme}"

    def clear_fields(self):
        self.ids.result_label.text = ''
        self.ids.genre_spinner.text = 'Escolha o gênero'

class MovieApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(SuggestionScreen(name='suggestion'))
        return sm

if __name__ == '__main__':
    MovieApp().run()
