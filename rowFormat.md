# Description of joson about rowFormat 
## Format
```
{ Key:[Columns],,, }
```

## Columns
### 1st : Data Type
dt = date
i=integer
f=float

### 2nd : Generate Method
* s=series
* r=random
* c=calculated

### 3rd 
#### min
* if type is float or integer or date

#### Start
* if Generate Method is series

### 4th 
#### max
* if type is float or integer

#### next value gap
* if Generate Method is series

### 5th 
#### precision
* if type is float or integer

### 6th : equation
* if type is calculated
* ex) "(key1+key2)*key3"
