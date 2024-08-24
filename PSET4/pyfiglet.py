import sys,pyfiglet


figlet=pyfiglet.Figlet()
if len(sys.argv)!=3 and len(sys.argv)!=1:
    sys.exit("Invalid Usage")
elif len(sys.argv)==3 and sys.argv[1] not in ("-f","--font"):
    sys.exit("Invalid Usage")
if len(sys.argv)==3:
    f=sys.argv[2]
    figlet.setFont(font=f)
s=input("Input: ")
print(figlet.renderText(s))
