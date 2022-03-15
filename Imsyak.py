# AUTHOR :Zeddnyx
# API : https://imsakiyah-api.santrikoding.com/

import os
import json
import requests as req


class JawaBarat():

	def Bogor():
		url = 'https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=SbYv3TDmpepPD%252BajUqt3wK1G6XjKpbgk7ZupoPmy8bMSbe%252FOom8EAgXGYERVvRHfTVik%252FwYcuLiATL94wTRfnA%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Bandung():
		url = 'https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=Obwt7TgCkfKWjV0hg%252B90q1QayS1yYSdFzbpJM1ssY6dWxME6g5VoxyZxwC558RsOgsjN05hwSFyYjYznueXP7g%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def BandungBarat():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=LxyNv4NwrGsZAdMxI%252FE13D64xMp%252BOxO1HY%252F6xgVwa%252FSXWioo8%252FZZWcsUIHs6nLHHd%252BUqRr0EZOSnXiJKlpUPbw%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Bekasi():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=te9JlU%252B5lUtwAqUxZbVEAwQuh3yLOU0YlLfID8bKb3YrTAtgjUmrSPhBnsvCfuIAvSTRnGbKPcaQGEeYNPMuTw%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Ciamis():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=wnUYTQQ5lqL7DI0EWkoHtvioRjvcoSzAJJpyhQ0kGl3DljEXGqoEYRMmHd9Zowd8F7FUsLSPIEsvRf5qTWh1Dg%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Cianjur():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=sfV%252FzsggPZngf7qAyi5V679d7iiOGZPCR0fu8KMXIG2GlsZpen9mXc9wNeBEM%252Bx%252BKGdOjsSJY7oJsIJtujDY9Q%253D%253D&year=2022' 
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Cirebon():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=TlCukfv%252FcZfhQlKM2KDP2uk61NWCoULqcxJq0FO2%252FB0fuIblaX6Zg5DmP8JA4s0hsLJuraSsWCj%252FZpFZBWMj7Q%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Garut():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=fV%252B2wQkc04RgKhxbS%252F%252Bcg%252Fzhfk16NC72qTf6Rfxnwo2OelHDtZffz4tuIM9cjwNG1WmIl19r8Y0zuGMoSWeKZQ%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Indramayu():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=AqXYeEBaghmTP2V8gQ48e2TWyj%252FoaRtDEaqp4wxTcb2vNwoR9ESutGOADQm7dE%252B2hCbmaB2yjwPHZYW7J2zlRA%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Karawang():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=wyUjSSQ5pWlq%252FgAGzhDQ2gg98sxXI2VjH%252BLGNXuf8muEq%252FY9Y9QF%252BSfUV8WR4thy%252FAWLRkjRIK9tVc%252FgJR1UPQ%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Kuningan():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=u5WThUojN%252BFN04Ou4lwq1y69oIyWnMw7s7er6pDKkYwWue6fsqWmEtjpxt6x%252BUQDb2Ay6g0xhHVADnrNXGN2JQ%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'])
			print('Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Majalengka():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=%252BgkEMhC4kNBoSDCMVLOEPhq2Sv3pP5goXmu2gYkewalvPaAZuK4J6LqLwl8zZOLexXewnzk%252BZxLpe5AqsKBiZQ%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Pangandaran():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=Iumr8ytfSzfLjeSCn7wEuNToqbDfV12XeTouoHvT0qVsrdoPvPsCcHnURxMSNZ8XjDeD3FUuE67u9BK8oqR0cQ%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Purwakakarta():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=MZ8LIKq0VNscz4WZVlcP%252BLrVADAnUXuE3I9DtUcdtSdhB06Ud6lU28npEAAcQRp%252FMD4QeJRsUIql%252FTjYgs1YzQ%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Subang():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=n5B9G%252BeDpxNiAUpviAp433fOXl1Fm8BGaaXnBIjwoOJOarE5gDqoBqwtQqeD%252BFkXsLQyBZJP6Wb7ru2gfnCSWg%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Sukabumi():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=hthP8WdWwXQ9xYmZKpqLYDmmDo3FhriwFML%252B9QALzbctNx29p5HQoNjR8vBPWFXlqYlYEOeKN30WiOjCjF3hWA%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Sumedang():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=https%3A%2F%2Fimsakiyah-api.santrikoding.com%2Fimsyakiyah%3Fstate%3DjHmGZN1Abw26OLYUFJ6CMC%25252Ful%25252BLn39My5vu1IDLVmKub%25252F7amc%25252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%25253D%25253D%26city%3DUOJdfMkynk6uHl7ms4WmuBfOT%25252Boz28ku6wubGZVHo06FdbIGOD2GBg3jQ2mwFPECPozHspF7NO3bhskwYVaI7g%25253D%25253D%26year%3D2022&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def Tasikmalaya():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=Ex5%252B%252B7eEE%252FZAMDo424cT%252BByOwzlTwj6e6qayfAVDaYedfNCwKx8Bdt2Bnz7jc0tDcMP0vyHyHV5mtF%252F3mxxe8Q%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def KotaBandung():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=qBzUNfnJPbyKMa8adt2IyADui5Gdxi0kKz14oJgJviAoo5lGWuV%252FvV0Z81h8MEXSqfAJkEVhbjNFVEV3Bg2lwA%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| msyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def KotaBogor():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=Qynj59poOlfL4zyuawNTx7omDhj8jefgcHMyVcvNcfdwXmtvQ9%252F1K5bmnVOEHb83f2zmWal5Wa8kEce8McrE9A%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def KotaBanjar():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=ZwxAYF%252FxKJ3GN1xs5LvKhU3MOtvsBi139fabhJ51onI86WB1Hp5jXeVpehmIOOgUQL6wIZHSZ6aZ%252F9%252Fa3cuxPA%253D'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*23)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def KotaBekasi():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=nVmleKIIDrc9wdxUua%252BlKSCENnDO7y3l%252FoRyfyWpomgADQEzp%252FWg8wYE%252FGFX%252BG%252ByLkOZqTnyc4hll659NKWoSw%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def KotaCimahi():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=gZ0lzrwIl09pNCdtXkgp7adAGImpWi0WXGQRP3SyfdPRcRKUwod1zXIB%252BKyRtgDq4OcNX3JG9zQBza1ZlMjAyg%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def KotaCirebon():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=K9EfqQ97M0Za8kZcSNTGxvxqKkr5oQVnRpqfk2q2oleAWcaCY0sDn9bgiS13x8QuaVxDVh1dHQQh1%252F4N7y8gRA%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def KotaDepok():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=NN576DD1KKcqG4BZRdNdDvDTA%252BzuHB9L71cBTtUnf6exiWkeqzHvjyo3bMZKmR3pojzdZsHZ7V2XbdcBuq4YlA%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def KotaSukabumi():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=rkxwjXbIMCMRL65P13%252FsZ0nvOR9xeqHrKTqGrAh6cCYvs07AyIVhlfXBVoF%252BQzq4CuCRJQFGxQxnBhJowLLC0g%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')

	def KotaTasikmalaya():
		url='https://imsakiyah-api.santrikoding.com/imsyakiyah?state=jHmGZN1Abw26OLYUFJ6CMC%252Ful%252BLn39My5vu1IDLVmKub%252F7amc%252F8KNWE78WDulWOS4xhiWYfcex3ErFjMTf10FQ%253D%253D&city=ifnT8jI2WTqg7iCfcmnXrFTTOHomc15h%252FOSDqB8h61Lj3CPJjLEuJwNEIy7v%252BmO8Tjp%252Fyr3xDH8M2nLRq2xLfw%253D%253D&year=2022'
		res = req.get(url)
		i = res.json()
		data = i["data"]

		for i in data:
			print('--'*22)
			print(i['date'])
			print('Maghrib',i['maghrib'],'| Imsyak ',i['imsak'],'| Subuh',i['subuh'])
			print('')


	def Menu():
		print('''\t\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT\n---------------------------------------------------------------------
01 KAB. BANDUNG           11 KAB. KUNINGAN      19 KOTA BANDUNG
02 KAB. BANDUNG BARAT     12 KAB. MAJALENGKA    20 KOTA BANJAR
03 KAB. BEKASI            13 KAB. PANGANDARAN   21 KOTA BEKASI
04 KAB. BOGOR             14 KAB. PURWAKARTA    22 KOTA BOGOR
05 KAB. CIAMIS            15 KAB. SUBANG        23 KOTA CIMAHI
06 KAB. CIANJUR           16 KAB. SUKABUMI      24 KOTA CIREBON
07 KAB. CIREBON           17 KAB. SUMEDANG      25 KOTA DEPOK
08 KAB. GARUT             18 KAB. TASIKMALAYA   26 KOTA SUKABUMI
09 KAB. INDRAMAYU                               27 KOTA TASIKMALAYA
10 KAB. KARAWANG                                00 EXIT
		''')
		pilih = int(input('Pilih : '))
		if pilih == 1:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. BANDUNG')
			JawaBarat.Bandung()
		elif pilih == 2:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. BANDUNG BARAT')
			JawaBarat.BandungBarat()
		elif pilih == 3:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. BEKASI')
			JawaBarat.Bekasi()
		elif pilih == 4:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. BOGOR')
			JawaBarat.Bogor()
		elif pilih == 5:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. CIAMIS')
			JawaBarat.Ciamis()
		elif pilih == 6:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. CIANJUR')
			JawaBarat.Cianjur()
		elif pilih == 7:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. CIREBON')
			JawaBarat.Cirebon()
		elif pilih == 8:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. GARUT')
			JawaBarat.Garut()
		elif pilih == 9:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. INDRAMAYU')
			JawaBarat.Indramayu()
		elif pilih == 10:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. KARAWANG')
			JawaBarat.Karawang()
		elif pilih == 11:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. KUNINGAN')
			JawaBarat.Kuningan()
		elif pilih == 12:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. MAJALENGKA')
			JawaBarat.Majalengka()
		elif pilih == 13:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. PANGANDARAN')
			JawaBarat.Pangandaraan()
		elif pilih == 14:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. PURWAKARTA')
			JawaBarat.Purwakarta()
		elif pilih == 15:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. SUBANG')
			JawaBarat.Subang()
		elif pilih == 16:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. SUKABUMI')
			JawaBarat.Sukabumi()
		elif pilih == 17:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. SEUMEDANG')
			JawaBarat.Sumedang()
		elif pilih == 18:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KAB. TASIKMALYA')
			JawaBarat.Tasikmalaya()
		elif pilih == 19:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KOTA BANDUNG')
			JawaBarat.KotaBandung()
		elif pilih == 20:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KOTA BANJAR')
			JawaBarat.KotaBanjar()
		elif pilih == 21:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KOTA BEKASI')
			JawaBarat.KotaBekasi()
		elif pilih == 22:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KOTA BOGOR')
			JawaBarat.KotaBogor()
		elif pilih == 23:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KOTA CIMAHI')
			JawaBarat.KotaCimahi()
		elif pilih == 24:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KOTA CIREBON')
			JawaBarat.KotaCirebon()
		elif pilih == 25:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KOTA DEPOK')
			JawaBarat.KotaDepok()
		elif pilih == 26:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KOTA SUKABUMI')
			JawaBarat.KotaSukabumi()
		elif pilih == 27:
			os.system('clear')
			print('\t\tJADWAL ( MAGHRIB-IMSYAK-SUBUH ) JAWA BARAT,KOTA TASIKMALAYA')
			JawaBarat.KotaTasikmalaya()
		elif pilih == 00:
			pass


os.system('clear')
JawaBarat.Menu()
lagi = input('Cek Jadwal lagi? (y/t) : ')
if lagi == 'y':
	JawaBarat.Menu()
else:
	pass
