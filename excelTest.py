import  xlwings as xw


app=xw.App(visible=True,add_book=False)
app.display_alerts=False
app.screen_updating=False

filepath='/Users/wkc/Desktop/2月有墨月度对账表.xlsx'
wb=app.books.open(filepath)
sht=wb.sheets['执行明细-图文']
sht.activate()
rng=sht.range('K1').expand('table')
nrows=rng.rows.count
a=sht.range(f'K2:K{nrows}').value
zongji = 0
for x in a:
    zongji=zongji+int(x)
print(zongji)
wb.save()
wb.close()
app.quit()
