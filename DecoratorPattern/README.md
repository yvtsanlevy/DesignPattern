The decorator pattern is a design pattern that allows behavior to be added to an individual object, dynamically, without affecting the behavior of other objects from the same class.

The decorator pattern is often useful for adhering to the Single Responsibility Principle, as it allows functionality to be divided between classes with unique areas of concern.

Decorator use can be more efficient than subclassing, because an object's behavior can be augmented without defining an entirely new object.

#What problems can it solve?
1. Responsibilities should be added to (and removed from) an object dynamically at run-time.[4]
2. A flexible alternative to subclassing for extending functionality should be provided.
3. When using subclassing, different subclasses extend a class in different ways. But an extension is bound to the class at compile-time and can't be changed at run-time