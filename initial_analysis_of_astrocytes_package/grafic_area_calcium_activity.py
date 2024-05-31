import matplotlib.pyplot as plt

def grafic_area_calcium_activity(time_list, calcium_activities):
  # Создание графика
  plt.figure(figsize=(8.27/3, 11.69/3), dpi=300)  # Установка dpi для 300 пикселей
  plt.plot(time_list, calcium_activities, color='#FF5733', linewidth=2)  
  plt.xlabel('Время, мин')  
  plt.ylabel('Площадь кальциевого события, мкм^2')  
  plt.title('Кальциевая активность астроцитов с течением времени')  
  plt.xlim(min(time_list), max(time_list)) 
  plt.ylim(min(calcium_activities), max(calcium_activities))  
  plt.legend(['Линия'], loc='upper right')  # Легенда

# Сохранение графика в форматах .png и .svg
  plt.savefig('график.png', dpi=300)  # Установка dpi для сохранения в png
  plt.savefig('график.svg')

  plt.show()