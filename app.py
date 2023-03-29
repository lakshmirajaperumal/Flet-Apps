import flet as ft
import os
import pdb

class ACCard(ft.UserControl):
    
    def add_click(self, e):
        
        self.counter += 1
        if self.counter%2 == 1:
            self.status.value = "AC ON"
            self.button.bgcolor=ft.colors.GREEN
            self.status.color=ft.colors.GREEN
        else:
            self.status.value = "AC OFF"
            self.button.bgcolor=ft.colors.RED
            self.status.color=ft.colors.RED
        #print("counter value : ",self.counter)  
          
        self.update()
        self.ac_info()
        self.update()
        
    def ac_info(self):
        if self.status.value=="AC OFF":
            print("AC is off") 
            self.time_range.visible=False
            self.slider.visible=False
            self.slider_text.visible=False
        else:
            print("AC is on")
            self.slider.visible=True
            self.slider_text.visible=True
            self.time_range.visible=True
    
    def submit_action(self,e):
        if self.status.value=="AC OFF":
            print(f"AC0{int(self.slider.value)}")
            self.serial_code.value= f"AC0{int(self.slider.value)}" 
        else:
            print(f"AC1{int(self.slider.value)}")
            self.serial_code.value= f"AC1{int(self.slider.value)}" 
        self.update()

    def temparature_change(self,e):
        print(self.slider.value)
        self.slider_text.value=f"{int(self.slider.value)}\u2103"
        self.update()
    
    def radiogroup_changed(self,e):
        self.timer_text.value = f"Your chosen time interval for AC is:  {e.control.value} mins"
        #AC slider for values
        time_range=ft.Text(value="0-15 Mins",visible=False)
        slider=ft.Slider(value=20.0,min=-20, max=40, divisions=60, label="{value}",on_change=self.temparature_change,visible=False)
        slider_text=ft.Text(value=f"{int(self.slider.value)} \u2103",visible=False)
        self.card.content.content.controls.extend([ft.Row([time_range]),ft.Row([slider,slider_text])])
        #pdb.set_trace()
            
        self.update()
    
    def build(self):
        #AC serial code
        self.serial_code=ft.Text(value="")
        
        #AC on off status
        self.counter = 0
        self.status = ft.Text("AC OFF",color=ft.colors.RED)
        self.button=ft.ElevatedButton("Status", color=ft.colors.WHITE,bgcolor=ft.colors.RED,on_click=self.add_click)
        
        
        #AC timer
        self.timer_text = ft.Text()
        self.timer_options = ft.RadioGroup(content=ft.Column([
            ft.Radio(value="0", label="Off"),
            ft.Radio(value="30", label="30 mins"),
            ft.Radio(value="60", label="60 mins"),
            ft.Radio(value="90", label="90 mins")],alignment=ft.alignment.top_left), on_change=self.radiogroup_changed)
        
        
        #AC slider for values
        self.time_range=ft.Text(value="0-15 Mins",visible=False)
        self.slider=ft.Slider(value=20.0,min=-20, max=40, divisions=60, label="{value}",on_change=self.temparature_change,visible=False)
        self.slider_text=ft.Text(value=f"{int(self.slider.value)} \u2103",visible=False)
        
        
        #submit action
        self.submit_button=ft.ElevatedButton("Submit", color=ft.colors.WHITE,bgcolor=ft.colors.BLUE,on_click=self.submit_action)
        #create a card for AC monitoring
        
        self.card=ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(name=ft.icons.AC_UNIT_ROUNDED,color=ft.colors.LIGHT_BLUE),
                            title=ft.Text("AC Control"),
                            # subtitle=ft.Text(
                            #     "Music by Julie Gable. Lyrics by Sidney Stein."
                            # ),
                        ),
                        ft.Row(
                            [self.button,self.status],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Row(
                            [self.timer_text],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Row(
                            [self.timer_options],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                         ft.Row(
                            [self.time_range],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Row(
                            [self.slider,self.slider_text],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Row(
                            [self.submit_button],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                        ft.Row(
                            [self.serial_code],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
        return self.card
    

def main(page:ft.Page):
    
    app_bar=ft.AppBar(leading=ft.IconButton(ft.icons.MENU, tooltip="Menu"),
        #leading_width=40,
        title=ft.Text("Patient Controller"),
        center_title=False,
        bgcolor=ft.colors.PURPLE)
    page.appbar=app_bar
    page.theme_mode=ft.ThemeMode.DARK
    card=ACCard()
    
    
    
    



    #page.add(ac_control)
    
    
    page.add(card)
    #print(ac_control.data)

ft.app(target=main)