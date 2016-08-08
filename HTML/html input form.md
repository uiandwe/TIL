#http://devproconnections.com/html5/html5-form-input-enhancements-form-validation-css3-and-javascript

```
<form> <!-- action & method attributes supplied by developer -->
    <label for="name">Name</label>
    <input id="name" name="name" type="text" /> 
    <label for="email">Email</label>
    <input id="email" name="email" type="text" /> 
    <label for="site">Site</label>
    <input id="site" name="site" type="text" /> 
    <label for="phone">Phone</label>
    <input id="phone" name="phone" type="text" /> 
    <input id="submit" name="submit" type="submit" 
     value="Send Data" /> 
</form>
```

![http://devproconnections.com/site-files/devproconnections.com/files/uploads/2013/11/Palermo%20DCM405%20Figure%202.jpg](http://devproconnections.com/site-files/devproconnections.com/files/uploads/2013/11/Palermo%20DCM405%20Figure%202.jpg)
```
<input id="email" name="email" type="email" 
 placeholder="name@domain.com"/>
<input id="site" name="site" type="url" 
 placeholder="http://www.yoursite.com" />
<input id="phone" name="phone" type="tel" 
 placeholder="(###) ###-####" pattern="\(\d\d\d\) \d\d\d\-\d\d\d\d" />
``` 
 
 ![http://devproconnections.com/site-files/devproconnections.com/files/uploads/2013/11/Palermo%20DCM405%20Figure%206.jpg](http://devproconnections.com/site-files/devproconnections.com/files/uploads/2013/11/Palermo%20DCM405%20Figure%206.jpg)
 
 
 ```
 input.data:required
{
    background-color:       rgba(255, 255, 0, 0.04);
}
input.data:not(:focus):valid 
{

    color:                  rgba(102, 172, 0, 1);
}
input.data:not(:focus):invalid
{
    color:                  rgba(255, 0, 0, 1);
}
input.data:focus
{ 
    border:                 5px solid #ff5400; 
    background-color:       rgba(255, 255, 255, 1); 
}
/* IE10 only */
input.data:-ms-input-placeholder:valid,  
input.data:-ms-input-placeholder:invalid
{
    font-style:             italic;   
    color:                  rgba(0, 0, 0, 0.4)        
}
```

![http://devproconnections.com/site-files/devproconnections.com/files/uploads/2013/11/Palermo%20DCM405%20Figure%209.jpg](http://devproconnections.com/site-files/devproconnections.com/files/uploads/2013/11/Palermo%20DCM405%20Figure%209.jpg)
