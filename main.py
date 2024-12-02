import data_download as dd
import data_plotting as dplt


def calculate_and_display_average_price(data: 'pd.DataFrame') -> None:
    """
    Вычисляет и выводит среднюю цену закрытия акций за заданный период.

    :param data: DataFrame с данными об акциях, который должен содержать колонку 'Close'.
    :return: None. Результат выводится в консоль.
    """
    if 'Close' not in data:
        print("Ошибка: В переданном DataFrame отсутствует колонка 'Close'.")
        return

    # Вычисляем среднюю цену закрытия
    average_price = data['Close'].mean()

    # Выводим результат в консоль
    print(f"Средняя цена закрытия за заданный период: {average_price:.2f}")




def main():
    """
        Основная функция программы. Запрашивает ввод от пользователя, загружает данные,
        обрабатывает их и выводит результаты, включая график и среднюю цену закрытия.
        """
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")

    # Загружаем данные об акциях
    stock_data = dd.fetch_stock_data(ticker, period)

    # Проверяем, получили ли мы данные
    if stock_data.empty:
        print("Не удалось загрузить данные для указанного тикера и периода. Проверьте ввод.")
        return

    # Добавляем скользящее среднее
    stock_data = dd.add_moving_average(stock_data)

    # Вычисляем и выводим среднюю цену закрытия
    calculate_and_display_average_price(stock_data)

    # Строим и сохраняем график
    dplt.create_and_save_plot(stock_data, ticker, period)



if __name__ == "__main__":
    main()
