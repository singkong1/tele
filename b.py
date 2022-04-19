#module
import requests
import asyncio
import json
from aiogram import Bot, Dispatcher, types
#endsModule

BOT_TOKEN = "5252703642:AAH7-lMf05uUdKTGk71yFV44k3kL2zM7zpI"

list_item_whm = """
```
• WHM Trial: Free
  - 1 GB SSD Storage
  - 1 Akun cPanel
  - 5 GB Bandwidth
  - 1 Addons Domain
  - 2 Subdomain

• WHM Mini: 30k
  - 10 GB SSD Storage
  - 15 Akun cPanel
  - Unlimited Bandwidth

• WHM Medium: 40k
  - 20 GB SSD Storage
  - 30 Akun cPanel
  - Unlimited Bandwidth

• WHM Super: 60k
  - 50 GB SSD Storage
  - 55 akun cPanel
  - All Unlimited

• WHM Extra: 70k
  - 60 GB SSD Storage
  - 55 Akun cPanel
  - All Unlimited

• WHM Unli: 90k
  - Unlimited Storage
  - 100 akun cPanel
  - All Unlimited```

**Payments**:
DANA, OVO, BCA.
"""

async def mulai(pesan: types.Message):
	await pesan.answer(
        f"Hello, {pesan.from_user.get_mention(as_html=True)} 👋!",
        parse_mode=types.ParseMode.HTML,
    )
    
async def nulis(pesan: types.Message):
	if pesan.text.replace('/nuliskiri', ''):
		tulisan = pesan.text.replace('/nuliskiri', '')
		await pesan.answer_photo(types.InputFile.from_url(f"https://api.dapuhy.xyz/api/maker/nuliskiri?text={tulisan}&apikey=risenqpi"))
		
	elif pesan.text.replace("/nuliskanan", ''):
		tulisan = pesan.text.replace('/nuliskanan', '')
		await pesan.answer_photo(types.InputFile.from_url(f"https://api.dapuhy.xyz/api/maker/nuliskanan?text={tulisan}&apikey=risenqpi"))

async def web_site(pesan: types.Message):
	url = 'https://risenmedia.my.id'
	await pesan.answer(
		f"Hallo, {pesan.from_user.get_mention(as_html=True)} Silahkan kunjungi website {pesan.link(url, as_html=True)} untuk informasi lebih lanjut!",
		parse_mode=types.ParseMode.HTML,
	);

async def kuso_nime(pesan: types.Message):
	jdul_nimek = pesan.text.replace("/kusonime", '')
	res = requests.get(f"https://xmadd4.herokuapp.com/api/kuso?q={jdul_nimek}").text
	stts = json.loads(res)['status']
	try:
		if stts == 200:
			jdl = json.loads(res)['title']
			info = json.loads(res)['info']
			sinop = json.loads(res)['sinopsis']
			lnk_dl = json.loads(res)['link_dl'].replace("=>", '\n')
			pic = json.loads(res)['thumb']
			await pesan.answer_photo(types.InputFile.from_url(pic), f"Judul: {jdl}\n\nInformasi:\n{info}\nSinopsis: {sinop}\n\nLink Download:\n{lnk_dl}"
			)

		else:
			await pesan.answer(f"Maaf ya kak {pesan.from_user.get_mention(as_html=True)}, Saat ini informasi tidak dapat di akses atau coba cari dengan judul lain!\nStatus Code: {stts}",
			parse_mode=types.ParseMode.HTML,
			)

	except IOError as err:
		await pesan.answer(f"Maaf kak {pesan.from_user.get_mention(as_html=True)}, Saat ini terjadi kesalahan pada {err}",
		parse_mode=types.ParseMode.HTML,)
		
	
async def list_whm(pesan: types.Message):
	await pesan.answer(
		f"Hallo kak {pesan.from_user.get_mention(as_html=True)}, {list_item_whm}\nSebelum membeli silahkan lihat & baca dulu ya kak 😊",
		parse_mode=types.ParseMode.HTML,
	)

async def main():
	print("Bot Sedang Berjalan ...")
	bot = Bot(token=BOT_TOKEN)
	try:
		disp = Dispatcher(bot=bot)
		disp.register_message_handler(mulai, commands={"start", "restart"})
		disp.register_message_handler(nulis, commands={"nuliskiri", "nuliskanan"})
		#disp.register_message_handler(nulis_kanan, commands={"nuliskanan"})
		disp.register_message_handler(web_site, commands={"website"})
		disp.register_message_handler(list_whm, commands={'listwhm'})
		disp.register_message_handler(kuso_nime, commands=['kusonime'])
		await disp.start_polling()
	finally:
		await bot.close()

if __name__ == "__main__":
	while(True):
		asyncio.run(main())