import webbrowser

res=input("Do you want to read the article say YES/NO:")
if res=='Y':
    url="https://en.wikipedia.org/wiki/Special:Random"
    webbrowser.open_new(url)

else:
    if res=='N':
        print("Thanks for visiting!!!")
    else:
        print("Invalid voice")
