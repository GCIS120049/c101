import dropbox
import os
from dropbox.files import WriteMode

class TransferData :

    def __init__( self , access_token ) :
        self.access_token = access_token

    def uploadFile( self , file_from , file_to ) :

        dbx = dropbox.Dropbox( self.access_token )

        for root , dirs , files in os.walk( file_from ) :

            for fileName in files:

                localPath = os.path.join(root,fileName)
                relativePath = os.path.relpath(localPath,file_from)
                dropboxPath = os.path.join(file_to,relativePath)

                with open(localPath,'rb')as f:
                    dbx.files_upload(f.read(),dropboxPath,mode = WriteMode('overwrite'))

def main() :

    access_token = 'eP9re7BseI4AAAAAAAAAAQ87HFtUOiRLBPQhiS0Z1DQd_LNaPZordeR7FoKB4OxK'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer"))
    file_to = input("Enter the full path to upload to dropbox")

    transferData.uploadFile(file_from,file_to)
    print("file has been moved")

main()