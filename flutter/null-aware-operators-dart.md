# Null aware operators in Dart
 

Null aware operators makes handling real world data very intuitive & easy. Let's have a brief overview of all the 4 null aware operators in Dart.

## The `?.` operator

> Prevent method call on null objects

```dart
// call func() only if myVar is not null
myVar?.func();
// can also be chained
final value = myVar?.getValue()?.valueA;
```

This is similar to following code

```dart
myVar = myVar == null ? null : myVar.func();
```


## The `??` operator

This operator can be used to assign a default fallback value.

> Return the first expression IFF it is not null.

```dart
// if unkownSource is null assign username with "default value" otherwise assign the value of unkownSource
username = unkownSource ?? "default value";
```

## The `??=` operator

> Assign a value IFF it is not null.

```dart
// assign string "test" to myVar only if myVar is null
myVar ??= "test";
```

## The `...?` operator - Null aware spread operator

> Expand list elements IFF it's not null

```dart
void main() {
  List<int> varA = [2, 3, 4];
  List<int>? varB = null;
  final concatList = [1, ...varA, ...?varB];
  print(concatList);
  // [1, 2, 3, 4]
}
```
