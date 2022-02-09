# AppSRepo
Applications repository for AppS  

# AppSI Syntax
This app manager uses AppSI files for app configuration. The syntax is pretty simple. First you type the application name. It can contain spaces.  
Then write down the application description. Try to fit it in one line, otherwise other things will break.
Next thing to do is to write down the type. If the app is a game, type /GAME/. Otherwise type /NAPP/. Remember to type everything after a newline!  
Now you need to describe the executable. From a new line, write down the path. For example, I have my game folder and it's called MySuperGame. I have an executable file in it called MSGExecutable.exe. So i write down MSGExecutable.exe. Or, if you have the executable located in a subfolder like MySuperGame/binaries/MSGExecutable.exe, write down binaries/MSGExecutable.exe.  
And for the last part, write down the app arguments to add when launching. If there is no arguments, leave an empty line.  

Example file:  

My Super Game  
This is a very good game like you should really play it it's soooooo good.  
/GAME/  
binaries/MSGExecutable.exe  
(this is an empty line)  

It's really important to write down the AppSI file with correct syntax. Remember that if it isn't correct, I will not accept it into the store.
