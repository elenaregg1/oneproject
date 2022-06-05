
import bluetooth
from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        #nearby_devices = bluetooth.discover_devices(lookup_names=True)
        #print("Found {} devices.")
        return Button(text="MOUBUTON", on_press=self.btn_press)

    def btn_press(self,instance):
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        print("Found {} devices.".format(len(nearby_devices)))
        instance.text=str(format(len(nearby_devices)))


if __name__=="__main__":
    MyApp().run()
#nearby_devices = bluetooth.discover_devices(lookup_names=True)
#print("Found {} devices.".format(len(nearby_devices)))

#for addr, name in nearby_devices:
 #   print("  {} - {}".format(addr, name))

