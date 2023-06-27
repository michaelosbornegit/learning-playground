import os
os.environ['KIVY_VIDEO'] = 'ffpyplayer'

from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

class EditorApp(App):
    # def slider_change(self, slider, value):
    #     print(self.video.loaded)
    #     if (self.video.loaded):
    #         print(value)
    #         self.video.seek(slider.value / 100, False)
    #         self.video.state = 'stop'
    
    def video_change(self, video, value):
        # self.slider.max = video.duration
        # print('value is', video.position / video.duration)
        # print(video)
        self.slider.value = video.position / video.duration

    def on_slider_touch(self, slider, value):
        if (self.video.loaded):
            print('TOUCHED')
            self.video.state = 'stop'
        

    def on_release(self, slider, value):
        if (self.video.loaded):
            print('RELEASED')
            print(slider.value)
            self.video.seek(slider.value, True)
            # self.video.position = slider.value
            self.video.state = 'play'

    def build(self):
        layout = BoxLayout(orientation='vertical')

        video = Video(source = 'input/test2.mp4')
        video.state = 'play'
        # video.options = {'eos': 'loop'}
        video.allow_stretch = True
        video.bind(position=self.video_change)

        # slider = Slider(min = 1, max = 99, value = 1)
        slider = Slider(min = 0, max = 1, value = 0)
        # slider.bind(value=self.slider_change)
        slider.bind(on_touch_up=self.on_release)
        slider.bind(on_touch_down=self.on_slider_touch)

        self.video = video
        self.slider = slider

        layout.add_widget(video)
        layout.add_widget(slider)

        return layout
    
if __name__ == "__main__":
    window = EditorApp()
    window.run()