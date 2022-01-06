# Get all Hive 🐝 boxes
**_Posted on 05 Jan, 2022_**


```dart
import 'dart:async';
import 'dart:io';

import 'package:hive/hive.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart' as p;

extension on HiveInterface {
  /// Get a name list of existing boxes
  FutureOr<List<String>> getNamesOfBoxes() async {
    final appDir = await getApplicationDocumentsDirectory();
    var files = appDir.listSync();
    var _list = <String>[];

    files.forEach((file) {
      if (file.statSync().type == FileSystemEntityType.file 
        && p.extension(file.path).toLowerCase() == '.hive') {
        _list.add(p.basenameWithoutExtension(file.path));
      }
    });
    print('Current boxes: $_list');
    return _list;
  }
}
```

## Resources

- Shamelessly copied from [StackOverflow](https://stackoverflow.com/questions/60584884/how-to-delete-all-the-boxes-in-the-hive-in-flutter)
