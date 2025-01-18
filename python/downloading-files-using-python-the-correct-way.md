# Downloading files using python the correct way



```python
# determine the type of file over network
res = urllib.request.urlopen(url)
# get file content type (jpeg, pdf etc)
file_type = res.info().get_content_subtype()
# filename ofc
file_name = res.info().get_filename()
# assuming file_name contains file extension as well
# otherwise use file_type and name together
urllib.request.urlretrieve(url, file_name)

```
