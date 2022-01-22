import webbrowser, sys, time, pyperclip, requests, bs4
"""
hovevei zion tel aviv
"""
if(len(sys.argv)>1):
    address = ' '.join(sys.argv[1:])
    print("address is:  "+address)
else:
    address = pyperclip.paste()
    print("address from clipboard:  "+address)

time.sleep(1.2)
webbrowser.open("https://www.google.com/maps/place/{}/".format(address))
webbrowser.open("http://automatetheboringstuff.com/files/rj.txt")
 hey = 'hey'