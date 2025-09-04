# PDF Sonar watermark cleaner

Удаляет водяной знак из PDF файла от триальной версии Sonar.

## Как использовать

Для работы программы необходимо установить пакет PyMuPDF

```python
pip install PyMuPDF
```

## Скомпилировать программу

Необходимо установить пакет PyInstaller

```python
pip install PyInstaller
```

Скомпилировать программу в один файл

```python
pyinstaller -F pdfSonarCleaner.py
```

Скомпилированный файл dist/pdfSonarCleaner можно добавить в переменную окружения

## Запуск программы
### Терминал:

Ключ
```commandline
-i (--input) /path/to/pdf/
```

Переменную окружения 

```commandline
$youVariableName -i /path/to/pdf`
```

Указание пути до программы
```commandline
/pdfSonarCleaner/dist/pdfSonarCleaner -i /path/to/pdf`
```

### Через файл pdfSonarCleaner
С небольшой задержкой появляется возможность ввести путь до PDF файла

### Результат работы
После очистки в той же директории, где находится исходный PDF файл, формируется файл с таким же названием, но с приставкой _cleaned.pdf