## FilesFormat

### Sofware

[Get the last version of the source here](https://github.com/PythonForChange/FilesFormat/blob/main/pfcf.py)


### Installation

:D Under construction 🛠️.

### Usage

:D Under construction 🛠️.
Include screenshots of the project in action.


Import the modules.
```python
from pfcf import *
import json, os
```
 
```python
l=LogFile("log1")
l.row("hello[") #this [ can not be printed
l.row("world\"") #this " can not be printed
l.section() #break
l.row("hello"+l.vip("[")) #this [ can be printed
l.row("world"+l.vip("\"")) #this " can be printed
l.section() #break
l.row("by Eanorambuena"+l.den("this text can not be printed"))
l.read()
```
 
log1_0.pfcf

```pfcf
hello[,world",|hello\[,world\",|by Eanorambuena~t~h~i~s~ ~t~e~x~t~ ~c~a~n~ ~n~o~t~ ~b~e~ ~p~r~i~n~t~e~d,
```

hello
world

hello[
world"

by Eanorambuena



    clients: 
        
            first_name: Sigrid

            last_name: Mannock

            age: 27

            amount: 7.17
        

        
            first_name: Joe

            last_name: Hinners

            age: 31


            amount: 
                1.9

                5.5
            
        

        
            first_name: Theodoric

            last_name: Rivers

            age: 36

```python
l.reset()
l.p.den=":"
l.row(l.den("this text can not be printed"))
l.read()
```
 
log1_1.pfcf

```pfcf
:t:h:i:s: :t:e:x:t: :c:a:n: :n:o:t: :b:e: :p:r:i:n:t:e:d,
```

log1_hist.pfcf

```pfcf
0
1
```


```python
l.h.reset()
```

```python
data = {}
data['clients'] = []
data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})
data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})
data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})
l2=LogFile("log2")
l2.fromDict(data)
```
log2.json
```json
{
    "clients": [
        {
            "first_name": "Sigrid",
            "last_name": "Mannock",
            "age": 27,
            "amount": 7.17
        },
        {
            "first_name": "Joe",
            "last_name": "Hinners",
            "age": 31,
            "amount": [
                1.9,
                5.5
            ]
        },
        {
            "first_name": "Theodoric",
            "last_name": "Rivers",
            "age": 36,
            "amount": 1.11
        }
    ]
}
```
