import os,sys,fnmatch
def get_filename():
    file_name=raw_input("Enter the file name: ")
    return file_name
def find_file(file_name,path):
    result=[]
    for root,dir,files in os.walk(path):
        for name in files:
         if fnmatch.fnmatch(name,file_name):
             result.append(os.path.join(root,name))
    return result

     
def main():
   get_name = get_filename()
   print(find_file(get_name,'/'))

if __name__ == "__main__": 
    main()