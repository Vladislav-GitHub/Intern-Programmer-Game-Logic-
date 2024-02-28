# Intern-Programmer-Game-Logic-

![image](https://github.com/Vladislav-GitHub/Intern-Programmer-Game-Logic-/assets/85065325/73cfd1b5-c63a-47c1-9998-721f435a7eee)

## Вопрос №1

Делаем бин. коньюнкцию или лог. операцию "AND" (кому как удобнее определять одну и ту же операцию) и смотрим на младший бит числа, если он равен 0 => чётное число, иначе нечётное. Бинарная операция работает быстрее обычных арифметических. Пример: 7_10 = 111_2 => 111 & 1 == 1 => чётное.

## Вопрос №2

**Класс Queue**:

Плюсы:

- Операции добавления имеет O(1) и удаления элемента из очереди имеют O(n) в худшем случае, что обычно приемлемо для многих приложений.

Минусы:

- При удалении элемента из начала списка (self.array.pop(self.idx)) требуется перекопировать все элементы, начиная со второго, что имеет квадратичную сложность и может быть неэффективным при больших объемах данных.

**Класс FIFO**:

Плюсы:

- Реализация кольцевого буфера с использованием индекса делает операции добавления и удаления элементов более эффективными, так как не требуется сдвигать все элементы в списке.
- Класс FIFO позволяет контролировать размер очереди, что может быть полезно в ограниченных по памяти средах или в ситуациях, когда требуется фиксированный объем данных.
  
Минусы:

- Интерфейс класса FIFO не так прост как у класса Queue. Он имеет методы push и getitem, которые могут потребовать более глубокого понимания тех, кто будет использовать этот класс.
- При попытке добавить элемент в полностью заполненную очередь, новый элемент просто заменяет самый старый элемент, без какого-либо предупреждения или возможности обработать эту ситуацию.

Сравнение быстродействия:
Оба класса имеют преимущества и недостатки в быстродействии в зависимости от конкретного сценария использования. В целом, FIFO склонен к более эффективному использованию памяти и времени, особенно при больших объемах данных, благодаря использованию кольцевого буфера. Однако, при малых объемах данных или при необходимости простоты и понятности реализации, Queue может быть более предпочтительным вариантом.

## Вопрос №3

Сортировка слиянием работает быстрее quicksort в худшем случае, и имеет сложность O(nlogn). Сортировка слиянием более эффективна для больших массивов по сравнению с quick sort + временная сложность сортировки слиянием не зависит от содержимого массива.
