![EasyPyGen](/pass.png)

**EasyPyGen** is a small Python script that will help you with your password bruteforce journey.

This script will allow you to generate an advanced targeted worldlist in a very simple way.

  

## Why use it?

**EasyPyGen** uses a config file which contain a bunch of password patten which you can add more into, meaning that you can almost generate any password pattern you want without getting you hand dirty with code. 

##  How to use

### usage : 

 `app.py --extend names.txt  --output myWordlist.txt`

--extend  : the list of words or name you want to extend

--output : name of the generated wordlist 

> i already provided a list of arabic names almsot all the popular ones in the `/data` folder

Example : ``exnted.conf``

```

{name}@[0-9]

```

Generated :

```

mike@2015

MIKE@2015

mike@2016

MIKE@2016

...

MIKE@2021

mike@2022

MIKE@2022

```




-You could also loop through symbols by putting them in a list/array like format : 




Example : ``exnted.conf``

```

{name}[@,#,$][0-5]

```

Generated :

```

mike@0

MIKE@0

mike#0

...

MIKE@5

mike#5

MIKE#5

mike$5

MIKE$5

```

 - Empty lines will be ignored as well as lines that stars with "#"

> 🚧 Work in progress (contributions welcome!).

  