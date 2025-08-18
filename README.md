# Сервис API для LMS

RESTful API для системы дистанционного обучения на Django REST Framework и PostgreSQL.

## Основные функции

- Аутентификация по JWT
- Управление курсами и уроками
- Управление пользователями (автоблокировка неактивных)
- Интеграция платежей
- Подписки на обновления курсов
- Документация через Swagger/Redoc

## Установка

1. Обновите систему:
```bash
sudo apt update && sudo apt upgrade -y
2. Установите Docker:
Чтобы установить Docker, воспользуйтесь инструкцией по установке с официального сайта: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
3. Настройте фаервол::
```commandline
sudo ufw status
sudo ufw enable
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 22/tcp
```
4. Клонируйте репозиторий:
```commandline
git clone https://github.com/mikhailsorochinskiy/sky_drf.git
cd sky_drf/
```
5. Настройте окружение:
```commandline
cp .env.sample .env
nano .env
```
6. Запустите сервис:
```commandline
docker-compose up
```
7. Поздравляем! Проект успешно настроен!
Для начала работы перейдите по адресу вашего сервера(IP)

## Workflows
### Запуск Workflow
При коммитах и отправке изменений в удаленный репозиторий, будет автоматически запускаться CI/CD workflow. 
Убедитесь, что ваш файл .env содержит следующее значение для HOST: HOST=localhost

Примечание: Если вы развертываете на удалённом сервере, измените значение на имя вашего сервиса или IP-адрес.

### Деплой приложения
Для развертывания приложения на удалённом сервере выполните следующие шаги:

1. Подключитесь к вашем серверу через SSH:
```
ssh user@your-server-ip
```

2. Перейдите в директорию проекта:
```
cd /path/to/your/project
```

3. Запустите развертывание с помощью команд:
```
docker-compose down
docker-compose up -d --build
```

## API Documentation

После запуска контейнера документация будет доступна по адресам:

Swagger UI: http://localhost:8000/swagger/
Redoc UI: http://localhost:8000/redoc/