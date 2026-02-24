import asyncio
from email.message import EmailMessage
from email.utils import make_msgid, formatdate
import aiosmtplib

EMAIL = "valentine.sender@yandex.com"
EMAIL_PASSWORD = "pfcsllcnvxfenfkk"


async def send_valentine(to: str, text: str, sender_name: str = "Тайный поклонник"):
    """
    Отправляет валентинку.
    :param to: Email получателя
    :param text: Текст валентинки
    :param sender_name: Имя отправителя (если анонимно - "Тайный поклонник")
    """
    message = EmailMessage()
    message["From"] = f"LoveMail <{EMAIL}>"
    message["To"] = to
    message["Subject"] = "Вам пришла новая валентинка! 💌"
    message["Date"] = formatdate(localtime=True)
    message["Message-ID"] = make_msgid(domain="yandex.com")

    plain_text = f"""
Вам пришла валентинка!

{text}

Отправитель: {sender_name}

---
Отправлено через сервис анонимных валентинок.
Каждая валентинка делает чей-то день немного ярче!
    """
    message.set_content(plain_text.strip())

    html_content = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
    </head>
    <body style="font-family: Arial, sans-serif; background: #ffe4ec; margin: 0; padding: 40px 20px;">
        <table width="100%" cellpadding="0" cellspacing="0" style="max-width: 500px; margin: auto; background: #ffffff; border-radius: 20px; box-shadow: 0 15px 40px rgba(225, 29, 116, 0.2); overflow: hidden;">
            
            <!-- Шапка письма -->
            <tr>
                <td style="padding: 40px 30px; text-align: center; background: linear-gradient(135deg, #ff7eb3 0%, #ff477e 100%);">
                    <div style="font-size: 48px; margin-bottom: 15px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.15));">💌</div>
                    <h1 style="margin: 0; color: #ffffff; font-size: 28px; font-weight: 700; text-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                        Вам пришла валентинка!
                    </h1>
                </td>
            </tr>

            <!-- Тело письма -->
            <tr>
                <td style="padding: 40px 30px; text-align: center;">
                    <p style="color: #e11d74; font-size: 16px; font-weight: bold; margin-bottom: 20px;">
                        Кто-то оставил вам послание:
                    </p>
                    <div style="background: #fff0f4; border: 1px dashed #ffc2d1; border-radius: 12px; padding: 25px; margin-bottom: 30px;">
                        <p style="color: #333333; font-size: 18px; line-height: 1.6; margin: 0; font-style: italic;">
                            "{text}"
                        </p>
                    </div>
                    <p style="color: #555555; font-size: 16px; margin: 0;">
                        Отправитель: <span style="font-weight: bold; color: #e11d74;">{sender_name}</span>
                    </p>
                </td>
            </tr>

            <!-- Подвал письма -->
            <tr>
                <td style="padding: 20px; text-align: center; background-color: #fcfcfc; border-top: 1px solid #ffecf0;">
                    <p style="margin: 0; font-size: 12px; color: #aaaaaa;">
                        Каждая валентинка делает чей-то день немного ярче.<br>
                        Отправлено через сервис анонимных валентинок.
                    </p>
                </td>
            </tr>
            
        </table>
    </body>
    </html>
    """
    message.add_alternative(html_content, subtype="html")

    # Отправка
    try:
        await aiosmtplib.send(
            message,
            hostname="smtp.yandex.com",
            port=587,
            username=EMAIL,
            password=EMAIL_PASSWORD,
            start_tls=True,
        )
        print(f"[✔️] Валентинка успешно отправлена на {to}")
    except aiosmtplib.errors.SMTPRecipientsRefused:
        print(f"[X] Ошибка: Почта {to} не существует или отклонила письмо.")
    except Exception as e:
        print(f"[X] Неизвестная ошибка при отправке: {e}")
