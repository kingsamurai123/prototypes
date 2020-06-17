import requests
import shutil

image_url = "paste_your_image_url_here"
filename = image_url.split("/")[-1]

r = requests.get(image_url, stream = True)

if r.status_code == 200:
    r.raw.decode_content = True
    
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
        
    print("Image is succesfully downloaded: ",filename)
else:
    print("Image could not be downloaded") 
