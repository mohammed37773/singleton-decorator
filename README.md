# python singleton decorator

unlike usual decorators which replace the ***class*** with a ***modified function*** that handle keeping one instance initialized. this decorator return the class itself

for example

```
@some_singleton_decorator
class ClassName:
    ...

print(type(ClassName)) # -> <class 'function'>
```
so you can't interact with the class itself.

And her comes this decorator to solve this.

The main idea is to move the modifications inside the class then return the new modified class so 
```
@singleton
class ClassName:
    ...

print(type(ClassName)) # -> <class 'ClassName'>
```