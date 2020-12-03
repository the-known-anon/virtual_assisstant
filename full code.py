import wx
import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver # to control browser operation
import sys
import subprocess


num = 1
def assistant_speaks(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
    file = str(num)+".mp3"  
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 
    def process_text(input): 
    try: 
        if 'search' in input or 'play' in input: 
            # a basic web crawler using selenium 
            search_web(input) 
            return
  
  
        elif "calculate" in input.lower(): 
              
            # write your wolframalpha app_id here 
            app_id = "PR8V5V-YAP8KWTJLK" 
            client = wolframalpha.Client(app_id) 
  
            indx = input.lower().split().index('calculate') 
            query = input.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            assistant_speaks("The answer is " + answer) 
            return
  
        elif 'open' in input: 
              
            # another function to open  
            # different application availaible 
            open_application(input.lower())  
            return
  
        else: 
  
            assistant_speaks("I can search the web for you, Do you want to continue?") 
            ans = get_audio() 
            if 'yes' in str(ans) or 'yeah' in str(ans): 
                search_web(input) 
            else: 
                return
    except : 
  
        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
        ans = get_audio() 
        if 'yes' in str(ans) or 'yeah' in str(ans): 
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query))  
            def search_web(input): 
  
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    driver = webdriver.Chrome(options=options)
    driver.get('https://python.org')
    driver.implicitly_wait(1) 
    driver.maximize_window() 
  
    if 'video' in input(): 
  
        assistant_speaks("Opening in youtube") 
        indx = input.lower().split().index('youtube') 
        query = input.split()[indx + 1:] 
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
        return
  
    elif 'who is' in input(): 
  
        assistant_speaks("Opening Wikipedia") 
        indx = input.lower().split().index('wikipedia') 
        query = input.split()[indx + 1:] 
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
        return
  
    else: 
  
        if 'google' in input: 
  
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        elif 'search' in input: 
  
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        else: 
  
            driver.get("https://www.google.com/search?q =" + '+'.join(input.split())) 
  
        return
  
  
 # function used to open application 
# present inside the system. 
def open_application(input): 
  
    if "chrome" in input: 
        assistant_speaks("Google Chrome") 
        subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
        return
  
    elif "firefox" in input or "mozilla" in input: 
        assistant_speaks("Opening Mozilla Firefox") 
        subprocess.Popen('C:\Program Files\Mozilla Firefox\\firefox.exe') 
        return
  
    elif "notepad" in input: 
        assistant_speaks("Opening notepad") 
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
        return
  
    elif "excel" in input: 
        assistant_speaks("Opening Microsoft Excel") 
        subprocess.Popen('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk') 
        return
  
    else: 
  
        assistant_speaks("Application not available") 
        return
    class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Key Press Tutorial")
 
        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        btn = wx.Button(panel, label="OK")
        btn.Bind(wx.EVT_KEY_DOWN, self.onKeyPress)
        
    def onKeyPress(self, event):
        keycode = event.GetKeyCode()
        print keycode
        if keycode == wx.WXK_SPACE:
            
        event.Skip()
    
# Run the program
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm()
    frame.Show()
    app.MainLoop()
