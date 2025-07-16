## Templates in C++

template is a tool in C++, that allows you to write generic code so that 
the template entity takes the datatype as an argument. 

### Syntax 

```
template<typename A, typename B>
entity_definition
    .
    .
    .
```
### Terminology 

* **template** keyword is used to mention the entity is a template  
* **typename** keyword is used to define a place holder name for data type which is provided at the time of instance creation. 
* **entity** in a program refers to any element that can be named or manipulated

### Entities for which template tool can be used

1. Function templates
2. Class templates
3. variable templates

### Instance creation for template entity

```
entity_name<type1, type2, . . .>
```

### --> Function template 

#### Template Definition
```
template<typename T>
T temp_max (T a, T b){
    return b < a ? a : b;
}
```
#### Instance Creation
```
temp_max<int>(a,b)
```

### --> Class Template

#### Template Definition 

```
template<typename t1, typename t2>
class MyClass{
    public:
        t1 mem1, 
        t2 mem2,
        
        //constructor 
        MyClass(t1 a, t2 b) : mem1(a), mem2(b) {
            //body
        } 
}
```

#### Instance Creation

```
MyClass my_object<string, int>("Rafee", 25)
```

### --> Variable Template ( we'll look into this when we go though the topic in the book)