# Import built-in libraries of system and datetime
import os
from datetime import datetime
# Import libraries which allows conection between Google Sheets and programm
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Import libraries of GUI
from kivy.config import Config
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivymd.uix.imagelist import SmartTileWithLabel
#from kivymd.uix.managerswiper import MDSwiperPagination
from kivymd.uix.bottomnavigation import MDBottomNavigation
#--------System configuration---------
Config.set('graphics','resizable',0)
Window.size = (600, 800)
#--------System configuration---------
#---------Connection with Google Sheets--------------------------------------
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sh = client.open('my_coffee')
sheet = sh.sheet1
sheet2 = client.open('my_coffee').worksheet('Sheet1')
sheet3 = client.open('my_coffee').worksheet('Sheet1') 
#---------Connection with Google Sheets--------------------------------------------------

# Kv Design Language. Allows you to create your widget tree in a declarative way and to bind widget properties to each other
root_kv = '''
#:import images_path kivymd.images_path


<MyCard>:
    text: ''
    MDCard:
        padding: 30
        orientation: 'horizontal'
        #pos_hint: {'top': 1}

        Image:
            source: '111.jpg'
            size_hint: None, None
            size: root.width/2, root.height/1.3
            pos_hint: {'top': 1}
        MDLabel:
            theme_text_color: 'Custom'
            text: root.text
            size_hint_x: None
            height: dp(60)
            valign: 'middle'
    Button:
        background_normal: ''
        on_press: root.open_product(self)
        size_hint: (.8,.6)
        pos_hint: ({'center_x': .5,'center_y': .5})
        canvas:
            Clear   

<MySinglCard>:
    MDCard:

<ScreenOne@Screen>:
    name: 'prod_1_screen'
    MyCard:
        text: 'Set of trinkets'.upper()
<ScreenTwo@Screen>:
    name: 'screen two'
    MyCard:
        text: 'Set of trinkets'.upper()
<ScreenThree@Screen>:
    name: 'screen three'
    MyCard:
        text: 'Set of trinkets'.upper()

<MySwiperManager@BoxLayout>:
    orientation: 'vertical'
    size_hint_y: 0.4
    pos_hint: {'top': 1}
    canvas:
        Color:
            rgba: 0, 0, 0, .2
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        padding: dp(10)
        orientation: 'vertical'



<MySmartTileWithStar>:
    text: ''
    discription: ''
    cost: 0
    img: ''
    RelativeLayout:
        SmartTileWithStar:
            id: tile_1
            source: root.img
            on_press: root.open_product(self)
            text: root.text
        MDIconButton:
            icon:'plus'
            text_color: (1,1,1,1)
            user_font_size: 35
            size_hint: (.3,.3)
            on_press: root.add_to_card(self)
            theme_text_color: 'Custom'
            pos: (self.parent.width-self.width/1.4,self.parent.height-self.height/1.4) 

<MyRegistration>:
    Screen:
        name: 'login_screen'
        BoxLayout:
            orientation: 'vertical'
            padding: 100
            Widget:
                size_hint: (None,.2)
            MDTextField:
                id: textfield_mail
                hint_text: 'Mail*'
                font_size: 28
                required: True
            MDTextField:
                id: textfield_pass
                hint_text: 'Password*'
                font_size: 28
                required: True
            Widget:
                size_hint: (None,.2)
            MDRaisedButton:
                text: 'Login'
                font_size: 18
                elevation_normal: 2
                opposite_colors: True
                pos_hint: {'center_x': .5}
                on_press: root.check(self,'main_menu') 
            Widget:
                size_hint: (None,.05)
            MDRaisedButton:
                text: 'Register Now'
                font_size: 18
                elevation_normal: 2
                opposite_colors: True
                pos_hint: {'center_x': .5}
                on_press: root.current ='reg_screen'
    Screen:
        name: 'reg_screen'
        BoxLayout:
            orientation: 'vertical'
            padding: 100
            MDTextField:
                id: textfield_fts_name
                hint_text: 'First Name*'
                required: True
            MDTextField:
                id: textfield_snd_name
                hint_text: 'Second Name*'
                required: True
            MDTextField:
                id: textfield_mail_reg
                hint_text: 'Mail*'
                required: True
            MDTextField:
                id: textfield_pass_reg
                hint_text: 'Password*'
                required: True
            Widget:
                size_hint: (None,.3)
            MDRaisedButton:
                text: 'Register'
                elevation_normal: 2
                opposite_colors: True
                pos_hint: {'center_x': .5}
                on_press: root.register(self,'login_screen')
    Screen:
        name: 'payment_screen'
        BoxLayout:
            orientation: 'vertical'
            padding: 100
            MDTextField:
                id: cardnumber
                hint_text: 'Card Number*'
                required: True
            MDTextField:
                id: adress
                hint_text: 'Adress*'
                required: True
            Widget:
                size_hint: (None,.3)
            MDRaisedButton:
                text: 'Register Payment'
                opposite_colors: True
                pos_hint: {'center_x': .5}
                on_press: root.reg_paymeth()
<MyBottomNavigation@BoxLayout>:
    MDBottomNavigation:
        MDBottomNavigationItem:
            name: 'files1'
            text: 'Shop'
            icon: 'apps'
            
            ScrollView:
                size_hint: (1,.6)
                do_scroll_x: False

                GridLayout:
                    cols: 2
                    row_default_height:
                        (self.width - self.cols*self.spacing[0])/self.cols
                    row_force_default: True
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(4), dp(4)
                    spacing: dp(4)
                    MySmartTileWithStar:
                        text: '   Set of trinkets \\n800T'
                        name: 'prod_1'
                        discription: 'Set of trinkets'
                        cost: int(800)
                        img: '111.jpg'
                    MySmartTileWithStar:
                        text: '   Hand Creams Set\\n1200T'
                        name: 'prod_2'
                        discription: 'Hand Creams Set'
                        cost: int(1200)
                        img: '222.jpg'
                    MySmartTileWithStar:
                        text: '   Refrigerator Magnets\\n450T'
                        name: 'prod_3'
                        discription: 'Refrigerator Magnets'
                        cost: int(450)
                        img: '333.jpg'

        MDBottomNavigationItem:
            name: 'files2'
            text: 'Cart'
            icon: 'basket'
            canvas:
                Color:
                    rgba: 0, 0, 0, .2
                Rectangle:
                    pos: (self.pos[0],self.pos[1]-56)
                    size: self.size
            BoxLayout:
                canvas:
                    Color:
                        rgba: 1, 1, 1, 1
                    Rectangle:
                        pos: (self.pos[0]+20,self.pos[1])
                        size: (self.size[0]-40,self.size[1]-20)
                padding: [60,40,60,40]
                orientation: 'vertical'
                spacing: 20
                MDLabel:
                    id: overall_cost_lb
                    text: 'Cost:  0'
                    size_hint: (1,.1)
                    pos_hint: {'top': 1}
                    font_size: '40sp'
                ScrollView:
                    size_hint: (1,.9)
                    GridLayout:
                        id: BNI_2_bl
                        cols:1
                        row_default_height: 250
                        row_force_default: True
                        size_hint: (1,None)
                        height: self.minimum_height
                MDRaisedButton:
                    name: 'checkout_btn'
                    text: 'Checkout'
                    font_size: 18
                    opposite_colors: True
                    pos_hint: {'center_x': .5}
                    size_hint: (1,.2)
                    on_press: root.checkout()

        MDBottomNavigationItem:
        	name: 'files3'
        	text: 'Account'
        	icon: 'account'
            BoxLayout:
                id: account
                orientation: 'vertical'
                padding: 40
                MDLabel:
                    id: name_lb
                    font_size: 20
                    halign: "center"
                MDLabel:
                    id: mail_lb
                    font_size: 20
                    halign: 'center'
                MDLabel:
                    id: adress_lb
                    font_size: 20
                    halign: 'center'
                MDLabel:
                    id: cardnumber_lb
                    font_size: 20
                    halign: 'center'
                MDRaisedButton:
                    name: 'reg_paymeth_btn'
                    id: btn_paymeth
                    text: 'Register payment method'
                    opposite_colors: True
                    pos_hint: {'center_x': .5}
                    on_press: root.reg_paymeth()

        MDBottomNavigationItem:
        	name: 'files4'
        	text: 'History'
        	icon: 'history'
            BoxLayout:
                id: history
                orientation: 'vertical'
                padding: 40

<MyScreenManager>:
    id: main_sm
    Screen:
        name: 'Reg'
        MyRegistration
            id: mr
    Screen:
        name: 'main_menu'
        MyBottomNavigation:
            id: mbn
'''

