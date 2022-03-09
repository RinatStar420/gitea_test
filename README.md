Запуск проекта:

1. git clone https://github.com/RinatStar420/gitea_test.git
2. cd gitea_test
3. docker-compose up -d

Тестирование проекта: 

4. cd gitea_test/tests  
5. pip3 install -r requirements.txt
6. python3 -m pytest test_clss.py



Примечание:

Код tests/test_clss.py настроен на работу с драйвером chromedriver под архитектуру
процессора М1, использование кода на системах:

- для linux необходимо раскомментировать строку кода 22;
- для mac64 необходимо раскомментировать строку кода 21;

и закомментировать строку с иным драйвером.

После выполнения каждой пошаговой инфструкции используется метод sleep(2) класса time, для 
визуальной оценки выполнения задания. 