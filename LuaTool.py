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

    cl = 'Client'
    sv = 'Server'
    
    # mainsv = open('main.lua', 'w')
    # maincl = open('main.lua', 'w')
    # configlua = open('config.lua', 'w')
    # mainfestlua = open('fxmainfest.lua', 'w')

    path = os.path.join(parent_dir, directory)
    clside = os.path.join(parent_dir, directory, cl)
    svside = os.path.join(parent_dir, directory, sv)

    # svsidelua = os.path.join(parent_dir, directory, sv, mainsv)
    # clsidelua = os.path.join(parent_dir, directory, cl, maincl)
    # config = os.path.join(parent_dir, directory, configlua)
    # mainfest = os.path.join(parent_dir, directory, mainfestlua)

    try:
        os.mkdir(path)
        os.mkdir(clside)
        os.mkdir(svside)
        # os.mkdir(svsidelua)
        # os.mkdir(clsidelua)
        # os.mkdir(config)
        # os.mkdir(mainfest)

        print("Directory " , directory ,  " Created ") 
    except FileExistsError:
        print("Directory " , directory , " allready Exists ")

if __name__ == "__main__":
    main()