=============
Pypedrive
=============

Just an approach using requests for python-pipedrive library by @jscott1989
with new features.


Installing
-------------

Clone this repo or use pip command:  
$ pip install pypedrive


Using
-------------

Python Code:

from pypedrive import Pypedrive

pipedrive = Pypedrive('AUTH_TOKEN')

# Creating organizations, deals, person ...
pipedrive.organizations({  
    'method': 'POST',  
    'name': 'Organization inc.',  
    'phone': '(12) 1231-1412',  
    ...  
})

# You can use lists to update or exclude a bunch of information
pipedrive.persons({  
    'method': 'DELETE',   
    'id': [1,2,3]  
})



For more information about how to use Pipedrive's API, [click here](https://developers.pipedrive.com/v1).
