## Generar estructura 'case' con Python

Para este ejercicio hay que generar con Python la siguiente estructura de control `case`:

```ruby
#estructura de control 'case' en ruby

speed = 37
case speed
when 0..20
  p "You are One"
when 21..30
  p "You are Second"
when 31..40
  p "You are Third"
else
  p "You are the best"
end

#=> "You are Third" 
```

Es importante definir la función anidada `numbers_to_ranges` con su función `switch_example` y hacer uso de las funciones `one`, `second`, `third` y `default` para retornar el mensaje `string` de cada caso. El resultado de la prueba `driver code` de esta función debe ser `True`.

```python
"""python functions"""

#one function

#second function

#third function

#default function

#numbers_to_ranges function
def numbers_to_ranges(number):
 

    #switch_example function
    def switch_example(speed, ranges):
        

#driver code

#switch o case con número 37
print(numbers_to_ranges(37) == "You are Third")
#switch o case con número 10
print(numbers_to_ranges(10) == "You are One")
#switch o case con número 25
print(numbers_to_ranges(25) == "You are Second")
#switch o case con número 41
print(numbers_to_ranges(41) == "You are the best")
``` 


> - Recuerda el uso de la función `range` en Python.
> - Hay que documentarse acerca de como iterar un diccionario para evaluar su clave `key`.