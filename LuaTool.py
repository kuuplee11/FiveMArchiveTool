import os

def main():

    print("""
$$\   $$\ $$\   $$\ $$$$$$$\  $$\       $$$$$$$$\                     $$$$$$$$\  $$$$$$\   $$$$$$\  $$\       
$$ | $$  |$$ |  $$ |$$  __$$\ $$ |      $$  _____|                    \__$$  __|$$  __$$\ $$  __$$\ $$ |      
$$ |$$  / $$ |  $$ |$$ |  $$ |$$ |      $$ |                             $$ |   $$ /  $$ |$$ /  $$ |$$ |      
$$$$$  /  $$ |  $$ |$$$$$$$  |$$ |      $$$$$\          $$$$$$\          $$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$  $$<   $$ |  $$ |$$  ____/ $$ |      $$  __|         \______|         $$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$ |\$$\  $$ |  $$ |$$ |      $$ |      $$ |                             $$ |   $$ |  $$ |$$ |  $$ |$$ |      
$$ | \$$\ \$$$$$$  |$$ |      $$$$$$$$\ $$$$$$$$\                        $$ |    $$$$$$  | $$$$$$  |$$$$$$$$\ 
\__|  \__| \______/ \__|      \________|\________|                       \__|    \______/  \______/ \________|                                                          
    """ )   


    parent_dir = input("Pon el directorio donde quires crear la carpeta: ")
    directory = input("Pon el nombre del script: ")

    mainsv = "main.lua"
    maincl = "main.lua"
    configlua = "config.lua"
    mainfestlua = "fxmainfest.lua"

    path = os.path.join(parent_dir, directory)
    clside = os.path.join(parent_dir, directory, "Client")
    svside = os.path.join(parent_dir, directory, "Server")
    svsidelua = os.path.join(parent_dir, directory, "Server", mainsv)
    clsidelua = os.path.join(parent_dir, directory, "Client", maincl)
    config = os.path.join(parent_dir, directory, configlua)
    mainfest = os.path.join(parent_dir, directory, mainfestlua)

    try:
        os.mkdir(path)
        os.mkdir(clside)
        os.mkdir(svside)
        fsv = open(svsidelua, 'w')
        fsv.write("-- Archivo Server.lua Creado Por La KUPLE-TOOL")    
        fsv.close()
        fcl = open(clsidelua, 'w')
        fcl.write("-- Archivo Client.lua Creado Por La KUPLE-TOOL")
        fcl.close()
        fcf = open(config, 'w')
        fcf.write("-- Archivo Config.lua Creado Por La KUPLE-TOOL")
        fcf.close()
        fm = open(mainfest, 'w')
        fm.write("-- Archivo FxMainfest.lua Creado Por La KUPLE-TOOL")
        fm.close()



        print("Directory " , directory ,  " Created ") 
    except FileExistsError:
        print("Directory " , directory , " allready Exists ")

if __name__ == "__main__":
    main()