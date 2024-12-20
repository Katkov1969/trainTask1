В файл main.py добавлена функция calculate_and_display_average_price.
Объяснение логики функции calculate_and_display_average_price:
1. Проверка наличия колонки 'Close':
   Прежде чем выполнять вычисления, функция проверяет, что в переданном DataFrame существует колонка 'Close'. Если её нет, выводится сообщение об ошибке, и выполнение функции завершается.
2. Вычисление средней цены закрытия:
   Среднее значение вычисляется с помощью метода .mean() для колонки Close.
3. Вывод результата:
   Результат округляется до двух знаков после запятой и выводится в консоль.
________________________________________________________________________________________________________________________________________________________________
   В рамках второго задания в файл main.py добавлена функция notify_if_strong_fluctuations.
Объяснение логики этой функции:
1. Проверка наличия колонки 'Close':
    Функция проверяет, что в переданном DataFrame существует колонка 'Close'. Если её нет, выводится сообщение об ошибке, и выполнение функции завершается.
2. Вычисление максимальной и минимальной цены закрытия:
   Используются методы .max() и .min() для нахождения максимального и минимального значения в колонке Close.
3.Вычисление разницы в процентах:
    Разница между максимальной и минимальной ценой рассчитывается по формуле:
         fluctuation = ((max_close - min_close) / min_close) * 100
4. Вывод разницы:
      Разница выводится на консоль в формате:
        "Разница между максимальной и минимальной ценой закрытия: 12.34%"
5.Проверка порога:
   Если вычисленная разница больше заданного порога threshold, выводится уведомление:
       "Превышен порог колебаний цены акций!"
   В противном случае выводится уведомление:
       "Порог колебаний цены НЕ превышен!"

   Пример выполнения программы (вывод в консоль):
   C:\Users\user\PycharmProjects\traineeshipProject1\.venv\Scripts\python.exe C:\Users\user\PycharmProjects\traineeshipProject1\main.py 
Добро пожаловать в инструмент получения и построения графиков биржевых данных.
Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).
Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.
Введите тикер акции (например, «AAPL» для Apple Inc)»: TSLA
Введите период для данных (например, '1mo' для одного месяца): 3mo
Введите порог колебаний цен в процентах (например, 7 для 7%): 5
Средняя цена закрытия за заданный период: 264.32
Разница между максимальной и минимальной ценой закрытия: 69.56%
Превышен порог колебаний цены акций!
График сохранен как TSLA_3mo_stock_price_chart.png

Process finished with exit code 0
_____________________________________________________________________________________________________________________
В рамках третьего задания в файл main.py добавлена функция export_data_to_csv(data, filename).
Объяснение логики этой функции:
1. Параметры функции:
    data: Объект DataFrame, содержащий данные об акциях.
    filename: Имя файла, в который нужно сохранить данные в формате CSV.
2. Сохранение данных:
   Используется метод to_csv() из библиотеки pandas для сохранения DataFrame в файл. Параметр index=True сохраняет индекс DataFrame, чтобы даты или другие индексы не терялись.
3. Обработка ошибок:
   Если при сохранении файла возникает ошибка (например, из-за некорректного имени файла или проблем с доступом к диску), она перехватывается с помощью try...except, и выводится сообщение об ошибке.
4. Уведомление об успешном сохранении:
    Если данные успешно сохранены, выводится сообщение с указанием имени файла.

Изменения в основной функции main
После загрузки и обработки данных программа спрашивает пользователя, хочет ли он экспортировать данные в CSV.
Если пользователь вводит "да" (или эквивалентное значение), данные сохраняются в файл с автоматически сгенерированным именем, например: AAPL_1mo_stock_data.csv.

Пример работы программы:
Добро пожаловать в инструмент получения и построения графиков биржевых данных.
Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).
Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.
Введите тикер акции (например, «AAPL» для Apple Inc)»: AAPL
Введите период для данных (например, '1mo' для одного месяца): 1mo
Введите порог колебаний цен в процентах (например, 7 для 7%): 5
Средняя цена закрытия за заданный период: 229.26
Разница между максимальной и минимальной ценой закрытия: 9.42%
Превышен порог колебаний цены акций!
График сохранен как AAPL_1mo_stock_price_chart.png
Хотите ли вы экспортировать данные в CSV? (да/нет): y
Данные успешно сохранены в файл: AAPL_1mo_stock_data.csv

Process finished with exit code 0
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
ЗАДАНИЕ 4
Добавлены технические индикаторы:
1. RSI (Relative Strength Index): Показывает, перекуплен ли или перепродан актив. Значения RSI варьируются от 0 до 100, где значения выше 70 указывают на перекупленность, а ниже 30 — на перепроданность.
2.MACD (Moving Average Convergence Divergence): Индикатор, показывающий расхождение или схождение двух скользящих средних.
   MACD Line (разница между двумя EMA — экспоненциальными скользящими средними),
   Signal Line (EMA от MACD Line).
3. ATR (Average True Range): Показатель волатильности, измеряющий средний диапазон движения цены за определённый период.
 В файле data_download.py добавлены функции:
calculate_rsi для расчета RSI,
calculate_macd для расчета MACD,
calculate_atr для расчета ATR.

В файл data_plotting.py внесены изменения. Строятс 4 графика в одном окне. На графике отображаются:

- Цена закрытия и скользящее среднее,
- RSI с уровнями перекупленности и перепроданности,
- MACD с сигнальной линией,
- ATR, показывающий волатильность актива.
Графики имеют метки, легенды и сетку.
  Пример работы. Запись в консоли:
![Запись в консоли](https://github.com/user-attachments/assets/597c6d4f-c2ed-4739-8162-e14c62efcbdc)

График:
![GOOGL](https://github.com/user-attachments/assets/e8e9e644-4f65-4930-ba82-6fabf3a10ba0)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
ЗАДАНИЕ 5
ЗАДАНИЕ 5
Сводка изменений
В main.py добавлен ввод дат начала и окончания (строки 80 - 89). Такж добавлена передача дат в fetch_stock_data (строка 99), а также обновление имени графика и CSV-файла (строки 119, 125).
В data_download.py функция fetch_stock_data модифицирована для работы с диапазоном дат.

Пример работы программы для Google с датами 2021-01-01  2021-06-01:
Запись в консоли:
![Запись в консоли_1](https://github.com/user-attachments/assets/7e6703fa-b6fe-497d-b009-718a7d11e4b0)

График:
![GOOGL_1](https://github.com/user-attachments/assets/cc37d222-d774-4707-b88d-d561d4c3d5c5)














   

