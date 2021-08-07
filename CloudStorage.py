import os
import dropbox
from dropbox.files import WriteMode
#
class TransferData:
    def_ init_(self,access_token)
        self.access_token = access_token
 #
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self,access_token)

            #enumerate loacal files recursively
        for root,dirs,files in os.walk(files_from)

            for filename in files:
                    #construct the full local path
                local_path = os.path.join(root, filename)


                    #construct the full Dropbox path
                relatives_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(files_to,  relatives_path)
                    # upload the files
                with opn(local_path,'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
        access_token = 'xzI3Q2_H6nMAAAAAAAAAAeTD0RA_2o4QB0dJjeItlvtOz-OoE6EcsABjppji4TLd'
        transferData = transferData(access_token)

        file_from = str(input("Enter the folder path to transfer : -"))
        file_to = input("enter the full path to upload to dropbox:- ") # this is the full path to upload the file to,including name that you wish the file to be called once upload


        #API v2 
        transferData.upload_file(file_from,file_to)
        print("file has been removed!!!")
        main()
