from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class ServicioApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        self.fecha_input = TextInput(text='Fecha')
        self.monto_input = TextInput(text='Monto')
        self.lugar_input = TextInput(text='Lugar')
        
        agregar_button = Button(text='Agregar Servicio')
        agregar_button.bind(on_press=self.agregar_servicio)
        
        self.resultado_label = Label(text='')
        
        layout.add_widget(self.fecha_input)
        layout.add_widget(self.monto_input)
        layout.add_widget(self.lugar_input)
        layout.add_widget(agregar_button)
        layout.add_widget(self.resultado_label)
        
        return layout
    
    def agregar_servicio(self, instance):
        fecha = self.fecha_input.text
        monto = float(self.monto_input.text)
        lugar = self.lugar_input.text
        
        # Aquí agregarías la lógica para guardar el servicio
        
        self.resultado_label.text = f'Servicio agregado: {fecha}, {monto}, {lugar}'

if __name__ == '__main__':
    ServicioApp().run()