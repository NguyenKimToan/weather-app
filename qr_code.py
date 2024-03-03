import qrcode
img = qrcode.make('https://nguyenkimtoan.github.io/weather-app/')
img.save('qrweatherApp.png')