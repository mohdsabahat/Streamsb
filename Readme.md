![Work in Progress](https://i.ibb.co/bHB3crc/banner.png)
# Unofficial Streamsb Api
### unofficial Python wrapper for [Streamsb Api](https://support.streamsb.com/docs). Streamsb is a Video hosting website which provides unlimited storage.
---
## Install
```
Pip package coming Soon
```

---
## Usage
import the client class and create Client object, it requires an Api Key as its only parameter.
You may get an API key from [Streamsb Site](https://streamsb.com/?op=my_account)
```python
from streamsb import Client
client = Client('Your_API_Key')
```
Client class has the attributes for four different functions mainly
- account realted methods under account attribute
- file related methods under file attribute
- folder related method under folder attribute
- upload related methods under upload attribute
---
## Detailed Use
Each method call returns a Object which has a "raw" attribute which contains the json response of the request if it was successful.
- To get Account info.
```python
acc_info = client.account.info()
acc_info
# AccountInfo Object, which may contain the following attributes.
{
          "raw": "It contains raw API response of this AccountInfo Object."
          "email": "myemail@gmail.com",
          "balance": "0.00000",
          "storage_used" :"24186265",
          "storage_left": 128824832615,
          "premim_expire": "2020-01-20 21:00:00
}
```
It will return an AccountInfo object which has a "raw" attribute which contains the json response of the request.
All other attributes of this object are the values in "raw['result']".
- To get Account Stats.
```python
acc_stats = client.account.stats()
acc_stats.stats
# List of Stat objects
# Attributes of Stat object can be
{
            "raw": "It contains raw API response of this Stat Object."
            "downloads": "0",
            "profit_views": "0.00000",
            "views_adb": "1",
            "sales": "0",
            "profit_sales": "0.00000",
            "profit_refs": "0.00000",
            "profit_site": "0.00000",
            "views": "0",
            "refs": "0",
            "day": "2020-08-01",
            "profit_total": "0.00000",
            "views_prem": "0"
}
```
It will return an AccountStat object, whose stats attribute is a list of Stat objects.
Each stat object contains the raw json response of request and all the attributes of the response.
- To get File Info.
```python
file = client.file.info(filecode = "File code")
file
# List of FileInfo objects which may contain attributes.
{
            "raw": "raw json response"
            "status": 200
            "filecode": "jthi5jdsu8t9" 
            "last_download": datetime.datetime object
            "canplay": bool value
            "public": bool value
            "length": duration of file (int)
            "title": "File Title"
            "views": "file views (int)
            "name": "file name (str)"
            "created": datetime.datetime Object
            #These fields are not document but seen in some responses.
            "full_views": (int)
            "cat_id": "category id (int)"
            "player_img": "video player image (str)
```
It will return a list of FileInfo object, and each object may contain the attributes as above.
- To rename a file.
```python
response = client.file.rename(filecode = "File code", title = "New Title", name = "New name" [optional])
response 
# Returns True if response is successful otherwise raises APIResponse error. 
```
- To clone a file.
```python
file = client.file.clone(filecode = "File Code")
file
# Returns a File object.
{
         "raw": "raw Json response"
         "filecode": "file code"
         "url": "streamsb url of file"
}
```
It returns a File object which may contain the above attributes.
- To List/Search files.
```python
files = client.file.list(filter = {}[optional])
# Filter is a dict which may have following keys
{
        "title": "title to look for"
        "page" : "page no. for pagination:
        "per_page": "no. of items per page"
        "folder_id": "folder id"
        "public": True to list public files, False for private
        "created": datetime.datetime object
}
```
- To get all direct links (Premium only).
```python
qualities = client.file.direct_all(filecode = "file code")
qualities
# Returns a dict of Quality object
# each dict key can have values ['l','n','h','o']
{
        "l": Quality(),
        "n": Quality()
}
# Each Quality object has attributes
{
        raw: "raw json response"
        url: "url of video"
        size : "size of video (int)"
}
```
