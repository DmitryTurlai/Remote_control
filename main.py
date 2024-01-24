import pyautogui, random, time
class Cursor_Mouse:
    def __init__(self):
        pass
    def moove_cursor(self, x, y, button_click):
        time.sleep(0.5)
        try:
            pyautogui.moveTo(x, y, random.uniform(0.0, 1.5))

        except pyautogui.FailSafeException:
            print(f"Заданные координаты x={x}, y={y} за пределами монитора.")
        x, y = pyautogui.position()  # сохранение текущего положения курсора
        self.click(x, y, button_click)
        return x, y

    def moove_cursor_pic(self, path, button_click):
        time.sleep(0.5)
        # Загрузка образца картинки для поиска ее на экране монитора
        pic = pyautogui.locateOnScreen(path)

        try:
            # Получение центральных координат образа
            x, y, width, height = pic
            x_center = x + width / 2
            y_center = y + height / 2

            # Перемещение курсора на центральные координаты образа
            pyautogui.moveTo(x_center, y_center, 1)
            pyautogui.mouseDown(x_center, y_center, button='left')
        except pyautogui.ImageNotFoundException:
            print("Изображение не найдено на экране.")



    def click(self, x, y, button_click):
        time.sleep(0.5)
        #self.button_click = button_click
        if button_click == 1:
            # Эмуляция нажатия левой кнопкой мыши по координатам
            pyautogui.mouseDown(x, y, button='left')
        elif button_click == 2:
            # Эмуляция двойного нажатия левой кнопкой мыши по координатам
            pyautogui.doubleClick(x, y)
        else:
            pass



# Создание экземпляра класса
my_object = Cursor_Mouse()
x = 100
y = 200
my_object.moove_cursor(x, y, 0)
time.sleep(0.6)
my_object.moove_cursor_pic('images/windows.png', 1)
time.sleep(0.5)
my_object.moove_cursor(377, 784, 1)
my_object.click(x,y,2)
#my_object.moove_cursor(x, y, 0)
my_object.moove_cursor_pic('images/close.png', 2)





