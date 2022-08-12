!(Work in Progress)[https://i.ibb.co/bHB3crc/banner.png]
# Unofficial Streamsb Api
---
!(Streamsb Api)[https://streamsb.com/streamSB_images/logo.png]
---
Unofficial Python wrapper for (Streamsb Api)[https://support.streamsb.com/docs]
Streamsb is a Video hosting website which providea unlimited storage.
---
## Install
```
Pip package coming Soon
```

---
## Usage
import the client class and create Client object, it requires an Api Key as its only parameter.
You may get an API key from (Streamsb Site)[https://streamsb.com/?op=my_account]
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
```
It will return an AccountInfo object which has a "raw" attribute which contains the json response of the request.
All other attributes of this object are the values in "raw['result']".
- To get Account Stats.
```python
acc_stats = client.account.stats()
acc_stats.stats
#List of Stat objects
```
It will return an AccountStat object, whose stats attribute is a list of Stat objects.
Each stat object contains the raw json response of request and all the attributes of the response.
- To get File Info.
```python
file = client.file.info()
```

