import cv2
import dropbox
import time
import random
start_time=time.time()

def take_snapshot():
    videoCaptureObject=cv2.VideoCapture(0)
    number=random.randint(0,100)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time()
        result=False
    return image_name
    print("Snapshot taken.")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_token="sl.BImeHTB5v1t5SFdMqXAzfxr9Z9YXSXXIYpWE-FN-MfscM9A3Dw8jN2GT2_ITTTR2hhE4zRZxA8RHQYJnJDA6BDPPVipSs-IniseP-awTWp4ztcP0lWvLgGXSpcO538KQxS6aMOaNTq1g"
    file=image_name
    file_from=file
    file_to="/testFolder/"+(image_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f :
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time()-start_time>=5)):
            name=take_snapshot()
            upload_file(name)

main()



    
    
