import time
import os
import shutil

def removefile():
    
    dfoldc=0
    dfilec=0
    
    days=30
    
    path="./delicon"
    
    seconds=time.time() - (days*24*60*60)
    
    if os.path.exists(path):
        
        for root_folder,folder,files in os.walk(path):
            
            if seconde >= getffa(root_folder):
                
                remove_folder(root_folder)
                dfoldc += 1
                
                break
            
            else:
                
                for folder in folders:
                    
                    folder_path = os.path.join(root_folder, folder)
                    
                    if seconde >= getffa(folder_path):
                        
                        remove_folder(folder)
                        dfoldc += 1
                        
                    
                for file in files:
                    
                    file_path = os.path.join(root_folder, file)
                    
                    if seconds >= getffa(file_path):
                        
                        remove_file()
                        dfilec += 1
 
        else:
            
            if seconds >= getffa(path):
                
                remove_file(path)
                dfilec += 1                
    
    else:
        
        print(f'"{path}" is not found')
        dfilec += 1

    print(f"total folders deleted: {dfoldc}")
    print(f"total files deleted: (dfilec)")    