# Class which works with ready boxes, allows to open and close screens with them.
class MyCard(FloatLayout):
	# Changes screen to the screen with that product
    def open_product(self,instance):
        self.screen = Screen(name = 'prod')
        self.screen.add_widget(Button(text = instance.text, on_press = self.close))
        self.screen.add_widget(MDCard())
        app.root.add_widget(self.screen)
        app.root.current = 'prod'

    #Changes screen to the main menu
    def close(self,instance):
        app.root.current = 'main_menu'
        app.root.remove_widget(self.screen)

#Class which works with bottom navigation and two registration functions (checkout and reg pay method)
class MyBottomNavigation(BoxLayout):
    def checkout(self):
    	# Takes a number of all orders
        index = int(sheet2.cell(1,2).value)

        ii = False
        # Looking for EMail in the Pay Meth Table, so checks is pay method already registered.
        for i in range(2,index+2):
        	# If pay method is already registered then updates the Pay Meth Table with new information 
            if sheet2.cell(2,i).value == app.root.login:
                ii = True
                sheet3.update_cell(2,int(sheet3.cell(1,2).value)+2,app.root.card)
                sheet3.update_cell(3,int(sheet3.cell(1,2).value)+2,datetime.today().strftime('%d.%m.%y'))
                sheet3.update_cell(4,int(sheet3.cell(1,2).value)+2,app.root.total_cost)
                sheet3.update_cell(5,int(sheet3.cell(1,2).value)+2,str(app.root.list_prods))
                sheet3.update_cell(1,2,int(sheet3.cell(1,2).value)+1)
                break
        if ii != True:
            self.reg_paymeth()

    #If there is no registered pay method then changes screen to Reg Pay method screen
    def reg_paymeth(self):
        app.root.ids.mr.current ='payment_screen'
        app.root.current = 'Reg'

