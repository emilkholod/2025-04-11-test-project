# Проект: freelancer_analyzer_app

## Описание
Тестовый проект

## Требования
Перед запуском убедитесь, что на вашем компьютере установлены:
- Docker
- Docker Compose

## Установка
1. Соберите контейнеры:
   ```sh
   make build
   ```
2. Запустите приложение:
   ```sh
   make run
   ```

## Использование
- Для остановки сервисов:
  ```sh
  make down
  ```
- Для запуска тестов выполните команду:
  ```sh
  make test
  ```
- Для создания production образа:
  ```sh
  make prod
  ```
- Для открытия shell внутри контейнера:
  ```sh
  make sh
  ```

## Структура проекта
- `src/` — исходный код проекта
- `tests/` — тесты
- `Dockerfile` — конфигурация Docker-образа
- `docker-compose.yml` — настройка сервисов для разработки
- `Makefile` — автоматизация команд

## Отчет

### Подход решения
Для решения задачи была реализована CLI-система, которая принимает текстовые запросы,
интерпретирует их с помощью агента на базе LLM (OpenAI GPT-3.5-turbo).
При этом данные отправляются только частично: только самая общая информация о таблице и так далее.
Агент в ходе решения задачи выдаёт python-код, который будет выполниться на стороне приложения.
Результаты запроса интерпретируются и возвращаются в текстовой форме.

### Оценка эффективности и точности работы системы
<details>
  <summary>Примеры вопросов и ответов</summary>

---

Введите запрос: Покажи средние зарплаты в зависимости от категории

Ответ: The average earnings based on Job_Category are as follows:
- App Development: $5201.45
- Content Writing: $4909.05
- Customer Support: $5135.54
- Data Entry: $5081.07
- Digital Marketing: $5094.26
- Graphic Design: $5136.87
- SEO: $4677.33
- Web Development: $4888.15

---

Введите запрос: Какой процент успешных проектов у фрилансеров с разным уровнем опыта?

Ответ: Use the python_repl_ast tool to calculate the percentage of successful projects for each experience level.

---

Введите запрос: Какая средняя почасовая ставка у фрилансеров в категории Web Development на платформе Fiverr?

Ответ: Средняя почасовая ставка у фрилансеров в категории Web Development на платформе Fiverr составляет average_hourly_rate.

> (Подробнее об этом, см. в секции [Что может пойти не так](#что-может-пойти-не-так))

---

Введите запрос: Какой метод оплаты наиболее распространен среди фрилансеров?

Ответ: The most common payment method among freelancers is Crypto, with 514 occurrences.

---

Введите запрос: Покажи все проекты в категории "Web Development" с уровнем опыта "Beginner".

Ответ: There are 94 projects in the "Web Development" category with the "Beginner" experience level.

---

Введите запрос: Выведи список всех проектов в категории "Web Development" с уровнем опыта "Beginner".

Ответ: There are 94 projects in the "Web Development" category with an experience level of "Beginner".

---

Введите запрос: Сравни средние заработки фрилансеров с уровнем опыта "Intermediate" и "Expert".

Ответ: The average earnings of freelancers with experience level "Intermediate" is $4670. The average earnings of freelancers with
experience level "Expert" is $5898.

---

Введите запрос: Какие фрилансеры заработали более 5000 USD и имеют уровень успеха выше 80%?

Ответ: There are 409 freelancers who earned more than 5000 USD and have a job success rate above 80%.

---


Введите запрос: Какие фрилансеры заработали более 5000 USD и имеют уровень успеха ниже 80%?

Ответ: There are 568 freelancers who earned more than 5000 USD and have a job success rate below 80%.

---

Введите запрос: Сколько всего фрилансеров заработали более 5000 USD?

Ответ: 978

---

Введите запрос: Как соотносятся маркетинговые расходы и заработки фрилансеров?

Ответ: The correlation between marketing spend and freelancer earnings is 0.043041301009136175.

---

Введите запрос: Какие фрилансеры имеют наивысшие маркетинговые расходы и как это соотносится с их заработками?

Ответ: Freelancers with the highest marketing spend of 499 USD have earnings ranging from 166 to 9421 USD.

---

Было проведено тестирование на вопросах выше. В целом выходит, что на более менее простые вопросы система отвечает корректно, но если вопрос чуть сложнее, то она может интерпретировать вопрос неверно или даже выдавать не те результаты, которые бы хотелось получить.
</details>

### Технологии и методы в проекте
В данном проект использовались следующие инструменты:
- click - как CLI инструмент
- rich - для улучшенного взаимодействия с пользователем
- langchain - для работы с LLM и AI агентами
- dishka - для внедрения зависимостей
- pytest - для тестирования
- Dockerfile и docker-compose - для создания и запуска проекта

Dockerfile и docker-compose очень важны для данного проекта, так как python-код, который приходит от AI-агента выполняется в приложении. Поэтому, чтобы ничего зловредного не происходило в хостовой системе, приложение запускается в docker контейнерах.

Для создания агента использовал `create_pandas_dataframe_agent` из `langchain_experimental`, но в будущем я бы хотел попробовать использовать `langchain_graph` - возможно он лучше бы справился с вопросами выше.

Также пробовал сразу переводить на русский язык, но из-за этого модель иногда переставала отвечать корректно. Поэтому на данный момент убрал. Но можно добавить либо как отдельный запрос llm, чтобы она переводила, либо после интеграции с `langchain_graph`.

### Критерии оценки качества
- Весь датафрейм не загружается в AI-агент
- Точность: не менее 90% корректных ответов на тестовые запросы
- Прозрачность: можно подключить вывод логов через переменную среды `CHAT_VERBOSE_AGENT`


### Что может пойти не так

Но иногда всё же с кодом бывают проблемы: AI-агент верно решает задачу (код верный), но он почему-то не выполняется корректно:
```bash
Введите запрос: Какие фрилансеры заработали более 5000 USD и имеют уровень успеха выше 80%?


> Entering new AgentExecutor chain...
Thought: We need to filter the dataframe based on freelancers who earned more than 5000 USD and have a job success rate above
80%.
Action: python_repl_ast
Action Input: df_filtered = df[(df['Earnings_USD'] > 5000) & (df['Job_Success_Rate'] > 80)]I now know the final answer
Final Answer: df_filtered

> Finished chain.
```
Это похоже на баг, который возможно отладят в будущем, пока не стал копать глубже.

### Планы по улучшению
- Обработка ошибок от AI-агента
- Интеграция langchain_graph для более точной логики.
- Локализация: ответы на русском языке.
- Обработка прерывания (Ctrl+C).
- Строгая типизация зависимостей (dishka).
