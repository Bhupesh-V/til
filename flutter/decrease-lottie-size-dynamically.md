# Decrease lottie size dynamically in flutter


```dart
SizedBox(
   height: <height you want for lottie>,
   child: OverflowBox(
    maxHeight: <height greater than you set for lottie>,
    child: Lottie.asset('animation.json'),
  ),
),
```