class MyRegistration(ScreenManager):
    def binarySearch(self, array, lft, rgt, x): 
        if rgt >= lft: 
            center = lft + (rgt - lft) // 2
            if array[center] == x: 
                return center 
            elif array[center] > x: 
                return self.binarySearch(array, lft, center-1, x) 
            else: 
                return self.binarySearch(array, center + 1, rgt, x) 
        else: 
            return -1
    def selection_sort(self,array):

        for i in range(len(array)):
            idx = i
            for j in range(i+1, len(array)):
                if array[idx] > array[j]:
                    idx = j
            array[i], array[idx] = array[idx], array[i]

    def check(self,instance,nxt_screen):
        #app.root.current = nxt_screen
        main_form = app.root.ids.mbn

        #List with all email from Clients Table
        list_of_logins = []
        d_arr_log_pass = []
        for i in range(2,int(sheet.cell(1,2).value)+2,1):
            list_of_logins.append(sheet.cell(3,i).value)
            for j in range(2,int(sheet.cell(1,2).value)+2,1):
                d_arr_log_pass.append([sheet.cell(4,i).value,sheet.cell(5,i).value])
        #Sorting the list
        self.selection_sort(list_of_logins)
        # Find the index of Clients Colum in the Clients Table
        index = self.binarySearch(list_of_logins, 0, len(list_of_logins), self.ids.textfield_mail.text) 

        # Verify the Email and Password. If they are correct, updates the account screen
        if sheet.cell(5,index).value == self.ids.textfield_pass.text:
            app.root.login = self.ids.textfield_mail.text
            main_form.ids.name_lb.text = "Name: " + sheet.cell(2,index).value + sheet.cell(3,index).value
            main_form.ids.mail_lb.text = "Mail: " + sheet.cell(5,index).value

            app.root.current = nxt_screen
        elif index == -1:
            from kivymd.toast.kivytoast import toast
            toast('No user with this Email!')

        else:
        	# If Email or Password are incorrect shows a warn text
            from kivymd.toast.kivytoast import toast
            toast('Some Error - Incorrect Email or Password!')


        index = int(sheet2.cell(1,2).value)
        iii = False
        # Checks the registration of pay method
        for i in range(2,index+2,1):
            # If pay method is registred then updates the account
            # Shows the Address, Card Number, and removes the Reg Pay Meth button
            if sheet2.cell(2,i).value == app.root.login:

                main_form.ids.adress.text = "Adress: " + sheet2.cell(3,i).value
                app.root.card = sheet2.cell(4,i).value
                main_form.ids.cardnumber_lb.text = "Card Number: " + app.root.card
                main_form.ids.account.remove_widget(app.root.ids.mbn.ids.btn_paymeth)
                iii = True

        if iii != True:
            # If there is no registered pay method, removes the labels with Address and Card Number
            main_form.ids.account.remove_widget(self.ids.adress_lb)
            main_form.ids.account.remove_widget(self.ids.cardnumber_lb)

        ind = 0
        #Checks history table. If find mathcing card number then shows order's detail on the history screen
        for i in range(2,index+2,1):
            if sheet3.cell(2,i).value == app.root.card:
                ind += 1
                text = 'Order #%i  '%ind + sheet3.cell(3,i).value + ' ' + sheet3.cell(4,i).value + ' ' + sheet3.cell(5,i).value
                app.root.ids.mbn.ids.history.add_widget(MDLabel(id = 'prod%i'%i, font_size = 20, text = text, halign = "center"))

    def register(self,instance,nxt_screen):

        index = int(sheet.cell(1,1).value)
        # List of special chars for validation
        spec_chars = '0123456789-_=+.,!'
        # Variables which shows which of input data is correct
        email_suitable, name_suitable, passw_suitable = False, False, False

        #Data from text inputs in the register form
        name = self.ids.textfield_fts_name.text
        s_name = self.ids.textfield_snd_name.text
        mail = self.ids.textfield_mail_reg.text
        passw = self.ids.textfield_pass_reg.text

        #Checks the EMail for valid value
        if mail.find('@') == -1:
            email_suitable = False
        else:
            for i in range(index):
                if mail == sheet.cell(4,i+1).value:
                    print('@')
                    email_suitable = False
                    break
                else:               
                    email_suitable = True

        #Checks the name and sceond name for valid value
        for i in range(17):
            if  name.find(spec_chars[i]) != -1 or s_name.find(spec_chars[i]) != -1:
                name_suitable = False
                break
            else: 
                name_suitable = True

        #Checks the password for valid value
        if len(passw) < 8:
            print('p')
            passw_suitable = False
        else:
            passw_suitable = True

        # Checks if all data is valid. If yes, so saves data and changes screen to login screen
        if email_suitable == True and name_suitable == True and passw_suitable == True:
            sheet.update_cell(3,index+1,name)
            sheet.update_cell(4,index+1,s_name)
            sheet.update_cell(5,index+1,mail)
            sheet.update_cell(6,index+1,passw)
            sheet.update_cell(1,1,index+1)
            self.current = nxt_screen

    def reg_paymeth(self):
    	# Updates Pay Method Table 
        index = int(sheet2.cell(1,2).value)+1
        sheet2.update_cell(1,2,index)
        sheet2.update_cell(2,index+1,app.root.login)
        sheet2.update_cell(3,index+1,self.ids.adress.text)
        sheet2.update_cell(4,index+1,self.ids.cardnumber.text)

        # Creates two labels on the account screen with Address and Card Number
        main_form = app.root.ids.mbn
        main_form.ids.account.add_widget(MDLabel(id = 'adress', font_size = 20, text = "Adress: " + self.ids.adress.text, halign = "center"))
        main_form.ids.account.add_widget(MDLabel(id = 'cardnumber', font_size = 20, text = "Card Number: " + self.ids.cardnumber.text, halign = "center"))
        app.root.ids.mbn.ids.account.remove_widget(app.root.ids.mbn.ids.btn_paymeth)
        app.root.current = 'main_menu'

