from __future__ import print_function
import pickle
import os.path
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload


SCOPES = ['https://www.googleapis.com/auth/drive']

class SaveDownloadDrive():

    def __init__(self):
        creds = None
        if os.path.exists('config/token.pickle'):
            with open('config/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('config/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('config/token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        self.service = build('drive', 'v3', credentials=creds)

    def downloadFiles(self,path):
        results = self.service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
            print('Files:')
            counter = 0
            for item in items:
                #print(u'{0} ({1})'.format(item['name'], item['id']))
                file_id = item['id']
                fileName= path+'/'+item['name']
                request = self.service.files().get_media(fileId=file_id)
                fh = io.FileIO(fileName, 'wb')
                print('patch', path+item['name'])
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    print("Download %d%%." % int(status.progress() * 100))
                counter += 1
            print('Downloaded:', counter, "files")
            return str(counter)


    def saveFile(self,filename):
        name = os.path.basename(filename)
        print('name', name)
        file_metadata = {'name': name}
        print('filename', filename)
        media = MediaFileUpload(filename)
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print('Upload:', name)
        return True
