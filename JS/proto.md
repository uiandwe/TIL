```

function p(n){
 this.name = n;
 this.__proto__.getName = function(){ return this.name; }
}

var pa = new p("pa");
var pb = new p("pb");

pa.getName();
pb.getName();

p.__proto__.getName = function(){ return this.name+" fuck you";}
pa.getName();
pb.getName();


pa.__proto__.getName = function(){ return this.name+" fuck you";}
pa.getName();
pb.getName();



```

- proto 로 생성한 경우 해당 객체에 종속된것이 아닌 하나의 객체에서 상속을 받게 된다. 
- 그래서 객체 생성후 p.__proto__.getName를 수정해도 변화가 없지만(생성을 하지 않은 상태에서 변경하였으므로 변경이 되지 않음)
pa.__proto__.getName를 수정하면 해당 객체를 수정하여 모든 객체들에 영향이 간다.
 