class MySmartTileWithStar(BoxLayout):
	# Opens the screen with product
    def open_product(self,instance):
        self.screen = Screen(name = 'prod')
        self.screen.add_widget(Button(text = instance.text, on_press = self.close))
        app.root.add_widget(self.screen)
        app.root.current = 'prod'

    # Returns the user to the main menu
    def close(self,instance):
        app.root.current = 'main_menu'
        app.root.remove_widget(self.screen)

    # Adds the products to the basket, creates the SmartTileWithLabel on the checkout screen and changes the overall cost
    def add_to_card(self,instance):
        b_prod = BoxLayout(orientation = 'horizontal')
        b_prod.add_widget(SmartTileWithLabel(text = self.text, source = self.img, size_hint=(1,1)))
        b_text_icon = StackLayout()
        b_text_icon.add_widget(MDLabel(text = self.text,size_hint_y=.8))
        b_text_icon.add_widget(Widget(size_hint_x=.7))
        b_text_icon.add_widget(MDIconButton(icon = 'delete', user_font_size=35, on_press = self.del_from_card, size_hint_y=.2))
        b_prod.add_widget(b_text_icon)
        app.root.ids.mbn.ids.BNI_2_bl.add_widget(b_prod)
        app.root.total_cost += int(self.cost)
        app.root.list_prods.append(self.name)
        app.root.ids.mbn.ids.overall_cost_lb.text = 'Cost: ' + str(app.root.total_cost)

    # Removes the product from basket, removes the SmartTileWithLabel from the checkout screen and changes the overall cost
    def del_from_card(self,instance):
        app.root.ids.mbn.ids.BNI_2_bl.remove_widget(instance.parent.parent)
        app.root.total_cost -= int(self.cost)
        app.root.list_prods.remove(self.name)
        app.root.ids.mbn.ids.overall_cost_lb.text = 'Cost: ' + str(app.root.total_cost)

class MyScreenManager(ScreenManager):
    pass

# Main class is basic of programm which contains the all objects
class MainApp(MDApp):
    # System configuration and title with theme of programm
    def __init__(self, **kwargs):
        self.title = 'GiftBoxes for everone!'
        self.theme_cls.primary_palette = 'Indigo'
        super().__init__(**kwargs)

    def build(self):
    	# connects the KV Language block with Python Code
        Builder.load_string(root_kv)
        # Creates main screen manager
        start_menu = MyScreenManager()
        # Assigns the screen maneger to the root property of Main class (MainApp)
        self.root = start_menu
        self.root.total_cost = 0
        self.root.login = ''
        self.root.card = ''
        self.root.list_prods = []

app = MainApp()
# Run the programm
if __name__ == '__main__':
    app.run()