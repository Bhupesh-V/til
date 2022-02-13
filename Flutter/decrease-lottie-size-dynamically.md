# Decrease lottie size dynamically in flutter
**_Posted on 08 Jan, 2022_**

```dart
SizedBox(
   height: <height you want for lottie>,
   child: OverflowBox(
    maxHeight: <height greater than you set for lottie>,
    child: Lottie.asset('animation.json'),
  ),
),
```

