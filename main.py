from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from lbs.screen.home_page import HomePage
class InstragramApp(MDApp):
    def build(self):
        Window.size=[300,600]
        self.load_all_kv_files()
        return HomePage()

    def load_all_kv_files(self) -> None:
        Builder.load_file('lbs/screen/home_page.kv')
        Builder.load_file('lbs/components/appbar.kv')
        Builder.load_file('lbs/components/story_creator.kv')
        Builder.load_file('lbs/components/bottom_nav.kv')
        Builder.load_file('lbs/components/circular_avatar_image.kv')
        Builder.load_file('lbs/components/post_card.kv')

    def on_start(self):
        self.root.dispatch("on_enter")
    
if __name__=="__main__":
    InstragramApp().run()