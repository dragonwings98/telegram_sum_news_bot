from aiogram.types import Message



async def help_bot(message: Message):
    return await message.answer(
        'Добро пожаловать в бота. \n\n'
        'С помощью данного бота вы добавить свои новостные каналы и получать выжимку из них за указанный период времени.\n\n'
        'Доступные команды:\n'
        'Для запуска бота /start \n'
        'Для регистрации в боте /login \n'
        'Для открытия меню /menu \n'
        'Для добавления канала /add_channel \n'
        'Для просмотра списка каналов /list_channels \n'
        'Для изменения периода рассылки для канала /update_period_channel \n'
        'Для удаления канала /remove_channel \n'
        'Для удаления учетной записи в боте /logout \n'
    )
