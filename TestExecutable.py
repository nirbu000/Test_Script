import subprocess
import requests


url = 'http://is-hw.getsandbox.com/test/'
header = {"Content-Type": "text/plain", "API-Key": "api-6cf4ee44-6284-418c-b4f4-8284869d6588"}


def is_vs_av():
    exename = 'iS.exe'
    successFlag = True
    for i in range(1, 11):
        avName = 'AV{0}.exe'.format(i)
        result = subprocess.call(['C:\AV\/' + avName, '.\Test\bin\Debug\/' + exename])
        if result == 0:
            response = requests.put(url + avName + '/' + exename, data="Test with {0}".format(avName), headers=header, params={'flagged': 'false'})
            print(response)
        else:
            response = requests.put(url + avName + '/' + exename, data="Test with {0}".format(avName), headers=header, params={'flagged': 'true'})
            print(response)
            successFlag = False

    if successFlag == False:
        raise Exception('flagged!')


is_vs_av()
