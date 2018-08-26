function hashMap(){
    this.hash = {};
    this.defaultModuler = 24;
    this.set = function(data){

    }
    this.moduler = function(data){
        if(!this.isNumber(data)){
            var sum = 0;
            data.split("").forEach(element => {
                sum += element.charCodeAt(0)
            });
            return sum%this.defaultModuler;
        }
        else{
            return data%this.defaultModuler;
        }
        
    }
    this.isNumber = function(s) {
        s += ''; 
        s = s.replace(/^\s*|\s*$/g, '');
        if (s == '' || isNaN(s)) return false;
        return true;
      }
}





var h = new hashMap();
console.log(h.moduler("adf"));