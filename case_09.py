import webbrowser
#pip install webbrowser
dir(webbrowser)

#Open URL in a new tab:
webbrowser.open_new_tab('http://www.csestack.org') 

#Open URL in new browser window:
webbrowser.open_new('http://www.csestack.org')

#Opening URL in specific browser, let’s say in Firefox and Chrome:
webbrowser.get('firefox').open_new_tab('http://www.csestack.org')
#Opens URL in Firefox browser
 
webbrowser.get('chrome').open_new_tab('http://www.csestack.org')
#Opens URL in Chrome browser

#Opening URL in Default Browser:
#Assigning URL to be opened
strURL = "http://www.csestack.org"
#Open url in default browser
webbrowser.open(strURL, new=2)

#If new = 0, open URL in same browser window
#If new = 1,  opens URL in new browser window
#If new = 2, open URL in same tab.