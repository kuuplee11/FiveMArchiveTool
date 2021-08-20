import os

def main():

    print("""
$$\   $$\ $$\   $$\ $$$$$$$\  $$\       $$$$$$$$\   
$$ | $$  |$$ |  $$ |$$  __$$\ $$ |      $$  _____|       
$$ |$$  / $$ |  $$ |$$ |  $$ |$$ |      $$ |              
$$$$$  /  $$ |  $$ |$$$$$$$  |$$ |      $$$$$\ 
$$  $$<   $$ |  $$ |$$  ____/ $$ |      $$  __|     
$$ |\$$\  $$ |  $$ |$$ |      $$ |      $$ |      
$$ | \$$\ \$$$$$$  |$$ |      $$$$$$$$\ $$$$$$$$\ 
\__|  \__| \______/ \__|      \________|\________|                                                      
    """)   


    maindir = input("Put the directory where you want to create the folder: ")
    directory = input("Put the main folder name: ")

    mainsv = "main.lua"
    maincl = "main.lua"
    configlua = "config.lua"
    mainfestlua = "fxmainfest.lua"

    path = os.path.join(maindir, directory)
    clside = os.path.join(maindir, directory, "Client")
    svside = os.path.join(maindir, directory, "Server")
    svsidelua = os.path.join(maindir, directory, "Server", mainsv)
    clsidelua = os.path.join(maindir, directory, "Client", maincl)
    config = os.path.join(maindir, directory, configlua)
    mainfest = os.path.join(maindir, directory, mainfestlua)

    try:
        os.mkdir(path)
        os.mkdir(clside)
        os.mkdir(svside)

        fsv = open(svsidelua, 'w')
        fsv.write("-- File Server.lua Created By FiveM Acrhive Tool")    
        fsv.close()

        fcl = open(clsidelua, 'w')
        fcl.write("-- File Client.lua Created By FiveM Acrhive Tool")
        fcl.close()

        fcf = open(config, 'w')
        fcf.write("-- File Config.lua Created By FiveM Acrhive Tool")
        fcf.close()
        
        fm = open(mainfest, 'w')
        fm.write("-- File FxMainfest.lua Created By FiveM Acrhive Tool")
        fm.close()



        print("Folder " , directory ,  " Created ") 
    except FileExistsError:
        print("Folder " , directory , " allready Exists ")

if __name__ == "__main__":
    main()
